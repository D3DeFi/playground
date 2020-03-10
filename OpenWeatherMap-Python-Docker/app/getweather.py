#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Retrieves weather data fromm openweathermap.org for a provided city.

This module doesn't accept any command line arguments, required input is provided via
ENV variables. Where OPENWEATHER_API_KEY holds an API key for the openweathermap.org
service and CITY_NAME specifies for which city should a weather be printed.

Attributes:
    API_KEY: Api key retrieved from the ENV variable named OPENWEATHER_API_KEY
    CITY: city name retrieved from the ENV variable named CITY_NAME

Example:
    $ export OPENWEATHER_API_KEY="xxxxxxxxxxxx"
    $ export CITY_NAME="Honolulu"
    $ python getweather.py
"""


from sys import exit
from os import getenv
from pyowm import OWM
from pyowm.exceptions.api_response_error import NotFoundError, UnauthorizedError


API_KEY = getenv('OPENWEATHER_API_KEY')
CITY = getenv('CITY_NAME')

def get_city_weather(city=CITY):
    """Function interacting with openweathermap.org API, retrieving weather for a specific city.

    The API response is parsed and result is printed to the stdout in format:
        source=openweathermap, city="X", description="X", temp=0, humidity=0

    Args:
        city: name of the city to retrieve weather for. Defaults to city provided in ENV variable.
    """
    if API_KEY is None:
        print('Missing API key for the openweathermap.org service.')
        exit(1)

    try:
        owm = OWM(API_key=API_KEY)
    except UnauthorizedError as e:
        print(e.msg)
        exit(1)

    if city is not None:
        try:
            cityres = owm.weather_at_place(city)
        except NotFoundError as e:
            print(e.msg)
            exit(1)

        weather = cityres.get_weather()
        result = {
            'city': cityres.get_location().get_name(),
            'description': weather.get_detailed_status(),
            'temp': weather.get_temperature().get('temp'),
            'humidity': weather.get_humidity()
        }

        print(('source=openweathermap, city="{city}", description="{description}", '
               'temp={temp}, humidity={humidity}').format(**result))
    else:
        print('Missing city name for which to provide weather for.')
        exit(1)



if __name__ == '__main__':
    get_city_weather()
