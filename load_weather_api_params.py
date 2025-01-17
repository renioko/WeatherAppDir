# from load_weather_api_key import load_weather_api_key
import tomllib
import sys

def weather_api_params():
    try:
        # key = load_weather_api_key()
        with open(r'C:\Users\renio\Documents\Python\Projects\toml_weather.toml', 'rb') as stream:
            data = tomllib.load(stream)
    except FileNotFoundError:
        print('error, toml file not found')
        sys.exit(1)
    except tomllib.TOMLDecodeError:
        print('error. invalid TOML document')
        sys.exit(2)
    return data

if __name__ == '__main__':
    data = weather_api_params()
    print(data)

{'api_params': {
    'url': 'http://api.weatherapi.com/v1/current.json', 'headers': {
        'Content-Type': 'application/json'}, 
    'params': {
        'key': 'cb236724e4434ab1933222300242511', 
        'q': 'WS10'
        }}}
