# 🌍 Python API Client

import urllib.request
import json

url = "https://api.github.com"

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    print("🌐 API RESPONSE")
    print("----------------")
    print("GitHub API URL:", url)
    print("Current rate limit:", data["current_user_url"])
    print("User endpoint:", data["user_url"])
    print("Repository endpoint:", data["repository_url"])

except Exception as error:
    print("❌ Something went wrong.")
    print("Error:", error)
