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

Certainly! Here's a section you can add to your README in Markdown code to explain how to run your WhatsApp poll bot using Docker:

```markdown
## Running with Docker

To run this WhatsApp poll bot using Docker, follow these steps:

1. **Build the Docker Image:**

   Open a terminal and navigate to the directory containing the Dockerfile and your project files. Build the Docker image by running the following command:

   ```bash
   docker build -t WhatsApp-Poll-Bot .
   ```

   Replace `WhatsApp-Poll-Bot` with your desired image name.

2. **Run the Docker Container:**

   Once the Docker image is built, you can run the Docker container using the following command:

   ```bash
   docker run -p 5000:5000 WhatsApp-Poll-Bot
   ```

   This command will start the WhatsApp poll bot inside a Docker container, and it will be accessible on port 5000 of your server.

3. **Configure Twilio:**

   Configure your Twilio WhatsApp number to use the public IP address or domain of your server for incoming messages and webhooks. Ensure that your bot's endpoint is set to `http://your-server-ip:5000/` or `http://your-domain:5000/` depending on your server setup.

4. **Access the Bot:**

   You can now access and interact with your WhatsApp poll bot by sending messages to your Twilio WhatsApp number.

**Note:** Make sure to replace `WhatsApp-Poll-Bot` with your actual Docker image name if you used a different name during the image build.

Enjoy using your WhatsApp poll bot with Docker!
```

You can add this section to your existing README to provide clear instructions on how to run your bot using Docker.
```
## Notes

- This is a basic example of a WhatsApp poll bot. You can extend it to add more features, such as storing and analyzing poll results.
- Ensure that your Twilio account is set up with WhatsApp API access and a phone number.
- Make sure Ngrok or a similar tool is running to expose your local server to the internet for the Twilio webhook.
```

You can replace `'your_account_sid'` and `'your_auth_token'` with your actual Twilio credentials, and make any other necessary adjustments to fit your specific setup.
```
