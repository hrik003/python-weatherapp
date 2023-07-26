from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()

def get_condition(city="Kolkata"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_report = requests.get(request_url).json()
    return weather_report

if __name__ == "__main__":
    print("\n*** Get Current Weather Information ***\n")

    city = input('\n PLease input a city name: ')

    # Check if input is empty or only having spaces
    if not bool(city.strip()):
        city = "Kolkata"

    weather_data = get_condition(city)
    print("\n")
    pprint(weather_data)