# Base image
FROM python:3.9-slim

# Copy app, templates and views
COPY . /app

# Set working directory for subsequent commands
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Command to run when container starts
ENTRYPOINT ["python", "app/app.py"]
