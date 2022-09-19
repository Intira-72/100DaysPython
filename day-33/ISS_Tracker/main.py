import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 13.756331 # Your latitude
MY_LONG = 100.501762 # Your longitude

MY_EMAIL = "enicma.shop2022@gmail.com"
MY_PASS = "vnvfhimxqntdmpwc"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise >= time_now or sunset <= time_now:
        return True


if __name__ == "__main__":
    while True:
        time.sleep(60)
        if is_iss_overhead() and is_night():
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=MY_EMAIL,
                                password=MY_PASS)

                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="hijika111@gmail.com",
                                    msg=f"Look Up 👆\n\nThe ISS is above you in the sky.")