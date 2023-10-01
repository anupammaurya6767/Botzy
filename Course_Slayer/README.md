# Course Slayer Bot - Telegram Bot for Courses

Course Slayer Bot is a Telegram bot that helps users request and access various courses. It's designed to streamline the process of sharing courses from a list stored in a Google Spreadsheet. With Course Slayer Bot, you can easily request courses and receive the information you need.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [How to Run with Docker](#how-to-run-with-docker)

## Getting Started

### Prerequisites

Before running Course Slayer Bot, ensure you have the following prerequisites:

- Node.js (Version 16.16.0 recommended)
- npm (Node Package Manager)
- Telegram Bot API Token
- Google Spreadsheet with course data

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/course-slayer-bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd course-slayer-bot
   ```

3. Install the required Node.js packages:

   ```bash
   npm install
   ```

### Configuration

To configure Course Slayer Bot, you'll need to set up the following environment variables:

- `TELEGRAM_BOT_TOKEN`: Your Telegram Bot API token.
- `GOOGLE_SPREADSHEET_ID`: The ID of the Google Spreadsheet containing the course data.
- `GOOGLE_SERVICE_ACCOUNT_CREDENTIALS`: The service account credentials for accessing the Google Spreadsheet (in JSON format).
- Additional configuration variables as needed for your specific bot functionality.

## Usage

1. Start the bot by running:

   ```bash
   node index.js
   ```

2. Interact with the bot in your Telegram group or chat. You can use commands such as `/request` to request courses and `/get` to retrieve course information.

3. The bot will handle course requests and provide course details from the Google Spreadsheet.

## How to Run with Docker

You can also run Course Slayer Bot using Docker:


1. Build a Docker image from the provided Dockerfile:

   ```bash
   docker build -t course-slayer-bot .
   ```

2. Run the Docker container:

   ```bash
   docker run -d course-slayer-bot
   ```
Note: 
 Replace `your_bot_token`, `your_spreadsheet_id`, and `your_service_account_credentials_json` with your actual bot and Google Spreadsheet information.
