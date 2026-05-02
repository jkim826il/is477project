import requests
import pandas as pd

with open("private/api_key.txt") as f:
    API_KEY = f.read()

# Parameters for data fetch
# See Documentation: https://api.census.gov/data/2024/acs/acs5/variables.html
params = {
    "get": ",".join([
        "NAME",
        "B19013_001E", # Median household income
        "B01003_001E", # Total population
        "B15003_001E", # Total Population 25+
        "B15003_017E", # High School Diploma
        "B15003_018E", # GED or Alternative Credential
        "B15003_021E", # Associate's Degree
        "B15003_022E", # Bachelor's Degree
        "B15003_023E", # Master's Degree
        "B15003_024E", # Professional Degree
        "B15003_025E" # Doctorate Degree
    ]),
    "for": "metropolitan statistical area/micropolitan statistical area:*",
    "key": API_KEY
}

# Make the request
r = requests.get("https://api.census.gov/data/2024/acs/acs5", params=params)
data = r.json()

headers, *rows = data

# See Documentation Here: https://www.census.gov/data/developers/data-sets/acs-1year/notes-on-acs-estimate-and-annotation-values.html
NULL_VALS = {"-666666666", "-888888888", "-999999999"} # Null values for Census Data

# Checks if value is a null value, used in loop below
def safe_int(val):
    return None if val in NULL_VALS else int(val)

# Loop through each JSON node. Append all the variables to cbsa list
cbsa = []
for row in rows:
    cbsa.append({
        "name": row[0],
        "cbsa_code": row[11],
        "median_income": safe_int(row[1]),
        "total_population": safe_int(row[2]),
        "population_25_plus": safe_int(row[3]),
        "hs_diploma": safe_int(row[4]),
        "ged": safe_int(row[5]),
        "associates": safe_int(row[6]),
        "bachelors": safe_int(row[7]),
        "masters": safe_int(row[8]),
        "professional": safe_int(row[9]),
        "doctorate": safe_int(row[10])
    })

# Convert to DataFrame
df = pd.DataFrame(cbsa)

# Export to CSV
df.to_csv("raw_data/census_data.csv", index=False)