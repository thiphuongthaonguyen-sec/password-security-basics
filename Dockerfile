# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY password_hash.py .

# Default command
CMD ["python", "password_hash.py"]
