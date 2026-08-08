# 🌍 API Data Fetcher
# Fetch live country information

import urllib.request
import json

country = input("Enter a country name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    country_data = data[0]

    name = country_data["name"]["common"]
    capital = country_data.get("capital", ["Unknown"])[0]
    population = country_data["population"]
    region = country_data["region"]

    print("\n🌍 COUNTRY INFORMATION")
    print("----------------------")
    print("Country:", name)
    print("Capital:", capital)
    print("Population:", population)
    print("Region:", region)

except Exception:
    print("\n❌ Country not found or API request failed.")
