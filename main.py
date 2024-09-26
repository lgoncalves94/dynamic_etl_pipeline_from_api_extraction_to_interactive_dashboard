import json
from utils import *

get_weather_input()

with open('weather_data.txt','r') as file:
    parsed_data = json.load(file)

current_data_point = parsed_data['location'] | parsed_data['current']

print(current_data_point)