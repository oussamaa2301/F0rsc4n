# Use an existing Docker image as the base
FROM python:3.8

# Set the working directory to /app
WORKDIR /Logis

# Copy the current directory contents into the container at /app
COPY . /Logis

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME env

# Run app.py when the container launches
CMD ["python", "app.py"]
