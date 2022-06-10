##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import pandas
import datetime as dt

MY_GMAIL = "example@gmail.com"
MY_PASSWORD = "****************"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./Project 32 (Birthday Wisher)/birthdays.csv")
brth_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in brth_dict:
    brth_person = brth_dict[today_tuple]
    file = f"./Project 32 (Birthday Wisher)/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file) as file_data:
        content = file_data.read()
        content = content.replace("[NAME]", brth_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(MY_GMAIL, MY_PASSWORD)
        con.sendmail(
            from_addr=MY_GMAIL,
            to_addrs=brth_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
            )