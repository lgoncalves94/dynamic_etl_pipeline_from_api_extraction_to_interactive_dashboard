import requests

class WeatherSense:
    """Class to fetch and manage weather data."""
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location
        self.condition = None  # This will hold the WeatherCondition instance

    def fetch_weather_data(self):
        """Fetch current weather data from the API."""
        params = {
            "key": self.api_key,
            "q": self.location
        }

        try:
            response = requests.get('http://api.weatherapi.com/v1/current.json', params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses

            # Parse the JSON response
            data = response.json()
            temperature = data['current']['temp_c']          # Current temperature in Celsius
            humidity = data['current']['humidity']            # Current humidity
            description = data['current']['condition']['text']  # Weather condition text

            # Create a WeatherCondition instance with fetched data
            self.condition = self.WeatherCondition(temperature, humidity, description)

            # Optionally, write the response to a file for logging purposes
            with open('weather_data.txt', 'w') as file:
                file.write(response.text)

        except Exception as e:
            self.handle_get_weather_error(e)

    def handle_get_weather_error(self, error):
        """Handle errors encountered during weather data fetching."""
        print("Error fetching weather data:", error)

    def get_weather_advice(self):
        """Get advice based on current weather conditions."""
        if self.condition:
            return self.condition.get_advice()
        else:
            return "Weather data not available."

    class WeatherCondition:
        """Class to represent the weather conditions."""

        def __init__(self, temperature, humidity, description):
            self.temperature = temperature  # Temperature in Celsius
            self.humidity = humidity          # Humidity percentage
            self.description = description    # Weather condition description

        def get_advice(self):
            """Provide weather-related advice based on temperature."""
            if self.temperature > 30:
                return "It's hot outside. Stay hydrated!"
            elif self.temperature < 0:
                return "It's freezing. Dress warmly!"
            else:
                return "Weather is moderate. Enjoy your day!"

# Example usage
def main():
    # Replace with your actual API key and desired location
    api_key = "your_api_key"  # Insert your actual API key here
    location = "Berlin"        # Change to your desired location

    weather_sense = WeatherSense(api_key, location)
    weather_sense.fetch_weather_data()  # Fetch weather data from API

    # Get recommendations based on the fetched condition
    print(weather_sense.get_weather_advice())  # Print weather advice

if __name__ == "__main__":
    main()
