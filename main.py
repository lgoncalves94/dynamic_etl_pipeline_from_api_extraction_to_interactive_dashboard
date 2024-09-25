import json
from utils import *

while True:
    choice = input('get weather_now yes or no?')
    match choice:
        case 'yes':
            get_weather_now()
            break
        case 'no':
            break
        case _ :
            print('Answer with -yes- or -no-')

with open('weather_data.txt','r') as file:

    parsed_data = json.load(file)

current_data_point = parsed_data['location'] | parsed_data['current']