import requests
import json
print("test")
url = "https://api.open-meteo.com/v1/forecast"
params = {
  "latitude": 40.725933,
  "longitude": -73.514290,
  "current": "temperature_2m",
  "timezone":"auto",
  "temperarure_unit":"fahrenheit"
}
payload = {}
headers = {}
respond = requests.get(url, params= params)
if respond.status_code != 200:
  print(f"Error {respond.status_code}")
else:
  data = respond.json()
  temperture = data.get("current").get("temperature_2m")
  print(f"The Temperature is {temperture}")

  
