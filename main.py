import requests

api_key = "",

params = {
    # "lat": 32.820194,
    # "lon": -96.784688,
    "lat": 31.581490,
    "lon": -102.244918,
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
weather_data = response.json()

hourly_weather_id = [weather_data["hourly"][hr]["weather"][0]["id"] for hr in range(12)]

if any(code < 700 for code in hourly_weather_id):
    print("Bring an umbrella.")

