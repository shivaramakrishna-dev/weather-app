import requests

weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    97: "Heavy thunderstorm",
    99: "Thunderstorm with heavy hail",
}

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params, timeout=5)
    data = response.json()
    if "results" not in data:
        return None
    result = data["results"][0]
    return result["latitude"], result["longitude"]

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params, timeout=5)
    data = response.json()
    return data["current_weather"]

while True:
    city = input("Enter city (or 'quit'): ").strip().title()
    if city == "Quit":
        break

    if city == "":
        print("Please enter a city name.")
        continue 

    try:
        coords = get_coordinates(city)
        if coords is None:
            print("City not found")
        else:
            lat, lon = coords
            weather = get_weather(lat, lon)
            desc = weather_codes.get(weather["weathercode"], "Unknown")
            print(f"{city}: {weather['temperature']}°C, {desc}, wind {weather['windspeed']} km/h")
    except requests.exceptions.RequestException:
        print("Network problem. Check your internet and try again.")   