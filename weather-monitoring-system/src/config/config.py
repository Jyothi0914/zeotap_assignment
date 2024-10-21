class Config:
    API_KEY = 'your_openweathermap_api_key'
    DATABASE_PATH = 'weather_data.db'
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    FETCH_INTERVAL = 300  # 5 minutes in seconds
    ALERT_THRESHOLD = {
        'temp': 35.0  # Temperature threshold in Celsius
    }
