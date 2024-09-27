from weather_sense import WeatherSense
from typing_effect import typing_effect

while True:
    typing_effect(">yes< to read test weather data from file")
    typing_effect('>no< to fetch latest weather data from API')
    choice = input('\n>> ').lower()
    match choice:
        case 'yes':
             WeatherSense.main('yes') # Read from file
             break
        case 'no' :
            WeatherSense.main('no') # Fetch latest data
            break
        case _ :
            typing_effect('Answer with **yes** or **no** please\n')


