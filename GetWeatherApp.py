
from load_weather_api_key import load_weather_api_key
from load_weather_api_params import weather_api_params
import flask
import json
import requests
import sys
import tomllib

from requests import status_codes
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
    print(f'Today the weather in {place['name']}, {place['region']}, {place['country']}) at the time: {place['localtime']} is as follows:')
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

{"location":{"name":"Wednesbury","region":"West Midlands","country":"UK","lat":52.560001373291,"lon":-2.02099990844727,"tz_id":"Europe/London","localtime_epoch":1732645892,"localtime":"2024-11-26 18:31"},
 "current":{"last_updated":"2024-11-26 18:30","temp_c":4.3,"is_day":0,"condition":{"text":"Clear","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":2.9,"wind_kph":4.7,"wind_degree":181,"wind_dir":"S","pressure_mb":1017.0,"pressure_in":30.03,"humidity":93,"cloud":0,"feelslike_c":3.4,"windchill_c":3.9,"windchill_f":39.1,"gust_mph":5.4,"gust_kph":8.7}}


