import requests as r
from private import *
import json


class WeatherSense:
    """Class to fetch and manage weather data."""
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location
        self.condition = None  # This will hold the WeatherCondition instance

    def fetch_weather_data(self,test='no'):
        """Fetch current weather data from the API."""
        params = {
            "key": self.api_key,
            "q": self.location
        }
        try:
            if test == 'no':
                response = r.get('http://api.weatherapi.com/v1/current.json', params=params)
                data = response.json()
            else:
                with open('weather_data.json','r') as file:
                    data = json.load(file)
            # Extrahieren der Werte für WeatherCondition
            temperature = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]
            precipitation = data["current"]["precip_mm"]
            feels_like = data["current"]["feelslike_c"]
            wind_chill = data["current"]["windchill_c"]
            heat_index = data["current"]["heatindex_c"]
            dew_point = data["current"]["dewpoint_c"]
            uv_index = data["current"]["uv"]
            cloud_cover = data["current"]["cloud"]
            gust_speed = data["current"]["gust_kph"]
            city = data['location']['name']
            region = data['location']['region']
            country = data['location']['country']
            time = data['location']['localtime']
            # Create a WeatherCondition instance with fetched data
            self.condition = self.WeatherCondition(
            city,
            region,
            country,
            time,
            temperature,
            humidity,
            wind_speed,
            precipitation,
            feels_like,
            wind_chill,
            heat_index,
            dew_point,
            uv_index,
            cloud_cover,
            gust_speed )

        except Exception as e:
            self.handle_get_weather_error(e)

    def handle_get_weather_error(e):

        if isinstance(e, r.exceptions.ConnectionError):
            print("Error: Failed to connect to the weather API. Check your network connection.")
        elif isinstance(e, r.exceptions.Timeout):
            print("Error: The request to the weather API timed out.")
        elif isinstance(e, r.exceptions.HTTPError):
            print(f"HTTP error occurred: {e}")
        elif isinstance(e, ValueError):
            print("Error: Received an invalid response (possibly not JSON).")
        else:
            print(f"An unexpected error occurred: {e}")

    def display_weather(self):
        if self.condition:
            print(f"City: {self.condition.city}")
            print(f"Region: {self.condition.region}")
            print(f"Country: {self.condition.country}")
            print(f"Local Time: {self.condition.localtime}")
            print(f"Temperature: {self.condition.temperature} °C")
            print(f"Humidity: {self.condition.humidity}%")
            print(f"Wind Speed: {self.condition.wind_speed} km/h")
            print(f"Precipitation: {self.condition.precipitation} mm")
            print(f"Feels Like: {self.condition.feels_like} °C")
            print(f"Wind Chill: {self.condition.wind_chill} °C")
            print(f"Heat Index: {self.condition.heat_index} °C")
            print(f"Dew Point: {self.condition.dew_point} °C")
            print(f"UV Index: {self.condition.uv_index}")
            print(f"Cloud Cover: {self.condition.cloud_cover}%")
            print(f"Gust Speed: {self.condition.gust_speed} km/h")
        else:
            print("No weather data available.")

    class WeatherCondition:
        """Class to represent the weather conditions."""
        def __init__(self, city, region, country, localtime, temperature, humidity, wind_speed, precipitation,
             feels_like, wind_chill, heat_index, dew_point, uv_index, cloud_cover, gust_speed):
            self.city = city                            # Name of the city
            self.region = region                        # Name of the region
            self.country = country                      # Name of the country
            self.localtime = localtime                  # Local time as a string
            self.temperature = temperature              # Current temperature in Celsius
            self.humidity = humidity                    # Current humidity as a percentage
            self.wind_speed = wind_speed                # Current wind speed in km/h
            self.precipitation = precipitation          # Current precipitation in mm
            self.feels_like = feels_like                # Feels-like temperature in Celsius
            self.wind_chill = wind_chill                # Wind chill temperature in Celsius
            self.heat_index = heat_index                # Heat index in Celsius
            self.dew_point = dew_point                  # Dew point in Celsius
            self.uv_index = uv_index                    # UV index
            self.cloud_cover = cloud_cover              # Cloud cover percentage
            self.gust_speed = gust_speed                # Gust speed in km/h




# Example usage
    def main(test='no'):
        # Replace with your actual API key and desired location
        api_key = API_KEY_WEATHER  # Insert your actual API key here
        location = "Berlin"        # Change to your desired location
        weather_sense = WeatherSense(api_key, location)
        weather_sense.fetch_weather_data(test=test)  # Fetch weather data from API
        weather_sense.display_weather()
