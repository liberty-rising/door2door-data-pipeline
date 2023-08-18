# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable for AWS Credentials (if you're using boto3 or AWS SDK in the application)
# It's recommended to pass these as secrets or use IAM roles in a real-world scenario
ENV AWS_ACCESS_KEY_ID=your_access_key
ENV AWS_SECRET_ACCESS_KEY=your_secret_key

# Run app.py when the container launches
CMD ["python", "app.py"]
