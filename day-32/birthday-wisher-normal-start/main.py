##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random as rn
import smtplib


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for index, data_row in data.iterrows()}

EMAIL_HOST_USER = "enicma.shop2022@gmail.com"
EMAIL_HOST_PASSWORD = "vnvfhimxqntdmpwc"

def send_mail(quote, mail):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=EMAIL_HOST_USER,
                        password=EMAIL_HOST_PASSWORD)

        connection.sendmail(from_addr=EMAIL_HOST_USER,
                            to_addrs=mail,
                            msg=f"Subject:Happy Birthday!\n\n{quote}")

 
if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{rn.randrange(1, 4)}.txt"
    birthday_person = birthdays_dict[today_tuple]

    with open(file_path) as letter:
        contents = letter.read()
        send_mail(contents.replace("[NAME]", birthday_person['name']), birthday_person['email'])
