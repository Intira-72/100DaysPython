import os
import smtplib
import random
import datetime as dt

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

def send_mail(quote, day_name):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=EMAIL_HOST_USER,
                        password=EMAIL_HOST_PASSWORD)

        connection.sendmail(from_addr=EMAIL_HOST_USER,
                            to_addrs="hijika111@gmail.com",
                            msg=f"Subject:{day_name} Motivation.\n\n{quote}")


def day_of_motivation():
    now = dt.datetime.now()

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    send_mail(quote, now.strftime("%A"))


if __name__ == "__main__":
    day_of_motivation()