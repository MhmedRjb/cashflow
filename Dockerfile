# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy all necessary files to the container
COPY . .

# Expose the port that your Flask app will run on
EXPOSE 5000

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to start the Flask app
CMD ["python", "app.py"]
