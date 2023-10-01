import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import libtorrent as lt
import time

# Telegram bot token (replace with your own token)
TOKEN = "your_telegram_token"

# Path to the directory where downloaded torrents will be saved
DOWNLOAD_PATH = "path_to_download_directory"

# Initialize the Telegram bot
bot = telegram.Bot(token=TOKEN)

# Dictionary to store torrent handles
torrent_handles = {}

# Function to handle the '/start' command
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Welcome to the Torrent Downloader Bot!"
    )

# Function to handle torrent download command
def download_torrent(update, context):
    # Get the user's message
    message = update.message.text

    # Extract the torrent link
    torrent_link = message.split(" ")[1]

    # Create a session for torrent downloading
    ses = lt.session()

    # Set download directory
    ses.set_download_settings({"save_path": DOWNLOAD_PATH})

    # Add the torrent to the session
    handle = lt.add_magnet_uri(ses, torrent_link)

    # Start downloading the torrent
    ses.start_dht()
    ses.start_lsd()
    ses.start_upnp()
    ses.start_natpmp()

    # Check if the torrent has been successfully added
    if handle.is_valid():
        # Set download location for the torrent
        handle.set_download_mode(lt.torrent_handle.download_mode_t(1))
        
        # Save the handle for future reference
        torrent_handles[update.effective_chat.id] = handle

        update.message.reply_text("Downloading the torrent...")
    else:
        update.message.reply_text("Invalid torrent link.")

# Function to check download progress
def progress(update, context):
    if update.effective_chat.id not in torrent_handles:
        update.message.reply_text("No active downloads.")
        return

    handle = torrent_handles[update.effective_chat.id]
    status = handle.status()
    progress = int(status.progress * 100)
    update.message.reply_text(f"Download Progress: {progress}%")

# Function to list downloaded torrents
def list_torrents(update, context):
    torrent_list = os.listdir(DOWNLOAD_PATH)
    if not torrent_list:
        update.message.reply_text("No downloaded torrents.")
        return

    update.message.reply_text("List of downloaded torrents:")
    for torrent in torrent_list:
        update.message.reply_text(torrent)

# Function to pause an ongoing download
def pause(update, context):
    if update.effective_chat.id not in torrent_handles:
        update.message.reply_text("No active downloads to pause.")
        return

    handle = torrent_handles[update.effective_chat.id]
    handle.pause()
    update.message.reply_text("Download paused.")

# Function to resume a paused download
def resume(update, context):
    if update.effective_chat.id not in torrent_handles:
        update.message.reply_text("No paused downloads to resume.")
        return

    handle = torrent_handles[update.effective_chat.id]
    handle.resume()
    update.message.reply_text("Download resumed.")

# Function to cancel and remove a download
def cancel(update, context):
    if update.effective_chat.id not in torrent_handles:
        update.message.reply_text("No active downloads to cancel.")
        return

    handle = torrent_handles[update.effective_chat.id]
    handle.abort()
    del torrent_handles[update.effective_chat.id]
    update.message.reply_text("Download canceled and removed.")

# Function to delete a downloaded torrent
def delete(update, context):
    message = update.message.text

    if len(message.split(" ")) < 2:
        update.message.reply_text("Please provide the name of the torrent to delete.")
        return

    torrent_name = message.split(" ")[1]

    try:
        os.remove(os.path.join(DOWNLOAD_PATH, torrent_name))
        update.message.reply_text(f"Torrent '{torrent_name}' deleted successfully.")
    except Exception as e:
        update.message.reply_text(f"Failed to delete torrent: {e}")

# Function to handle any other messages
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sorry, I don't understand that command."
    )

# Main function to run the Telegram bot
def main():
    # Create an instance of the Updater class
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_torrent))
    dispatcher.add_handler(CommandHandler("progress", progress))
    dispatcher.add_handler(CommandHandler("list", list_torrents))
    dispatcher.add_handler(CommandHandler("pause", pause))
    dispatcher.add_handler(CommandHandler("resume", resume))
    dispatcher.add_handler(CommandHandler("cancel", cancel))
    dispatcher.add_handler(CommandHandler("delete", delete))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl+C is pressed
    updater.idle()

if __name__ == "__main__":
    main()
