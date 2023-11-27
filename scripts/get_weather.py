import requests
import json

def load_settings():
    try:
        with open('projectsettings.json', 'r') as file:
            settings = json.load(file)
            return settings
    except FileNotFoundError:
        print("Error: projectsettings.json not found.")
        return None

def is_valid_plz(plz):
    return plz.isdigit() and len(plz) == 5

def get_weather(api_key, plz):
    if not is_valid_plz(plz):
        print("Error: Invalid PLZ. Please enter a valid German postal code.")
        return False

    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'zip': f'{plz},de',
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"---------------------------")
        return True
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
        return False

def main():
    settings = load_settings()

    if settings:
        api_key = settings.get('openweathermap_api_key')

        if api_key:
            while True:
                plz = input("Enter the German PLZ (postal code): ")
                if get_weather(api_key, plz):
                    break  
        else:
            print("Error: openweathermap_api_key not found in projectsettings.json.")
    else:
        print("Exiting due to missing project settings.")

if __name__ == "__main__":
    main()
