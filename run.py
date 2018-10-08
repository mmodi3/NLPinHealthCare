from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pinocchio import *
import sys
import errno
import json
import requests

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    message_body = request.form['Body']


    resp = MessagingResponse()

    # Add a message
    resp.message(str(process_input(message_body)))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
