import requests


def city_coordinate(city_name):
    if len(city_name) > 2:
        resp = requests.get(
            url="https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city_name,
                "count": 1,
            }
        )
        result = resp.json()["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        return latitude, longitude
    else:
        print("Incorrect input")
        return None


def request_weather(coordinate):
    latitude = coordinate[0]
    longitude = coordinate[1]
    res = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "apparent_temperature",
                       "surface_pressure"],
        }
    )
    temp_lst = res.json()["hourly"]["temperature_2m"]
    apparent_temp_lst = res.json()["hourly"]["apparent_temperature"]
    pressure = res.json()["hourly"]["surface_pressure"]
    avr_temp = round(sum(temp_lst)/len(temp_lst), 1)
    avr_app_temp = round(sum(apparent_temp_lst)/len(apparent_temp_lst), 1)
    avr_pressure = round(sum(pressure)/len(pressure), 1)
    return avr_temp, avr_app_temp, avr_pressure


def weather_app(city_name):
    coordinate = city_coordinate(city_name)
    if coordinate is None:
        print("Invalid data")
    else:
        res = request_weather(coordinate)
        avr_temp = res[0]
        avr_app_temp = res[1]
        avr_pressure = res[2]
        print(f" City: {city_name},\n Temperature: {avr_temp},\n "
              f"Feels like: {avr_app_temp},\n Pressure: {avr_pressure}hPa.")


if __name__ == "__main__":
    city_name = "Detroit"
    weather_app(city_name)
