import pandas as pd

census_data = pd.read_csv("./processed_data/census_data_cleaned.csv")
postsecondary_data = pd.read_csv("./processed_data/postsecondary_schools_cleaned.csv")
public_school_data = pd.read_csv("./processed_data/public_schools_cleaned.csv")

postsecondary_data["School Type"] = "Postsecondary"
public_school_data["School Type"] = "Public"

# Vertically stack the school data
stacked = pd.concat([postsecondary_data, public_school_data])

# Merge the census data and the stacked school data on the CBSA
merged = pd.merge(census_data, stacked, left_on="cbsa_code", right_on="CBSA", how="inner")

# Save to csv

merged.to_csv("./integrated_data/integrated.csv", index=False)