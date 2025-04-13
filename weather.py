import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("WEATHER_API_KEY")

# Base URL for OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Function to fetch weather data
def get_weather(city):
    # Construct the complete API URL
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Send a request to the API
    response = requests.get(complete_url)
    
    # Convert the response to JSON format
    data = response.json()

    # Check if the response code is successful (200)
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Extract the necessary data
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]
        
        # Print the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description.capitalize()}")
    else:
        print("City not found or error in fetching data.")

# Prompt user to input a city name
city_name = input("Enter city name: ")
get_weather(city_name)
