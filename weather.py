import urllib.request
import json

city = input("Enter your city: ")

url = "https://wttr.in/" + city + "?format=j1"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    weather = current["weatherDesc"][0]["value"]

    print("\n🌤️ Weather Information")
    print("----------------------")
    print("City:", city)
    print("Weather:", weather)
    print("Temperature:", temperature, "°C")
    print("Feels like:", feels_like, "°C")
    print("Humidity:", humidity + "%")

except Exception:
    print("Sorry, I couldn't get the weather information.")
