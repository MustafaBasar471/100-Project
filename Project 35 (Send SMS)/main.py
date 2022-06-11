import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key"

weather_params = {
    "lat": 39.933365,
    "lon": 32.859741,
    "appid": api_key,
    "exclude": "current,minutely,daily"
    }


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

rain = False
for i in weather_slice:
    weather_id = i["weather"][0]["id"]
    if int(weather_id) < 700:
        rain = True

if rain:
    account_sid = 'your_sid' 
    auth_token = 'your_token' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+************',  
                                body='Bugün hava yağmurlu gözüküyor şemsiyeyi unutmuyoruz',      
                                to='whatsapp:+**********' 
                            ) 
    print(message.status)

