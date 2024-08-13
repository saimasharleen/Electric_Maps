import requests
import json

# Your API key
api_key = "aPJsgKlOxR8i3"

# Set the API endpoint
url = "https://api.electricitymap.org/v3/carbon-intensity/latest?zone=DE"

# Set the headers
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the request
response = requests.get(url, headers=headers)

# Check the status of the response
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))  # Print the entire data structure
else:
    print(f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}")

