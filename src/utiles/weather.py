import requests
from dotenv import load_dotenv
import os

def get_weather(city_name):
    """
    Fetches real-time weather directly by city name using WeatherAPI.com.
    """
  
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    
   
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name.strip()}"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            
            # Extract data cleanly out of the JSON structure
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"].lower()
            
            return f"The current weather in {location}, {country} is {temp}°C and it is mostly {condition}."
        elif response.status_code == 400:
            return f"I couldn't find a city named {city_name}. Please check the spelling."
        else:
            return "I am currently unable to connect to the weather network."
            
    except Exception:
        return "Network error. Please check your internet connection."
    