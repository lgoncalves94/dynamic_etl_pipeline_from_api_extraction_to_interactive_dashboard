import requests as r
from private import *
from error_handling import *

def get_weather_input():
    while True:
        choice = input('get weather_now yes or no?  > ')
        match choice:
            case 'yes':
                get_weather_now() # Writes current datapoint to file
                break
            case 'no':
                break
            case _ :
                print('Answer with -yes- or -no-')


def get_weather_now():
    params = {
        "key": API_KEY_WEATHER,
        "q":'Berlin'
        }

    try:
        response = r.get('http://api.weatherapi.com/v1/current.json',params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        with open('weather_data.txt','w') as file:
            file.write(response.text)

    except Exception as e:
        handle_get_weather_error(e)


