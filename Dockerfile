# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Run database migrations
RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "MyDjangoProjectSec.wsgi:application", "--bind", "0.0.0.0:8000"]
