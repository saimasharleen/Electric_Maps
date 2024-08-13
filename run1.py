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
    
    # Extract the desired information based on the structure of the response
    datetime_utc = data.get("datetime", "N/A")
    country = "Germany"  # Since the zone is DE, which corresponds to Germany
    zone_name = "Germany"  # Assuming the zone name corresponds to the country
    zone_id = data.get("zone", "N/A")
    carbon_intensity_direct = data.get("carbonIntensity", "N/A")
    carbon_intensity_lca = "N/A"  # This specific field isn't provided in the response
    low_carbon_percentage = "N/A"  # This information isn't in the provided response
    renewable_percentage = "N/A"  # This information isn't in the provided response
    data_source = data.get("emissionFactorType", "N/A")
    data_estimated = data.get("isEstimated", "N/A")
    data_estimation_method = data.get("estimationMethod", "N/A")
    
    # Print the information
    print(f"Datetime (UTC): {datetime_utc}")
    print(f"Country: {country}")
    print(f"Zone Name: {zone_name}")
    print(f"Zone Id: {zone_id}")
    print(f"Carbon Intensity gCO2eq/kWh (direct): {carbon_intensity_direct}")
    print(f"Carbon Intensity gCO2eq/kWh (LCA): {carbon_intensity_lca}")
    print(f"Low Carbon Percentage: {low_carbon_percentage}")
    print(f"Renewable Percentage: {renewable_percentage}")
    print(f"Data Source: {data_source}")
    print(f"Data Estimated: {data_estimated}")
    print(f"Data Estimation Method: {data_estimation_method}")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}, Message: {response.text}")

