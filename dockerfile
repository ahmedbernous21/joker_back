# Use an official Python runtime as a parent image
FROM python:3.10.1

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=joker.settings

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Install Python dependencies
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the rest of the application code
ADD . /code/
