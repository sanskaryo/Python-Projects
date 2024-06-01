import requests
from twilio.rest import Client


owm = "https://api.openweathermap.org/data/2.5/forecast"

api = "028abf845a5e1b62a538c9bdd5f9f182"


weather_params = {
    "lat" : 27.492413,
    "lon": 77.673676,
    "appid": api,
    "cnt" : 4,
    
}

response = requests.get(owm, params=weather_params)
print(response.status_code)
response.raise_for_status()

weather_data=response.json()
print(weather_data["list"][0]["weather"][0]["id"])


for hour_data in weather_data["list"]:
    condition = hour_data["weather"]
    if int(condition) < 700:
        print("bring umbrella")
        
        # JJT3WF6D2Z58XW82PVRJB8RT