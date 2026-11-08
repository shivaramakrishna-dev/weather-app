# Weather App

A command-line weather app built in Python. Enter a city name and get the current temperature, weather condition and wind speed.

## Features
- Converts a city name to coordinates using the Open-Meteo Geocoding API
- Fetches live weather using the Open-Meteo Forecast API (no API key needed)
- Translates weather codes into readable text like "Partly cloudy"
- Handles unknown cities and network errors without crashing
- Keeps asking for cities until you type `quit`

## How to run
1. Make sure Python 3 is installed.
2. Install the dependency: `pip install requests`
3. Clone this repo: `git clone https://github.com/shivaramakrishna-dev/weather-app.git`
4. Run: `python weather.py`

## Concepts used
REST APIs, the `requests` library, JSON parsing, functions, dictionaries, `while` loops, and `try/except` error handling.