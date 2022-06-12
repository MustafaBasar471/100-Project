import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "your_stock_api"
NEW_API_KEY = "your_news_api"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]

diff = float(yesterday_closing_data) - float(day_before_yesterday_closing_data)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_precent = round((diff / float(yesterday_closing_data)) * 100)

if abs(diff_precent) > 2:
    news_params = {
        "apiKey": NEW_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    article = new_response.json()["articles"]
    two_article = article[:2]
    
    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_precent}%\n\nHeadline: {article['title']}.\n\nBrief: {article['description']}.\n\nUrl: {article['url']}" for article in two_article]
    account_sid = 'your_sid' 
    auth_token = 'your_token' 
    client = Client(account_sid, auth_token) 
    
    for i in formatted_article:
        message = client.messages.create( 
                                    from_='whatsapp:+**********',  
                                    body=i,      
                                    to='whatsapp:+***********' 
                                ) 
        print(message.status)


