import time
from src.api.openweathermap import OpenWeatherMapAPI
from src.processor.data_processor import DataProcessor
from src.alert.alert_system import AlertSystem
from src.db.database import Database
from src.config.config import Config

def main():
    # Initialize the OpenWeatherMapAPI, DataProcessor, AlertSystem, and Database
    weather_api = OpenWeatherMapAPI(Config.API_KEY)
    db = Database(Config.DATABASE_PATH)
    processor = DataProcessor(db)  # Pass the db instance here
    alert_system = AlertSystem()

    try:
        while True:
            # Fetch weather data for each city
            for city in Config.CITIES:
                try:
                    data = weather_api.fetch_weather(city)
                    processed_data = processor.process_weather_data(data)
                    
                    # Save real-time weather data to the database
                    db.save_real_time_data(city, processed_data)
                    
                    # Rollup daily summary (handled separately, possibly scheduled every midnight)
                    processor.update_daily_summary(city, processed_data)
                    
                    # Check for alerts based on the data
                    alert_system.check_thresholds(processed_data)

                except Exception as e:
                    print(f"Error fetching or processing data for {city}: {e}")

            # Sleep for the configured interval before fetching new data
            time.sleep(Config.FETCH_INTERVAL)

    except KeyboardInterrupt:
        print("Terminating the system...")
    finally:
        # Close the database connection
        db.close()

if __name__ == '__main__':
    main()
