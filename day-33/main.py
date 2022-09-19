import requests
from datetime import datetime

MY_LAT = 13.756331
MY_LNG = 100.501762

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response_api = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_api.raise_for_status()

data = response_api.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)