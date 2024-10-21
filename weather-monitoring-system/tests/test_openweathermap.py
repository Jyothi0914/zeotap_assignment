import unittest
from unittest.mock import patch
from api.openweathermap import OpenWeatherMapAPI

class TestOpenWeatherMapAPI(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_weather_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 298.15, "feels_like": 300.15},
            "weather": [{"main": "Clear"}],
            "dt": 1625484367
        }
        api = OpenWeatherMapAPI(api_key="fake_key", city="Delhi")
        response = api.fetch_weather_data()
        self.assertEqual(response["main"]["temp"], 298.15)

    @patch('requests.get')
    def test_fetch_weather_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        api = OpenWeatherMapAPI(api_key="fake_key", city="Delhi")
        with self.assertRaises(Exception):
            api.fetch_weather_data()

if __name__ == '__main__':
    unittest.main()
