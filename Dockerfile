# Use official Python image
FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /usr/src/app  

# Copy and install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start Django server (Without Gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
