import os
import re
import subprocess
import sys
import logging
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Define the project root and source directory
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, 'src')

# Setup logging
log_file = os.path.join(PROJECT_ROOT, 'project_setup.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Start logging
logging.info("Starting project setup...")

# Updated regex pattern to capture both 'import' and 'from ... import ...' statements
IMPORT_PATTERN = re.compile(r'^(from|import)\s+([a-zA-Z0-9_\.]+)')

# Dictionary to store found modules and their corresponding file paths
module_paths = {}

# Recursively scan for all Python files and map modules to their file paths
def scan_directory_for_modules():
    """
    Scans the src directory for Python modules and stores their paths for later reference.
    """
    logging.info("Scanning directories for Python modules...")
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Determine the module path based on the file location
                module_name = os.path.relpath(file_path, SRC_DIR).replace(os.sep, '.').replace('.py', '')
                module_paths[module_name] = file_path
                logging.info(f"Found module: {module_name} -> {file_path}")
    logging.info("Module scan completed.")

# Detect and fix import path issues
def fix_imports_in_file(file_path):
    """
    Analyze the imports in the file and fix any incorrect paths based on the actual module paths.
    """
    logging.info(f"Fixing imports in file: {file_path}")
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        new_lines = []
        modified = False

        for line in lines:
            # Check for 'from' or 'import' statements
            match = IMPORT_PATTERN.match(line.strip())
            if match:
                import_type, imported_module = match.groups()
                # If the imported module is found in the module paths, correct the path
                if imported_module in module_paths:
                    correct_import = line.replace(imported_module, f"src.{imported_module}")
                    logging.info(f"Fixing import: {line.strip()} -> {correct_import.strip()}")
                    new_lines.append(correct_import)
                    modified = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        # Overwrite the file if changes were made
        if modified:
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
            logging.info(f"Updated imports in {file_path}")

    except Exception as e:
        logging.error(f"Error fixing imports in {file_path}: {str(e)}")

# Fix all imports across the project
def fix_imports():
    """
    Scans all files in the project and fixes the imports based on the scanned module paths.
    """
    logging.info("Starting to fix imports across the project...")
    for root, dirs, files in os.walk(SRC_DIR):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                fix_imports_in_file(file_path)
    logging.info("Finished fixing imports.")

# Install requirements from the requirements.txt file
def install_requirements():
    """
    Installs all dependencies listed in the requirements.txt file.
    """
    requirements_path = os.path.join(PROJECT_ROOT, 'requirements.txt')
    if os.path.exists(requirements_path):
        logging.info("Installing dependencies from requirements.txt...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
            logging.info("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error installing requirements: {str(e)}")
    else:
        logging.warning("No requirements.txt found.")

# Install MySQL and set up the database locally
def install_mysql_and_setup_db():
    """
    Install MySQL (if necessary) and run the project's MySQL setup script to create tables.
    """
    logging.info("Installing MySQL and setting up the database...")

    try:
        # Install MySQL based on the current operating system
        if sys.platform == "linux" or sys.platform == "linux2":
            logging.info("Installing MySQL on Linux...")
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mysql-server', 'mysql-client'])
        elif sys.platform == "darwin":
            logging.info("Installing MySQL on macOS...")
            subprocess.run(['brew', 'install', 'mysql'])
        elif sys.platform == "win32":
            logging.warning("Please install MySQL manually on Windows.")

        # Ensure MySQL service is running (for Linux/macOS)
        if sys.platform != "win32":
            subprocess.run(['sudo', 'service', 'mysql', 'start'])

        # Run the MySQL setup script to create tables
        mysql_setup_path = os.path.join(SRC_DIR, 'database', 'mysql_setup.py')
        if os.path.exists(mysql_setup_path):
            logging.info(f"Running MySQL setup script: {mysql_setup_path}")
            subprocess.check_call([sys.executable, mysql_setup_path])
        else:
            logging.error("MySQL setup script not found. Please ensure mysql_setup.py is in /src/database/.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error during MySQL setup: {str(e)}")

# Install OS-specific dependencies if needed
def install_os_specific_dependencies():
    """
    Install any OS-specific packages if necessary (example: MySQL client libraries, system-level dependencies).
    """
    logging.info("Installing OS-specific dependencies...")
    try:
        if sys.platform == "linux" or sys.platform == "linux2":
            logging.info("Installing Linux-specific dependencies...")
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', 'libmysqlclient-dev'])
        elif sys.platform == "darwin":
            logging.info("Installing macOS-specific dependencies...")
            subprocess.check_call(['brew', 'install', 'mysql-client'])
        elif sys.platform == "win32":
            logging.warning("Windows-specific dependency installation not included, please install manually if needed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during OS-specific dependency installation: {str(e)}")

# Verify that the environment is properly set up
def verify_setup():
    """
    Verify that all necessary dependencies are installed, .env is loaded, and Python environment is correct.
    """
    logging.info("Verifying environment setup...")

    # Check if .env was loaded correctly
    if 'MYSQL_HOST' in os.environ:
        logging.info(f".env file loaded successfully. MYSQL_HOST: {os.environ['MYSQL_HOST']}")
    else:
        logging.warning("Warning: .env file not loaded or missing required environment variables.")

    # Check for installed packages
    try:
        import mysql.connector
        import dotenv
        logging.info("All required packages are installed.")
    except ImportError as e:
        logging.error(f"Missing package: {str(e)}")

if __name__ == '__main__':
    logging.info("Starting full project scan and import path fix...")

    # Step 1: Scan for modules in the src directory
    scan_directory_for_modules()

    # Step 2: Fix imports based on the current directory structure
    fix_imports()

    # Step 3: Install necessary Python dependencies
    install_requirements()

    # Step 4: Install OS-specific dependencies (if any)
    install_os_specific_dependencies()

    # Step 5: Install MySQL and set up the database
    install_mysql_and_setup_db()

    # Step 6: Verify the environment is set up correctly
    verify_setup()

    logging.info("Process completed. Please check the log for details.")
    print("Process completed. Check 'project_setup.log' for details.")
