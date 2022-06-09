import smtplib
import datetime as dt
import random

MY_GMAIL = "example@gmail.com"
MY_PASSWORD = "****************"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("./Project 31 (Motivation Mail)/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_c = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_GMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_GMAIL, 
        to_addrs=MY_GMAIL,
        msg=f"Subject:Motivation Mail Title\n\n{random_c}"
        )