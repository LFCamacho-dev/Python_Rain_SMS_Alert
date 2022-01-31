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
hourly_weather = weather_data["hourly"]
# print(hourly_weather[0]["weather"][0]["id"])
print(type(hourly_weather))
# for hr in hourly_weather[:12]:
#     print(hourly_weather[hr]["weather"][0]["id"])

