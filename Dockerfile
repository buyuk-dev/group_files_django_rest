# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container at /app/
COPY Pipfile Pipfile.lock key.pem cert.pem /app/

# Install project dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your application's code into the container at /app/
COPY ./rest /app/

# Collect static files
RUN pipenv run python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 443

# Start Gunicorn
CMD ["pipenv", "run", "gunicorn", "--certfile", "/app/cert.pem", "--keyfile", "/app/key.pem", "rest.wsgi:application", "--bind", "0.0.0.0:443"]
