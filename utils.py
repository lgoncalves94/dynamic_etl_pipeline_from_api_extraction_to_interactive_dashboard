import requests as r
from private import *

def get_weather_now():
    params = {
        "key": API_KEY_WEATHER,
        "q":'Berlin'
        }
    response = r.get('http://api.weatherapi.com/v1/current.json',params=params)
    if response.status_code == 200:
        data = response.text

    with open('weather_data.txt','w') as file:
        file.write(data)