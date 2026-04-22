import pandas as pd

public_schools = pd.read_csv("./raw_data/public_schools.csv")
postsecondary = pd.read_csv("./raw_data/postsecondary_schools.csv")

# Drop observations with "M" or "N" in "CBSA" column

public_schools = public_schools[(public_schools["CBSA"] != "N") & (public_schools["CBSA"] != "M")]
postsecondary = postsecondary[(postsecondary["CBSA"] != "N") & (postsecondary["CBSA"] != "M")]

# Drop "CSA", "NMCSA", and "SCHOOLYEAR" columns for better clarity

public_schools = public_schools.drop(columns=["CSA", "NMCSA", "SCHOOLYEAR"])
postsecondary = postsecondary.drop(columns=["CSA", "NMCSA", "SCHOOLYEAR"])

# Drop the "LEAID" column in public_schools since this data is contained in the "NCESSCH" column; 
# Drop the "OPSTFIPS" column in public_schools since this data is not relevant to our analysis
# and causes issues during integration

public_schools = public_schools.drop(columns=["LEAID", "OPSTFIPS"])

# Rename "NCESSCH" and "UNITID" to "ID" for simplicity

public_schools = public_schools.rename(columns={"NCESSCH" : "ID"})
postsecondary = postsecondary.rename(columns={"UNITID" : "ID"})

# Save files in processed_data directory

public_schools.to_csv("./processed_data/public_schools_cleaned.csv", index=False)
postsecondary.to_csv("./processed_data/postsecondary_schools_cleaned.csv", index=False)