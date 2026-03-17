import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Heavy drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight showers", 81: "Moderate showers", 82: "Heavy showers",
    95: "Thunderstorm",
}


def get_coordinates(city):
    data = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
    results = data.get("results")
    if not results:
        print(f"City '{city}' not found.")
        return None

    location = results[0]
    return {
        "name": location["name"],
        "country": location["country"],
        "lat": location["latitude"],
        "lon": location["longitude"],
    }


def get_weather(city):
    location = get_coordinates(city)
    if not location:
        return

    url = f"https://api.open-meteo.com/v1/forecast?latitude={location['lat']}&longitude={location['lon']}&current=temperature_2m,wind_speed_10m,weather_code"
    weather = requests.get(url).json()

    temp_c = weather["current"]["temperature_2m"]
    wind = weather["current"]["wind_speed_10m"]
    code = weather["current"]["weather_code"]
    temp_f = round((temp_c * 9 / 5) + 32, 1)
    desc = WEATHER_CODES.get(code, "Unknown")

    print(f"\nCity        : {location['name']}, {location['country']}")
    print(f"Description : {desc}")
    print(f"Temperature : {temp_c}°C / {temp_f}°F")
    print(f"Wind Speed  : {wind} km/h")


get_weather("London")
