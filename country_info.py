import requests

print("=== COUNTRY INFORMATION ===")

country = input("Enter a country name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]

    name = data["name"]["common"]
    capital = data.get("capital", ["Unknown"])[0]
    region = data.get("region", "Unknown")
    population = data.get("population", 0)

    print("\n🌍 Country:", name)
    print("🏛️ Capital:", capital)
    print("🌎 Region:", region)
    print("👥 Population:", population)

else:
    print("❌ Country not found.")

print("\n🚀 You just used your first API!")
