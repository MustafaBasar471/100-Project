import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "AMAZON LINK HERE"
header = {
    # http://myhttpheader.com get "user-agent" and "Accept-Language"
    "User-Agent": "",
    "Accept-Language": ""
}

MY_GMAIL = "your_mail"
MY_PASSWORD = "your_password"
WALLET = 110

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-price-whole").get_text()
price_ = price.split(".")[0]
product_title = soup.find(id="productTitle").get_text().strip()

if int(price_) < WALLET:
    with smtplib.SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(MY_GMAIL, MY_PASSWORD)
        con.sendmail(
            from_addr=MY_GMAIL,
            to_addrs="***",
            msg=f"Subject:AMAZON PRICE ALERT AMAZON PRICE ALERT\n\n{product_title} is now {price_}$\n{URL}"
        )