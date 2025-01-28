# Weather-app
Reports weather forecast for a given location.
This Python program retrieves and displays weather information for a user-specified location. It uses the `requests` library to make HTTP requests to a weather API.

## Table of Contents

- [Weather-app](#weather-app)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Error Handling](#error-handling)
  - [Requirements](#requirements)
  - [License](#license)
  - [Contact](#contact)

## Description

The Weather Report Program simplifies the process of checking the weather.  It prompts the user for a location, fetches the corresponding weather data from a weather API, and presents a formatted weather report.

## Features

*   Retrieves current weather conditions for a given location.
*   Displays temperature (Celsius), "feels-like" temperature, wind speed and direction, pressure, and humidity.
*   Handles HTTP errors and other potential exceptions during the API request.
*   Uses configuration files (`load_weather_api_key.py` and `load_weather_api_params.py`) for API key and parameters, promoting better security practices by keeping sensitive information out of the main script.

## Installation

1.  Clone the repository (or download the files if not using Git):

    ```bash
    git clone https://github.com/renioko/WeatherAppDir/tree/main
    ```

2.  Navigate to the project directory:

    ```bash
    cd WeatherAppDir  # Or the name of your project directory
    ```

3.  Install the required library:

    ```bash
    pip install requests
    ```

## Usage

1.  Run the script:

    ```bash
    python GetWeatherApp.py  

2.  The program will prompt you to enter a location:

    ```
    enter location: London 
    ```

3.  The program will then display the weather report:

    ```
    Today the weather in London, Greater London, United Kingdom at the time: 2024-10-27 14:30 is as follows:
    temperature: 12C,
    feels-like temp: 10C
    wind: 20kph, wind direction: SW,
    pressure: 1012mb,
    humidity: 75
    ```

## Configuration

The program uses two configuration files:

*   `load_weather_api_key.py`: This file should contain a function `load_weather_api_key()` that returns your weather API key as a string.  **Do not hardcode your API key directly into the main script.**  A recommended approach is to store your API key in a `.env` file and use the `python-dotenv` library to load it.  Example:

    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()

    def load_weather_api_key():
        return os.getenv("WEATHER_API_KEY")
    ```

    Then install the needed library:

    ```bash
    pip install python-dotenv
    ```

*   `load_weather_api_params.py`: This file should contain a function `weather_api_params()` that returns a dictionary containing the URL, headers, and parameters for your weather API request. This allows you to easily change the API endpoint or parameters without modifying the main script. Example:

    ```python
    def weather_api_params():
        return {
            'api_params': {
                'url': 'http://api.weatherapi.com/v1/current.json',  
                'headers': {
                    'Content-Type': 'application/json'
                },
                'params': {
                    'key': '',  # API key will be inserted here
                    'q': ''  # Location will be inserted here
                }
            }
        }
    ```

## Error Handling

The program includes error handling to catch potential issues:

*   `HTTPError`: Catches HTTP errors (e.g., incorrect API key, network issues).
*   `Exception`: Catches other exceptions that may occur during the API request or data processing.
*   `UnboundLocalError`: Catches errors if the `r` variable (containing the API response) is accessed before it's assigned a value (e.g., if an HTTP error occurred).

The program will print informative error messages and exit if an error occurs.

## Requirements

*   Python 3.x
*   `requests` library (install with `pip install requests`)
*   `python-dotenv` library (install with `pip install python-dotenv`) (Optional, but recommended for API key management)

## License

 MIT License

## Contact

email address: regasior@gmail.com, 
GitHub: https://github.com/renioko
