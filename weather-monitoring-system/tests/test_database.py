import unittest
import os
from src.db.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_weather_data.db'
        self.db = Database(db_path=self.db_path)

    def tearDown(self):
        self.db.close()
        os.remove(self.db_path)

    def test_save_and_fetch_real_time_data(self):
        data = {
            'timestamp': '2024-10-19 10:00:00',
            'temperature': 30.5,
            'feels_like': 32.0,
            'weather_condition': 'Clear'
        }
        self.db.save_real_time_data('Delhi', data)
        result = self.db.fetch_data()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], '2024-10-19 10:00:00')

    def test_save_daily_summary(self):
        self.db.save_daily_summary('Delhi', '2024-10-19', 30.0, 35.0, 25.0, 'Clear')
        result = self.db.fetch_data()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'Delhi')

if __name__ == '__main__':
    unittest.main()
