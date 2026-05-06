## Raw Data Directory

This directory contains all of the unclean, raw data that we collect. Here is what each file contains:

`census_data.csv`: Contains all of the census data we collect from [fetch_census_data.py](/scripts/fetch_census_data.py).

`public_schools.zip`: .zip file of all of the public school data that we retrieve using [fetch_and_convert_school_data.py](/scripts/fetch_and_convert_school_data.py).

`postsecondary_schools.zip`: .zip file of all of the postsecondary school data that we retrieve using [fetch_and_convert_school_data.py](/scripts/fetch_and_convert_school_data.py).

`EDGE_GEOCODE_POSTSECSCH_2425.xlsx`: Excel file extraced from `postsecondary_schools.zip`.

`EDGE_GEOCODE_PUBLICSCH_2425.xlsx`: Excel file extraced from `public_schools.zip`.

`postsecondary_schools.csv`: Converted .csv file from `EDGE_GEOCODE_POSTSECSCH_2425.xlsx`.

`public_schools.csv`: Converted .csv file from `EDGE_GEOCODE_PUBLICSCH_2425.xlsx`.

`census_data.sha`: The correct value of the SHA-256 hash of `census_data.csv`. This is the hash value that the downloaded data is compared against when running the `check_integrity.py` script.

`public_schools.sha`: The correct value of the SHA-256 hash of `public_schools.csv`. This is the hash value that the downloaded data is compared against when running the `check_integrity.py` script.

`postsecondary_schools.sha`: The correct value of the SHA-256 hash of `postsecondary_schools.csv`. This is the hash value that the downloaded data is compared against when running the `check_integrity.py` script.

`data_quality_report.ipynb`: The code we used to analyze data quality.

See the [data codebook](../data_codebook.pdf) for the metadata for the three .csv files.
