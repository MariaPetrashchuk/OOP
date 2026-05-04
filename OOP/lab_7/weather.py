import requests

# Київ (координати)
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 50.45,
    "longitude": 30.52,
    "current_weather": True
}

r = requests.get(url, params=params)

data = r.json()

print("Температура:", data["current_weather"]["temperature"], "°C")
print("Вітер:", data["current_weather"]["windspeed"], "км/год")