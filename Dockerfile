# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --noinput

# Run Gunicorn
#CMD ["gunicorn", "online_survey.wsgi:application", "--bind", "0.0.0.0:8001"]

RUN apt-get update && apt-get install -y ncat

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
