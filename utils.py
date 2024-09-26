import requests as r
from private import *
from error_handling import *
import pandas as pd

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

def clean_df_inplace(datapoint:dict) -> pd.DataFrame:
    pd.set_option('display.max_columns', None)  # None means no limit
    pd.set_option('display.expand_frame_repr', False) # prevent line break
    df = pd.DataFrame([datapoint])
    df.drop(columns=['localtime_epoch', 'tz_id','lat', 'lon','heatindex_c'],inplace=True)
    df.rename(columns={'name':'city'}, inplace=True)
    df['localdate'] = df.localtime.iloc[0].split(' ')[0]
    df['localtime'] = df.localtime.iloc[0].split(' ')[1]
    order = ['city', 'region', 'country', 'localtime','localdate', 'temp_c', 'feelslike_c', 'dewpoint_c', 'humidity', 'cloud', 'precip_mm', 'wind_kph', 'gust_kph', 'windchill_c', 'uv']
    df = df[order]
    return df


def eval_weather(df:pd.DataFrame):


