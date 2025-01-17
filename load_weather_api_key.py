import os
from dotenv import load_dotenv
import sys


def load_weather_api_key():
    load_dotenv()
    try:
        api_key = os.getenv('WEATHER_API_KEY')
    except ValueError:
        print('problem with Weather API key')
        sys.exit(1)
    return api_key
