import os
import subprocess
import sys
import logging
from pathlib import Path

# Setup logging to capture the output of the script
log_file = 'package_mysql_setup.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_command(command):
    """
    Run a shell command and log its output. If the command fails, log the error.
    """
    try:
        logging.info(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running command: {' '.join(command)}\n{e.stderr}")
        sys.exit(1)

def is_virtual_env():
    """
    Check if the script is running inside a virtual environment.
    """
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def activate_virtual_env(venv_path):
    """
    Try to activate the virtual environment if it's not already active.
    """
    if sys.platform == "win32":
        activate_script = venv_path / 'Scripts' / 'activate.bat'
    else:
        activate_script = venv_path / 'bin' / 'activate'
    
    if activate_script.exists():
        logging.info(f"Activating virtual environment at {venv_path}...")
        run_command(['source', str(activate_script)])
    else:
        logging.error(f"Could not find activation script at {activate_script}. Exiting...")
        sys.exit(1)

def upgrade_pip():
    """
    Upgrade pip to the latest version inside the virtual environment.
    """
    logging.info("Upgrading pip...")
    run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

def list_outdated_packages():
    """
    List all outdated packages in the virtual environment.
    """
    logging.info("Listing outdated packages...")
    result = subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated'], capture_output=True, text=True)
    outdated_packages = result.stdout.splitlines()
    for package in outdated_packages:
        logging.info(f"Outdated package: {package}")
    return outdated_packages

def upgrade_outdated_packages():
    """
    Upgrade all outdated packages in the virtual environment.
    """
    logging.info("Upgrading all outdated packages...")
    outdated = subprocess.run([sys.executable, '-m', 'pip', 'list', '--outdated', '--format=freeze'], capture_output=True, text=True)
    packages = [line.split('=')[0] for line in outdated.stdout.splitlines()]
    if packages:
        run_command([sys.executable, '-m', 'pip', 'install', '--upgrade'] + packages)
    else:
        logging.info("No outdated packages found.")

def reinstall_from_requirements():
    """
    Reinstall dependencies from requirements.txt, adjusting incompatible versions if necessary.
    """
    requirements_path = 'requirements.txt'
    if os.path.exists(requirements_path):
        logging.info(f"Reinstalling dependencies from {requirements_path} with latest compatible versions...")
        try:
            run_command([sys.executable, '-m', 'pip', 'install', '-r', requirements_path, '--upgrade', '--use-deprecated=legacy-resolver'])
        except subprocess.CalledProcessError as e:
            logging.error(f"Error installing requirements: {str(e)}")
            sys.exit(1)
    else:
        logging.warning(f"No {requirements_path} found.")

def resolve_tensorflow_version():
    """
    Resolve the latest compatible version of TensorFlow for the current Python version.
    """
    logging.info("Resolving the latest compatible version of TensorFlow...")
    try:
        # Automatically install the compatible version of TensorFlow
        run_command([sys.executable, '-m', 'pip', 'install', 'tensorflow'])
    except Exception as e:
        logging.error(f"Error resolving TensorFlow version: {str(e)}")
        sys.exit(1)

def install_mysql_connector():
    """
    Ensure the MySQL Python connector is installed for MySQL connection.
    """
    logging.info("Installing MySQL Connector for Python...")
    try:
        run_command([sys.executable, '-m', 'pip', 'install', 'mysql-connector-python'])
    except Exception as e:
        logging.error(f"Error installing MySQL connector: {str(e)}")
        sys.exit(1)

def install_mysql():
    """
    Install MySQL server and client locally based on the operating system.
    """
    logging.info("Installing MySQL...")
    
    try:
        # Install MySQL based on the current operating system
        if sys.platform == "linux" or sys.platform == "linux2":
            logging.info("Installing MySQL on Linux...")
            run_command(['sudo', 'apt-get', 'install', '-y', 'mysql-server', 'mysql-client'])
        elif sys.platform == "darwin":
            logging.info("Installing MySQL on macOS...")
            run_command(['brew', 'install', 'mysql'])
        elif sys.platform == "win32":
            logging.warning("Please install MySQL manually on Windows.")
            logging.warning("Windows MySQL installation is not handled automatically.")

        # Start MySQL service for Linux/macOS
        if sys.platform != "win32":
            run_command(['sudo', 'service', 'mysql', 'start'])

    except Exception as e:
        logging.error(f"MySQL installation failed: {str(e)}")
        sys.exit(1)

def setup_mysql_database():
    """
    Run the project's MySQL setup script to create tables in the MySQL database.
    """
    mysql_setup_path = os.path.join('src', 'database', 'mysql_setup.py')
    if os.path.exists(mysql_setup_path):
        logging.info(f"Running MySQL setup script: {mysql_setup_path}")
        run_command([sys.executable, mysql_setup_path])
    else:
        logging.error(f"MySQL setup script not found at {mysql_setup_path}.")
        sys.exit(1)

def verify_mysql_connection():
    """
    Verifies if MySQL is running and can be accessed with credentials from .env.
    """
    try:
        import mysql.connector
        from dotenv import load_dotenv

        # Load environment variables from .env
        load_dotenv()

        # Fetch MySQL credentials from .env
        mysql_host = os.getenv('MYSQL_HOST', 'localhost')
        mysql_user = os.getenv('MYSQL_USER', 'root')
        mysql_password = os.getenv('MYSQL_PASSWORD', '')
        mysql_db = os.getenv('MYSQL_DATABASE', 'test_db')

        # Test MySQL connection
        connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_db
        )
        logging.info(f"Successfully connected to MySQL database '{mysql_db}' on host '{mysql_host}'")
        connection.close()
    except Exception as e:
        logging.error(f"MySQL connection failed: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    logging.info("Starting virtual environment verification and package/MySQL setup...")

    # Check if inside a virtual environment
    if not is_virtual_env():
        logging.error("Not inside a virtual environment. Please activate the virtual environment and try again.")
        sys.exit(1)
    else:
        logging.info("Virtual environment is active.")

    # Step 1: Upgrade pip
    upgrade_pip()

    # Step 2: List outdated packages
    list_outdated_packages()

    # Step 3: Upgrade all outdated packages
    upgrade_outdated_packages()

    # Step 4: Reinstall from requirements.txt (if available)
    reinstall_from_requirements()

    # Step 5: Resolve TensorFlow version
    resolve_tensorflow_version()

    # Step 6: Install MySQL Connector
    install_mysql_connector()

    # Step 7: Install MySQL locally
    install_mysql()

    # Step 8: Run the MySQL setup script to create tables
    setup_mysql_database()

    # Step 9: Verify MySQL connection using credentials from .env
    verify_mysql_connection()

    logging.info("Package upgrade and MySQL setup process completed successfully.")
    print(f"Process completed! Check '{log_file}' for details.")
