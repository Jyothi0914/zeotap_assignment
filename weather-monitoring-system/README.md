Real-Time Weather Monitoring System

Project Overview
This project implements a real-time weather monitoring system using data from the OpenWeatherMap API. The system continuously retrieves weather data for specified metro cities in India and provides summarized insights such as daily weather summaries, alerts based on configurable thresholds, and historical trends visualization. The system includes rollups and aggregates, such as average, minimum, and maximum temperatures, and dominant weather conditions for each day.

Features
-> Real-Time Data Retrieval: Continuously fetch weather data for multiple metro cities in India.
-> Temperature Conversion: Convert weather data from Kelvin to Celsius or Fahrenheit based on user preference.
-> Daily Summaries: Aggregate daily weather data to calculate average, minimum, maximum temperatures, and dominant weather conditions.
-> Alerting System: Trigger alerts when temperature or weather conditions exceed predefined thresholds.
-> Visualization: Display daily weather summaries and trends using graphical plots.
Modular Design: Components for data fetching, processing, alerting, and visualization are structured in a modular fashion.

Prerequisites
Before running the project, ensure you have the following installed:
1. Python 3.9 or higher: Download and install from Python's official website.
2. SQLite: For local database storage (used in this project for weather data summaries).
3. Git: To upload the project to GitHub (if needed).

Python Dependencies
-> requests: For making API calls to OpenWeatherMap.
-> matplotlib: For generating weather trend visualizations.
-> sqlite3: For storing daily weather summaries.
-> unittest: For running the test suite.
These dependencies are listed in the requirements.txt file.

Project Setup
1. Clone the repository (after uploading to GitHub)
	git clone <your-repository-url>
	cd weather-monitoring-system
2. Create and activate a Python virtual environment
	# On Windows
	python -m venv venv
	venv\Scripts\activate

	# On Mac/Linux
	python3 -m venv venv
	source venv/bin/activate
3. Install dependencies
	pip install -r requirements.txt
4. Configure OpenWeatherMap API Key
Sign up for a free OpenWeatherMap API key at OpenWeatherMap. Then, create a .env file in the root directory and add your API key:
	API_KEY=your_openweathermap_api_key
5. Configure Thresholds and Interval (Optional)
You can adjust the weather alert thresholds and data fetching intervals in the config.py file or through environment variables.
6. Running the Application
To start the application and begin fetching real-time weather data:
	python src/main.py
The system will fetch data at regular intervals (e.g., every 5 minutes), process it, and store daily summaries in the SQLite database.
7. Visualizing Data
To visualize the daily weather trends:
	python src/visualization/visualize.py
Graphs will be generated displaying trends like average temperature over time.

API Endpoints (Optional for Extension)
If extended into a web application, the following API endpoints can be implemented:

1. Get Weather Data
-> URL: /weather
-> Method: GET
-> Description: Retrieves the latest weather data for a given city.

2. Set Alert Thresholds
-> URL: /set_alert
-> Method: POST
-> Description: Allows users to set temperature thresholds for alerts.

Testing
Unit Tests
The project includes unit tests that validate the core functionality:
-> API Data Retrieval: Tests the connection to the OpenWeatherMap API and ensures correct data parsing.
-> Data Processing: Tests temperature conversion, daily rollups, and weather condition aggregation.
-> Alerting System: Tests the alert triggering mechanism based on temperature thresholds.
-> Database Operations: Tests the correct insertion and retrieval of data from SQLite.
To run the test suite:
	python -m unittest discover tests/

Manual Testing
You can manually test the system by observing real-time weather data logs and checking the alerting system for any threshold breaches. The visualization module also provides a way to manually inspect historical weather trends.

Logging and Error Handling
The project includes logging to track the weather monitoring process and capture any errors that may occur during API requests or data processing. Logs are stored in weather_monitoring.log, and any errors are gracefully handled with appropriate error messages.

Conclusion
This project provides a comprehensive real-time weather monitoring solution that supports rollups and aggregates for daily weather summaries, configurable alert thresholds, and data visualization. The modular design allows for easy extension and maintenance.