# Discord Music Bot

A simple Discord music bot powered by the `discord.js-musicbot-addon` library. This bot allows you to play music in your Discord server without the need for a YouTube API key.

## Features

- Play music from various sources
- Skip, pause, and resume playback
- Clear the queue
- Display queue status
- Owner-only commands
- Help command for easy navigation

## Usage

1. **Invite the Bot to Your Server**

   - Invite the bot to your Discord server using the following link:
     [Invite Bot](https://discord.com/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&scope=bot&permissions=YOUR_BOT_PERMISSIONS)

2. **Bot Commands**

   - Use the bot's prefix (default is `-`) followed by commands to interact with the bot.
   - Example commands:
     - `-play <song name or URL>`: Play a song from various sources.
     - `-skip`: Skip the current song.
     - `-pause`: Pause the current song.
     - `-resume`: Resume the paused song.
     - `-stop`: Stop the song and clear the queue.
     - `-help`: Display the list of available commands.

3. **Bot Owner Commands**

   - Certain commands are available only to the bot owner (specified in the code).
   - Example owner command:
     - `-owner`: Display owner-only commands.

4. **Bot Configuration (Optional)**

   - You can customize the bot's prefix, presence, and other settings in the code to suit your preferences.

## Prerequisites

- Node.js
- Discord account

## Installation

1. Clone or download this repository.
2. Install the required dependencies using `npm install`.
3. Replace `'YOUR_BOT_TOKEN'` with your bot's token in the code.

## Running the Bot

- Start the bot by running `node your-bot-file.js`.

## Running with Docker

You can run the Discord music bot inside a Docker container. Docker provides a consistent and isolated environment for your bot.

### Prerequisites

- Docker installed on your server.

### Steps

1. **Build the Docker Image**

   - In the project directory where the `Dockerfile` is located, run the following command to build the Docker image:

     ```bash
     docker build -t your-bot-image .
     ```

   Replace `your-bot-image` with a suitable name for your Docker image.

2. **Run the Docker Container**

   - Once the Docker image is built, you can run a Docker container using the following command:

     ```bash
     docker run -d your-bot-image
     ```

   This command starts a container based on the image you built and runs your Discord music bot inside the container.

3. **Verify Bot Status**

   - To verify that your bot is up and running inside the Docker container, you can check the container logs:

     ```bash
     docker logs <container_id>
     ```

   Replace `<container_id>` with the actual ID or name of the running container.

4. **Interacting with the Bot**

   - You can now interact with your Discord music bot as usual using the bot's commands.

   ```text
   Example: -play <song name or URL>
   ```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests to improve the bot.
