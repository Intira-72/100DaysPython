import os
import requests
from twilio.rest import Client


API_KEY = os.environ.get('OWN_API_KEY')
API_URL = "https://api.openweathermap.org/data/2.5/weather"

account_sid = os.environ.get('OWN_ACC_SID')
auth_token = os.environ.get('OWN_AUTH_TOKEN')

parameters = {
    "lat": 13.547140,
    "lon": 100.274338,
    "appid": API_KEY
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()

condition_data = data['weather'][0]

client = Client(account_sid, auth_token)
message = client.messages.create(body=f"The Condition is {condition_data['main']} - {condition_data['description']}",
                                from_='+16403446119',
                                to='+66984094135')
print(message.status)