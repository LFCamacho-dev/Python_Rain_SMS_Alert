import requests
import os
from twilio.rest import Client

api_key = os.environ.get("APIKEY")

account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    "lat": 30.281490,  # test rainy location
    "lon": -97.144918,  # test rainy location
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
weather_data = response.json()

hourly_weather_id = [weather_data["hourly"][hr]["weather"][0]["id"] for hr in range(12)]

if any(code < 700 for code in hourly_weather_id):
    print("Bring an umbrella.")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.environ.get("TO_TEL"),
        from_=os.environ.get("FROM_TEL"),
        body="It's gonna rain! grab umbrella :)",
    )

    print(f"the ID is: {message.sid}, and the status is: {message.status}")

