# 💱 Currency Converter
# Beginner Python API Project

import urllib.request
import json

amount = float(input("Enter amount in USD: "))
currency = input("Convert to which currency? (EUR/GBP/NGN): ").upper()

url = f"https://api.frankfurter.app/latest?from=USD&to={currency}"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    rate = data["rates"][currency]
    converted_amount = amount * rate

    print("\n💱 CURRENCY CONVERSION")
    print("----------------------")
    print("Amount:", amount, "USD")
    print("Currency:", currency)
    print("Exchange rate:", rate)
    print("Converted amount:", round(converted_amount, 2), currency)

except Exception:
    print("\n❌ Unable to get the exchange rate.")
    print("Please check the currency code and try again.")
