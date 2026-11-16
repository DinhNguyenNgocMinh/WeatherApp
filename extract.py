import requests

base_url = r"https://api.open-meteo.com"
end_point = r"v1/forecast"

def get_weather(lat = 21.0245, lon = 105.8412, hourly = "temperature_2m", timezone = "Asia%2FSingapore"):

    url = f"{base_url}/{end_point}?latitude={lat}&longitude={lon}&hourly={hourly}&timezone={timezone}"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            print(response.status_code)
    except Exception as e:
        print(e)
        print(f"URL: {url}")

        