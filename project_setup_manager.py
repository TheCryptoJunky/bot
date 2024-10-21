import os
import re
import subprocess
import sys
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Define the project root and relevant files
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_ROOT, 'requirements.txt')
ENV_FILE = os.path.join(PROJECT_ROOT, '.env')
CONFIG_FILE = os.path.join(PROJECT_ROOT, 'config.py')
DOCKERFILE = os.path.join(PROJECT_ROOT, 'Dockerfile')
DOCKER_COMPOSE = os.path.join(PROJECT_ROOT, 'docker-compose.yml')

# Load environment variables from .env
load_dotenv(dotenv_path=ENV_FILE)

def update_requirements():
    """
    Scans the entire directory for missing dependencies and updates the requirements.txt file.
    """
    print("Updating requirements.txt based on the project files...")

    # Traverse the entire project directory
    required_packages = set()
    
    for root, dirs, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    # Open file with UTF-8 encoding to avoid UnicodeDecodeError
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            match = re.search(r'import (\S+)|from (\S+) import', line)
                            if match:
                                package = match.group(1) or match.group(2)
                                required_packages.add(package.split('.')[0])
                except UnicodeDecodeError as e:
                    print(f"Error reading {file_path}: {e}")

    # Write the requirements.txt file
    with open(REQUIREMENTS_FILE, 'w') as f:
        for package in sorted(required_packages):
            f.write(f"{package}\n")

    print("requirements.txt updated successfully!")

def check_mysql():
    """
    Ensures MySQL is installed and sets up the initial tables if needed.
    """
    print("Checking MySQL installation...")
    
    try:
        # Try connecting to MySQL
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', 'test_db')
        )
        
        if connection.is_connected():
            print(f"Connected to MySQL server. Database '{os.getenv('MYSQL_DATABASE')}' is ready.")
            connection.close()

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print("Attempting to install MySQL...")

        # Install MySQL based on the current operating system
        if sys.platform.startswith('linux'):
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mysql-server', 'mysql-client'], check=True)
        elif sys.platform == 'darwin':
            subprocess.run(['brew', 'install', 'mysql'], check=True)
        elif sys.platform.startswith('win'):
            print("Please install MySQL manually on Windows.")
            return

        # Start MySQL service after installation
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            subprocess.run(['sudo', 'service', 'mysql', 'start'], check=True)
            print("MySQL installation complete. Please create the initial tables manually or in the project.")

def update_docker_files():
    """
    Ensures Dockerfile and docker-compose.yml are properly modularized and set up for deployment.
    """
    print("Updating Docker configuration...")

    if not os.path.exists(DOCKERFILE):
        with open(DOCKERFILE, 'w') as f:
            f.write("""
# Dockerfile for the Python project
FROM python:3.9-slim

WORKDIR /app

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run the project
CMD ["python", "main.py"]
""")
        print("Dockerfile created!")

    if not os.path.exists(DOCKER_COMPOSE):
        with open(DOCKER_COMPOSE, 'w') as f:
            f.write("""
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      MYSQL_HOST: ${MYSQL_HOST}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: mysql:5.7
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
""")
        print("docker-compose.yml created!")

def update_config_and_env():
    """
    Updates config.py and .env to ensure modularity in database and project settings.
    """
    print("Updating config.py and .env...")

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            f.write("""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'test_db')

config = Config()
""")
        print("config.py created!")

    if not os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'w') as f:
            f.write("""
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database
""")
        print(".env file created!")

def create_deployment_script():
    """
    Creates an automated deployment script to set up and deploy the project.
    """
    deployment_script = os.path.join(PROJECT_ROOT, 'deploy_project.sh')

    with open(deployment_script, 'w') as f:
        f.write("""
#!/bin/bash

echo "Starting deployment..."

# Ensure virtual environment is set up
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up database..."
python src/database/mysql_setup.py

echo "Running Docker setup..."
docker-compose up --build -d

echo "Deployment complete!"
""")
    
    # Make the script executable
    os.chmod(deployment_script, 0o755)
    print("Deployment script created: deploy_project.sh")

if __name__ == "__main__":
    update_requirements()
    update_config_and_env()
    update_docker_files()
    check_mysql()
    create_deployment_script()
    print("Project setup complete.")
