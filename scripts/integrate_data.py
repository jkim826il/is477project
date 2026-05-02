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

# Columns for census and school data
census_columns = ["name","cbsa_code","median_income","total_population","population_25_plus","hs_diploma","ged","associates","bachelors","masters","professional","doctorate"]
school_columns = ["ID","NAME","STREET","CITY","STATE","ZIP","STFIP","CNTY","NMCNTY","LOCALE","LAT","LON","CBSA","NMCBSA","CBSATYPE","CD","SLDL","SLDU"]

# Drop columns with duplicate "cbsa_code" and store in smaller
smaller = merged[census_columns].drop_duplicates(subset=["cbsa_code"])

# Count the number of public & postsecondary schools
count_public = merged[merged["School Type"] == "Public"][["cbsa_code", "School Type"]].groupby("cbsa_code").agg("count").reset_index()
count_postsecondary = merged[merged["School Type"] == "Postsecondary"][["cbsa_code", "School Type"]].groupby("cbsa_code").agg("count").reset_index()

# Join on public schools
merge1 = smaller.merge(count_public, on="cbsa_code", how="left").fillna(0)
merge1 = merge1.rename(columns={"School Type" : "Public Schools"})

# Join on postsecondary schools
merge2 = merge1.merge(count_postsecondary, on="cbsa_code", how="left").fillna(0)
merge2 = merge2.rename(columns={"School Type" : "Postsecondary Schools"})
merge2["Postsecondary Schools"] = merge2["Postsecondary Schools"].apply(lambda x: int(x))

# Add columns to be based on a percentage of the total population for postsecondary schools
merge2["hs_diploma_per_greater_than_25_pop"] = merge2["hs_diploma"] / merge2["population_25_plus"]
merge2["ged_per_greater_than_25_pop"] = merge2["ged"] / merge2["population_25_plus"]
merge2["associates_per_greater_than_25_pop"] = merge2["associates"] / merge2["population_25_plus"]
merge2["bachelors_per_greater_than_25_pop"] = merge2["bachelors"] / merge2["population_25_plus"]
merge2["masters_per_greater_than_25_pop"] = merge2["masters"] / merge2["population_25_plus"]
merge2["professional_per_greater_than_25_pop"] = merge2["professional"] / merge2["population_25_plus"]
merge2["doctorate_per_greater_than_25_pop"] = merge2["doctorate"] / merge2["population_25_plus"]

# Add columns to be based on a percentage of the total population for postsecondary schools
merge2["Public_Schools_per_total_pop"] = merge2["Public Schools"] / merge2["total_population"]
merge2["Postsecondary_Schools_per_total_pop"] = merge2["Postsecondary Schools"] / merge2["total_population"]

# Drop columns that are no longer needed
merge2 = merge2.drop(columns=["total_population", "population_25_plus", "hs_diploma", "ged", "associates", "bachelors", "masters", "professional", "doctorate", "Public Schools", "Postsecondary Schools"])

# Save to csv

merge2.to_csv("./integrated_data/integrated.csv", index=False)