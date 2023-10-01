# Use the official Python image as a parent image
FROM python:3.9-slim

# Set environment variables for Twilio credentials
ENV TWILIO_ACCOUNT_SID=your_account_sid
ENV TWILIO_AUTH_TOKEN=your_auth_token
ENV TWILIO_PHONE_NUMBER=your_twilio_phone_number

# Set environment variables for Flask
ENV FLASK_APP=app.py

# Create and set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that your Flask app will run on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
