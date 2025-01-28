
from load_weather_api_key import load_weather_api_key
from load_weather_api_params import weather_api_params
import json
import requests
import sys

from requests import HTTPError

'''
This program asks user for a location and presents weather.
'''

def get_request(location) -> json:
    api_key = load_weather_api_key()
    data = weather_api_params()

# zastepuje klucz z toml kluczem api_key oraz lokalizacja
    data['api_params']['params']['key'] = api_key
    data['api_params']['params']['q'] = location

    try:
        r = requests.get(data['api_params']['url'], headers=data['api_params']['headers'], params=data['api_params']['params'])
        r.raise_for_status
        if r.status_code == 200:
            print(f'Succes! Status code: {r.status_code}')
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
        sys.exit(1)
    except Exception as e:
        print(f'Other error occured: {e}')
        sys.exit(1)
    try:
        weather_json = r.json()
    except UnboundLocalError:
        print('error, cannot acces variable, where it is not associated with data')
        sys.exit(2)
    return weather_json

def print_raport(weather_json):
    place = weather_json['location']
    weather = weather_json['current']
    print(f'Today the weather in {place['name']}, {place['region']}, {place['country']} at the time: {place['localtime']} is as follows:')
    print(f'temperature: {weather['temp_c']}C,')
    print(f'feels-like temp: {weather['feelslike_c']}C')
    print(f'wind: {weather['wind_kph']}kph, wind direction: {weather['wind_dir']},')
    print(f'pressure: {weather['pressure_mb']}mb,')
    print(f'humidity: {weather['humidity']}')

def main():
    location = input('enter location: ')
    weather_json = get_request(location)
    print_raport(weather_json)


if __name__ == '__main__':
    main()




