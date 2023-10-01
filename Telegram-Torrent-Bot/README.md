# Telegram Torrent Downloader Bot

This Telegram bot allows you to download torrents via magnet links directly to your server. You can manage and monitor your torrent downloads with ease.

## Usage

1. Start a chat with the Telegram bot.

2. Use the following commands to interact with the bot:

   - `/start`: Displays a welcome message.

   - `/download <torrent_link>`: Initiates the download of a torrent file using the provided magnet link.

   - `/progress`: Checks the progress of ongoing downloads.

   - `/list`: Lists downloaded torrents with details.

   - `/pause`: Pauses ongoing downloads.

   - `/resume`: Resumes paused downloads.

   - `/cancel`: Cancels downloads in progress.

   - `/delete`: Deletes downloaded torrents.

## Docker Run

You can run the Telegram Torrent Downloader Bot using Docker. Here are the steps:

1. Build the Docker image:

   ```bash
   docker build -t telegram-torrent-bot .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 4000:80 telegram-torrent-bot
   ```

Replace `telegram-torrent-bot` with the desired image name and `-p 4000:80` with the desired port mapping if you're using a different port.

## Contributing

Contributions are welcome! If you have any improvements or feature suggestions, feel free to submit a pull request.
