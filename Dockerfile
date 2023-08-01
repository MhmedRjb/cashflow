FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the app files into the container
COPY . /app

# Install app dependencies

RUN pip install -r requirements.txt

# Expose the port your Flask app will be running on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
