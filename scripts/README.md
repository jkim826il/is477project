## Scripts Directory

This directory contains all of the scripts that are used to collect, process, clean, and analyze the data. Here is a brief description of what each of the scripts do, in the order they should be run:

1. `fetch_census_data.py`: Gets all of the Census Data we need from the American Community Survey (2024) from the United States Census API. After fetching the data, outputs the data into `/raw_data/census_data.csv`. **NOTE:** To run this code, you must request an API key from the U.S. Census [here](https://api.census.gov/data/key_signup.html) and store it in `../private/api_key.txt`.

2. `fetch_and_convert_school_data.py`: Fetches the Public & Postsecondary School Data from the U.S. Department of Education website. These files are .zip files, which are saved into the `/raw_data/` directory. In the same script, we unzip these files and extract the .xlsx files from them, which contains the actual data. Then, we convert the .xlsx files into .csv files (`/raw_data/postsecondary_schools.csv` and `/raw_data/public_schools.csv`).

3. `check_integrity.py`: Runs integrity check on the three .csv files in `/raw_data/`. Checks the SHA-256 hash of each of the .csv files and sees if they match the correct values.

4. `process_census_data.py`: "Cleans" the census data. However, as noted in [/raw_data/data_quality_report.ipynb](/raw_data/data_quality_report.ipynb), the census data is already cleaned. This effectively just creates a new .csv file named `census_data_cleaned.csv` and stores it in `/processed_data/`.

5. `process_school_data.py`: Cleans the public and postsecondary school data. Stores the cleaned datasets into `/processed_data/postsecondary_schools_cleaned.csv` and `/processed_data/public_schools_cleaned.csv`.

6. `integrate_data.py`: Integrates `census_data_cleaned.csv`, `/processed_data/postsecondary_schools_cleaned.csv`, and `/processed_data/public_schools_cleaned.csv` into one dataset. This integrated dataset is stored in `integrated_data/integrated.csv`.

7. `analysis.py`: Performs our data analysis. Stores the output into the `/analysis/` directory.
