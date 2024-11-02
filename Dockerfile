# Use an appropriate base image
FROM python:3.11-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3-flask python3-psutil && \
    apt-get install -y python3-pip

# Upgrade pip
RUN pip install --upgrade pip

# Install your Python packages
RUN pip install --upgrade tornado flask_socketio docker

# Set up the working directory
WORKDIR /app

# Copy your application code to the container
COPY . .

# Command to run your application (change as needed)
CMD ["python3", "app.py"]
