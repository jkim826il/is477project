import pandas as pd

census_data = pd.read_csv("./raw_data/census_data.csv")

census_data.to_csv("./processed_data/census_data_cleaned.csv", index=False)