## Raw Data Directory

This directory contains all of the unclean, raw data that we collect. Here is what each file contains:

`census_data.csv`: Contains all of the census data we collect from [fetch_census_data.py](/scripts/fetch_census_data.py).

`public_schools.zip`: .zip file of all of the public school data that we retrieve using [fetch_and_convert_school_data.py](/scripts/fetch_and_convert_school_data.py).

`postsecondary_schools.zip`: .zip file of all of the postsecondary school data that we retrieve using [fetch_and_convert_school_data.py](/scripts/fetch_and_convert_school_data.py).

`EDGE_GEOCODE_POSTSECSCH_2425.xlsx`: Excel file extraced from `postsecondary_schools.zip`.

`EDGE_GEOCODE_PUBLICSCH_2425.xlsx`: Excel file extraced from `public_schools.zip`.

`postsecondary_schools.csv`: Converted .csv file from `EDGE_GEOCODE_POSTSECSCH_2425.xlsx`.

`public_schools.csv`: Converted .csv file from `EDGE_GEOCODE_PUBLICSCH_2425.xlsx`.