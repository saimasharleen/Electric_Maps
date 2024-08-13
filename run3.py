import requests
import psycopg2
from psycopg2 import sql
from datetime import datetime

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

# Database connection setup
conn = psycopg2.connect(
    dbname="carbon_intensity",
    user="exporter_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Function to insert data into the database
def insert_data(data):
    insert_query = sql.SQL("""
        INSERT INTO carbon_data (datetime_utc, country, zone_id, carbon_intensity_direct, carbon_intensity_lca,
                                 low_carbon_percentage, renewable_percentage, data_source, data_estimated, 
                                 data_estimation_method)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    cur.execute(insert_query, data)
    conn.commit()

# Loop through each country and get the data
for country, zone_id in countries.items():
    url = base_url + zone_id
    response = requests.get(url, headers=headers)
    
    # Check the status of the response
    if response.status_code == 200:
        data = response.json()
        
        # Extract the desired information
        datetime_utc = data.get("datetime", "N/A")
        carbon_intensity_direct = data.get("carbonIntensity", "N/A")
        carbon_intensity_lca = None  # This specific field isn't provided in the response
        low_carbon_percentage = None  # This information isn't in the provided response
        renewable_percentage = None  # This information isn't in the provided response
        data_source = data.get("emissionFactorType", "N/A")
        data_estimated = data.get("isEstimated", "N/A")
        data_estimation_method = data.get("estimationMethod", "N/A")
        
        # Prepare the data for insertion
        record = (
            datetime_utc, country, zone_id, carbon_intensity_direct, carbon_intensity_lca,
            low_carbon_percentage, renewable_percentage, data_source, data_estimated, data_estimation_method
        )
        
        # Insert the data into the database
        insert_data(record)

        # Log the success
        print(f"Data inserted successfully for {country} at {datetime.utcnow()} UTC")

    else:
        print(f"Failed to fetch data for {country}. Status code: {response.status_code}, Message: {response.text}")

# Close the database connection
cur.close()
conn.close()
