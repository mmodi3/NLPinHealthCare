# from twilio.rest import Client
# import sys
# import requests
# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse
# app = Flask(__name__)
# account_sid = "AC5b5e6e2dd9a7748ee5f56aac847f6f57"
# auth_token  = "92243c7755e8aeda70c62738f768181d"

# def process_input(msg):
#     headers = {
#         # Request headers
#         'Ocp-Apim-Subscription-Key': 'e74ec3d437c84103b0cda324cef1473e',
#     }
#     params ={
#         # Query parameter
#         'q': msg,
#         # Optional request parameters, set to default values
#         'timezoneOffset': '0',
#         'verbose': 'false',
#         'spellCheck': 'false',
#         'staging': 'false',
#     }
#     try:
#         r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/a7985484-8966-4125-969a-e13be956d301',headers=headers, params=params)
#         print(r.json())
#         return r.json()

#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))

# @app.route("/sms", methods=['GET', 'POST'])
# def incoming_sms():
#     """Send a dynamic reply to an incoming text message"""
#     # Get the message the user sent our Twilio number
#     body = request.values.get('Body', None)

#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Determine the right reply for this message
#     if body == 'hello':
#         resp.message("Hi!")
#     elif body == 'bye':
#         resp.message("Goodbye")

#     return str(resp)


# # message_body = request.values.get('Body', None)
# # response = MessagingResponse()
# # response.message(str(process_input(message_body)))

# # message = client.messages.create(
# #     to="+19733687203", 
# #     from_="+19737848845",
# #     body= str(process_input("advil?")))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)