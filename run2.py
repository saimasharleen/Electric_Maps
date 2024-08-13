import requests
import json

# Your API key
api_key = "aPJsgKlOxR8i3"

# List of countries with their zone identifiers
countries = {
    "Estonia": "EE",
    "Finland": "FI",
    "France": "FR",
    "Germany": "DE",
    "Italy": "IT",
    "Norway": "NO",
    "Singapore": "SG"
}

# Set the base API endpoint
base_url = "https://api.electricitymap.org/v3/carbon-intensity/latest?zone="

# Set the headers
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Loop through each country and get the data
for country, zone_id in countries.items():
    url = base_url + zone_id
    response = requests.get(url, headers=headers)
    
    # Check the status of the response
    if response.status_code == 200:
        data = response.json()
        
        # Extract the desired information
        datetime_utc = data.get("datetime", "N/A")
        zone_name = country
        carbon_intensity_direct = data.get("carbonIntensity", "N/A")
        carbon_intensity_lca = "N/A"  # This specific field isn't provided in the response
        low_carbon_percentage = "N/A"  # This information isn't in the provided response
        renewable_percentage = "N/A"  # This information isn't in the provided response
        data_source = data.get("emissionFactorType", "N/A")
        data_estimated = data.get("isEstimated", "N/A")
        data_estimation_method = data.get("estimationMethod", "N/A")
        
        # Print the information for each country
        print(f"Country: {country}")
        print(f"Datetime (UTC): {datetime_utc}")
        print(f"Zone Id: {zone_id}")
        print(f"Carbon Intensity gCO2eq/kWh (direct): {carbon_intensity_direct}")
        print(f"Carbon Intensity gCO2eq/kWh (LCA): {carbon_intensity_lca}")
        print(f"Low Carbon Percentage: {low_carbon_percentage}")
        print(f"Renewable Percentage: {renewable_percentage}")
        print(f"Data Source: {data_source}")
        print(f"Data Estimated: {data_estimated}")
        print(f"Data Estimation Method: {data_estimation_method}")
        print("-" * 40)  # Separator for each country output

    else:
        print(f"Failed to fetch data for {country}. Status code: {response.status_code}, Message: {response.text}")
        print("-" * 40)

