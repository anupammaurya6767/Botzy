# Import the necessary libraries
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# Set up your Twilio account credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Create a Flask web application
app = Flask(__name__)

# Define a dictionary to store poll questions and options
polls = {}

# Define a function to send poll questions to users
def send_poll_question(to, question, options):
    message_body = f"{question}\nOptions: {', '.join(options)}"
    client.messages.create(body=message_body, from_='your_twilio_number', to=to)

# Handle incoming WhatsApp messages
@app.route('/webhook', methods=['POST'])
def webhook():
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)

    if body.lower() == 'start':
        # Start a new poll
        polls[from_number] = {'question': '', 'options': []}
        return str(MessagingResponse().message("Enter your poll question:"))
    elif from_number in polls:
        if not polls[from_number]['question']:
            # Store the poll question
            polls[from_number]['question'] = body
            return str(MessagingResponse().message("Enter poll options (comma-separated):"))
        else:
            # Store poll options
            options = body.split(',')
            polls[from_number]['options'] = [option.strip() for option in options]

            # Send the poll question and options
            send_poll_question(from_number, polls[from_number]['question'], polls[from_number]['options'])

            # Clear the poll data
            del polls[from_number]

    return str(MessagingResponse().message("Invalid command. Send 'start' to create a new poll."))

if __name__ == '__main__':
    app.run(debug=True)
