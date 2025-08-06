import requests
from bs4 import BeautifulSoup
import time

def get_weather(city):
    city = city.lower().replace(" ", "-")
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            desc = soup.find('span', class_='phrase')
            
            if desc:
                print(f"\n📍 Weather in {city.capitalize()}:")
                print(f"{desc.text.strip()}")
            else:
                print("⚠️ Weather description not found.")
        else:
            print("❌ Unable to fetch data. Try another city.")
    except Exception as e:
        print("🚫 Error:", e)

# 💡 Run this every 60 seconds
city_name = input("Enter city name: ")

while True:
    get_weather(city_name)
    print("\n🔄 Refreshing in 60 seconds...\n")
    time.sleep(60)
