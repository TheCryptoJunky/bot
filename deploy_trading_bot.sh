#!/bin/bash
# File: /deploy_trading_bot.sh
# Purpose: Deploy the crypto trading bot via Docker and SSH to the cloud server.
# Key improvements: Ensure error handling, security checks, and logging of the deployment process.

echo "Starting deployment process at $(date)"  # Log start time

# Check if Docker credentials are available
if [ -z "$DOCKER_USERNAME" ] || [ -z "$DOCKER_PASSWORD" ]; then
  echo "Error: Docker credentials are not set."
  exit 1
fi

# Step 1: Build and push Docker images to Docker Hub
echo "Building and pushing Docker images..."
docker-compose -f docker-compose.yml build  # Build images using docker-compose
docker-compose -f docker-compose.yml push   # Push the images to Docker Hub

# Verify success of build and push
if [ $? -eq 0 ]; then
  echo "Docker images built and pushed successfully."
else
  echo "Error: Failed to build or push Docker images."
  exit 1
fi

# Step 2: SSH to the cloud server for deployment
echo "Deploying bot to cloud server..."
ssh -o StrictHostKeyChecking=no user@your_cloud_server << 'EOF'
  echo "Connecting to the server..."

  # Pull the latest Docker image from Docker Hub
  echo "Pulling latest Docker images..."
  docker-compose -f /path/to/your/project/docker-compose.yml pull
  
  # Stop existing containers
  echo "Stopping existing containers..."
  docker-compose -f /path/to/your/project/docker-compose.yml down
  
  # Start new containers in detached mode
  echo "Starting new containers..."
  docker-compose -f /path/to/your/project/docker-compose.yml up -d
  
  # Run MySQL table setup inside the Docker container
  echo "Setting up MySQL database tables..."
  docker exec -it trading_bot python /app/src/database/mysql_setup.py

EOF

# Verify success of deployment
if [ $? -eq 0 ]; then
  echo "Bot deployed successfully."
else
  echo "Error: Deployment failed."
  exit 1
fi

echo "Deployment process completed at $(date)"  # Log end time
