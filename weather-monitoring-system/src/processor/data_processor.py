from datetime import datetime
from collections import defaultdict

class DataProcessor:
    def __init__(self, db):
        """Initialize the processor with a reference to the Database instance."""
        self.db = db
        self.daily_data = defaultdict(lambda: {"temps": [], "conditions": []})

    def process_weather_data(self, data):
        """Process raw weather data from OpenWeatherMap API."""
        return {
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'weather_condition': data['weather'][0]['main'],
            'dt': data['dt']  # Unix timestamp
        }

    def update_daily_summary(self, city, data):
        """Update daily summary with new data and roll up the results."""
        date = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d')

        # Track the temperature and weather condition for the day
        self.daily_data[city]['temps'].append(data['temperature'])
        self.daily_data[city]['conditions'].append(data['weather_condition'])

        # At the end of the day, compute the rollup and store it
        if self._is_end_of_day():
            avg_temp = sum(self.daily_data[city]['temps']) / len(self.daily_data[city]['temps'])
            max_temp = max(self.daily_data[city]['temps'])
            min_temp = min(self.daily_data[city]['temps'])
            dominant_condition = self._find_dominant_condition(self.daily_data[city]['conditions'])

            # Save the daily summary using the database instance
            self.db.save_daily_summary(city, date, avg_temp, max_temp, min_temp, dominant_condition)

            # Clear the day's data
            self.daily_data[city] = {"temps": [], "conditions": []}

    def _is_end_of_day(self):
        """Check if the current time is the end of the day (e.g., 23:59)."""
        current_time = datetime.utcnow().strftime('%H:%M')
        return current_time == '23:59'

    def _find_dominant_condition(self, conditions):
        """Find the dominant weather condition based on frequency."""
        return max(set(conditions), key=conditions.count)
