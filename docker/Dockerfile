# Dockerfile
FROM python:3.11-slim

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip-tools for dev management
RUN pip install --upgrade pip

# Copy requirements
COPY ../backend/requirements.txt /app/

RUN pip install -r requirements.txt

# Copy project files
COPY ../backend/ /app/

# Default command (overridden in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
