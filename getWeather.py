# openweather.py
import requests
from config import Config

class OpenWeatherMap:
    @staticmethod
    def get_weather(city):
        api_key = Config.OPENWEATHER_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to retrieve data from OpenWeatherMap. {str(e)}"}
        

    
