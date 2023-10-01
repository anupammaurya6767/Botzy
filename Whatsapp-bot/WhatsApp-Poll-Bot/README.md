# WhatsApp Poll Bot

A simple WhatsApp poll bot built with Python and the Twilio API.

## Setup

### Prerequisites

1. Python 3.x installed on your system.
2. A Twilio account with WhatsApp API access.
3. Ngrok or a similar tool for exposing a local web server to the internet (for webhook).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/anupammaurya6767/Botzy.git
   ```

2. Navigate to the project directory:

   ```bash
   cd WhatsApp-Poll-Bot
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Twilio account credentials in the `app.py` file:

   ```python
   # Set up your Twilio account credentials
   account_sid = 'your_account_sid'
   auth_token = 'your_auth_token'
   ```

5. Replace `'your_twilio_number'` in the code with your Twilio phone number.

### Usage

1. Start the Flask web application:

   ```bash
   python app.py
   ```

2. Expose the local web server to the internet using Ngrok or a similar tool. Run Ngrok with the following command:

   ```bash
   ngrok http 5000
   ```

   Note: Update the Twilio webhook URL in your Twilio dashboard to point to the Ngrok URL.

3. Send a WhatsApp message to your Twilio phone number with the following commands:

   - Send 'start' to create a new poll.
   - Follow the prompts to enter the poll question and options.
   - The bot will send the poll question and options to the user.

4. Respond to the bot's prompts to configure and send polls to WhatsApp users.

## Notes

- This is a basic example of a WhatsApp poll bot. You can extend it to add more features, such as storing and analyzing poll results.
- Ensure that your Twilio account is set up with WhatsApp API access and a phone number.
- Make sure Ngrok or a similar tool is running to expose your local server to the internet for the Twilio webhook.
```

You can replace `'your_account_sid'` and `'your_auth_token'` with your actual Twilio credentials, and make any other necessary adjustments to fit your specific setup.
```
