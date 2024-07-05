#this is a python weather module that will retrive the weather for any city using the open weather api

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

#load the api key value from .env file 

load_dotenv()

# default value is mumbai 
def get_current_weather(city = "Mumbai"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()
    # it will return cod = 404 if the city is not found
    return weather_data

# if this file is called directly

if __name__ == "__main__":
    # welcome to the app
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")
    # check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Mumbai"
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)