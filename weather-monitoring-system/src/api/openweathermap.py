import requests
import json

class OpenWeatherMapAPI:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def fetch_weather_data(self):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")
