import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    city_name = data["name"]
    temp_c = round(data["main"]["temp"], 2)
    humidity = round(data["main"]["humidity"], 2)
    description = data["weather"][0]["description"]
    
    temp_f = round(((temp_c * 9/5) + 32), 2)

    hours_of_sun = round(((data["sys"]["sunset"] - data["sys"]["sunrise"])/3600), 2)

    pressure = data["main"]["pressure"]
    
    # 6. Print
    print(f"In {city_name}, it is {temp_c}°C with humidity of {humidity}%. The weather is described as: {description}.")

    decision = input("Do you want to know more data? Say 'yes' or 'no'.")
    if decision == "yes":

        print(f"The temperature in Fahrenheit is {temp_f}")

        print(f"Today, there are going to be {hours_of_sun} hours of sunshine from sunrise to sunset")
        
    
        if pressure > 1013.25:
            print(f"Today, there is HIGH pressure equal to {pressure} millibars")
        
        elif data["main"]["pressure"] < 1013.25:
            print(f"Today, there is LOW pressure equal to {pressure} millibars")

        else:
            print(f"Today, there is AVERAGE pressure equal to {pressure} millibars")


    elif decision == "no":
        print("Bye!")
    
    else:
        print("Invalid Decision!")

# Try it
city = input("What city do you want weather data for?")
get_weather(city)
