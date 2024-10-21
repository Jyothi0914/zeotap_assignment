import sqlite3

class Database:
    def __init__(self, db_path='weather_data.db'):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            # Real-time weather data
            self.connection.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                                        city TEXT,
                                        timestamp TEXT,
                                        temperature REAL,
                                        feels_like REAL,
                                        weather_condition TEXT)''')
            # Daily weather summary
            self.connection.execute('''CREATE TABLE IF NOT EXISTS daily_summary (
                                        city TEXT,
                                        date TEXT,
                                        avg_temp REAL,
                                        max_temp REAL,
                                        min_temp REAL,
                                        dominant_condition TEXT)''')

    def save_real_time_data(self, city, data):
        with self.connection:
            self.connection.execute('INSERT INTO weather_data VALUES (?, ?, ?, ?, ?)', 
                                    (city, data['timestamp'], data['temperature'], 
                                     data['feels_like'], data['weather_condition']))

    def save_daily_summary(self, city, date, avg_temp, max_temp, min_temp, dominant_condition):
        with self.connection:
            self.connection.execute('INSERT INTO daily_summary VALUES (?, ?, ?, ?, ?, ?)', 
                                    (city, date, avg_temp, max_temp, min_temp, dominant_condition))

    def fetch_data(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM weather_data')
        return cursor.fetchall()

    def close(self):
        self.connection.close()
