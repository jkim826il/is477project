import pandas as pd

postsecondary_schools = pd.read_excel("raw_data/EDGE_GEOCODE_POSTSECSCH_2425.xlsx")
public_schools = pd.read_excel("raw_data/EDGE_GEOCODE_PUBLICSCH_2425.xlsx")

postsecondary_schools.to_csv("raw_data/postsecondary_schools.csv")
public_schools.to_csv("raw_data/public_schools.csv")