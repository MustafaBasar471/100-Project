import requests
from datetime import datetime

GENDER = ""
WEIGHT_KG = ""
HEIGHT_CM = ""
AGE = ""

APP_ID = "your_id"
APP_KEY = "your_key"

exericse_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "your_endpoint"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exericse_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "your_username",
            "password",
        )
    )

    print(sheet_response.text)
