import requests
import pandas as pd
from zipfile import ZipFile

# 1) Fetch the school data from the Education Department website
print("Start Stage 1a")
public_request = requests.get("https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2425.zip", params=None)

print("Start Stage 1b")
postsecondary_request = requests.get("https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECSCH_2425.zip", params=None)

# 2) Write the .zip files to disk
print("Start Stage 2")
with open("./raw_data/public_schools.zip", mode="wb") as public_f:
    public_f.write(public_request.content)

with open("./raw_data/postsecondary_schools.zip", mode="wb") as postsecondary_f:
    postsecondary_f.write(postsecondary_request.content)

# 3) Extract the zip files and save the .xlsx files to disk
print("Start Stage 3")
with ZipFile("./raw_data/public_schools.zip", "r") as z1:
    z1.extract("EDGE_GEOCODE_PUBLICSCH_2425.xlsx", path="./raw_data")

with ZipFile("./raw_data/postsecondary_schools.zip", "r") as z2:
    z2.extract("EDGE_GEOCODE_POSTSECSCH_2425.xlsx", path="./raw_data")

# 4) Convert the .xlsx files to .csv files
print("Start Stage 4")
public_schools = pd.read_excel("./raw_data/EDGE_GEOCODE_PUBLICSCH_2425.xlsx")
postsecondary_schools = pd.read_excel("./raw_data/EDGE_GEOCODE_POSTSECSCH_2425.xlsx")

public_schools.to_csv("./raw_data/public_schools.csv", index=False)
postsecondary_schools.to_csv("./raw_data/postsecondary_schools.csv", index=False)