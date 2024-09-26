import json
import pandas as pd
from utils import *

get_weather_input()
with open('weather_data.txt','r') as file:
    parsed_data = json.load(file)

full_dict = parsed_data['location'] | parsed_data['current']
df = clean_df_inplace(full_dict)
print(df)
