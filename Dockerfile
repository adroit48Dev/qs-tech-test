# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtualenv and activate it
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN /bin/bash -c "source /app/venv/bin/activate"

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the tests
RUN python3 -m pytest tests/

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]