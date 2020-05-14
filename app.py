
from twilio.rest import Client
import requests
account_sid = 'xxxxxxxxxxx'
auth_token = 'xxxxxxxxxxx'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)
#formulate the message that will be sent
message = client.messages.create(
    to="+1xxxxxxxxxx",
    from_="+1xxxxxxxxxx",
    body=Message)
print(message.sid)
