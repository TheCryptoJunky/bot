
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
