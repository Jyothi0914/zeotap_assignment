import unittest
from unittest.mock import patch
from main import main  # Import the main script

class TestFullWorkflow(unittest.TestCase):
    @patch('api.openweathermap.OpenWeatherMapAPI.fetch_weather_data')
    @patch('alert.alert_system.AlertSystem.check_alert')
    @patch('db.database.Database.save_data')
    def test_full_workflow(self, mock_save_data, mock_check_alert, mock_fetch_weather_data):
        # Mock the API response
        mock_fetch_weather_data.return_value = {
            "main": {"temp": 298.15, "feels_like": 300.15},
            "weather": [{"main": "Clear"}],
            "dt": 1625484367
        }

        # Run the main function to test the workflow
        main()

        # Check if the data was fetched, processed, and alerts checked
        mock_fetch_weather_data.assert_called_once()
        mock_check_alert.assert_called_once()
        mock_save_data.assert_called_once()

if __name__ == '__main__':
    unittest.main()
