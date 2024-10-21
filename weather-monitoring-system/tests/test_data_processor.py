import unittest
from src.processor.data_processor import DataProcessor
from src.db.database import Database

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.db = Database(db_path='test_weather_data.db')
        self.processor = DataProcessor(db=self.db)

    def tearDown(self):
        self.db.close()

    def test_process_weather_data(self):
        raw_data = {
            'main': {'temp': 303.15, 'feels_like': 305.0},
            'weather': [{'main': 'Clear'}],
            'dt': 1603123200
        }
        processed = self.processor.process_weather_data(raw_data)
        self.assertEqual(processed['temperature'], 303.15)
        self.assertEqual(processed['feels_like'], 305.0)
        self.assertEqual(processed['weather_condition'], 'Clear')

    def test_update_daily_summary(self):
        data = {'temperature': 30.5, 'feels_like': 32.0, 'weather_condition': 'Clear', 'dt': 1603123200}
        self.processor.update_daily_summary('Delhi', data)
        # Check if daily summary would be saved correctly (this is end-of-day dependent)

if __name__ == '__main__':
    unittest.main()
