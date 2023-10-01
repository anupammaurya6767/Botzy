# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the bot source code to the working directory
COPY . .

# Replace 'YOUR_BOT_TOKEN' with your actual bot token in the code
ENV BOT_TOKEN=YOUR_BOT_TOKEN

# Expose the port your bot is listening on (if applicable)
# EXPOSE 3000

# Command to start your bot
CMD ["node", "your-bot-file.js"]
