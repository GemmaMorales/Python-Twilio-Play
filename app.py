
from twilio.rest import Client
import requests
account_sid = 'AC6607710a8da5a23b7fa63232c27efd86'
auth_token = 'a20d91042265b4e138517e278362614c'
client = Client(account_sid, auth_token)
r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()
number_iss = people['number']
Message = 'Hi Fun fact,Number of people in space right now is '+str(number_iss)
#formulate the message that will be sent
message = client.messages.create(
    to="+13124201017",
    from_="+12058755998",
    body=Message)
print(message.sid)
