from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC5b5e6e2dd9a7748ee5f56aac847f6f57'
auth_token = '92243c7755e8aeda70c62738f768181d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19737848845',
                     to='+19733687203'
                 )

print(message.sid)