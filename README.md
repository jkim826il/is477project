## Title: To what extent does education impact median household income?

## Contributors

- Juno Kim (NetID: jkim826)
- Abbie Long (NetID: abbiel2)

## Summary

This project examines the relationship between education, income, and the availability of public and postsecondary schools across U.S. metropolitan and micropolitan areas. The motivation for the project came from a broader interest in understanding whether educational attainment is associated with higher income, and whether the local school system may play a measurable role in shaping either education or income outcomes. Since education is often discussed as a pathway to economic mobility, the project focuses on whether that assumption is supported in the data and whether school availability adds meaningful explanatory value.

The project is guided by two main research questions: Are income and education positively correlated? and Does the public/postsecondary school system impact education and/or income? To investigate these questions, the project uses data from the U.S. Census Bureau and the National Center for Education Statistics. The Census dataset includes information for 936 U.S. cities or CBSAs, including median income, total population, population age 25 and older, and counts of people with different levels of educational attainment, such as high school diplomas, GEDs, associate’s degrees, bachelor’s degrees, master’s degrees, professional degrees, and doctorates. The NCES datasets include the 2024–25 public school file and postsecondary school file, containing geographic and institutional information for 102,179 public schools and 6,606 postsecondary schools. These datasets were integrated using CBSA codes so that school availability could be compared with income and educational attainment at a regional level.

Before analysis, the data was evaluated for quality, including completeness, accuracy, consistency, and timeliness. The Census dataset had no missing values after accounting for Census-specific null codes, although it was limited to areas included in CBSAs, meaning rural and sparsely populated areas were excluded. The public and postsecondary school datasets contained some missing values, especially in CBSA fields, as well as syntactic and semantic issues in address and city fields. To prepare the school datasets for integration, observations missing CBSA codes were removed, unnecessary columns were dropped, and identifying columns were renamed for consistency. The final integrated dataset converted educational attainment counts into percentages of the population aged 25 and older, and school counts into schools-per-population measures.

The analysis used visualizations and several linear regression models to evaluate the relationships among income, education, and school availability. Initial pairplots suggested that median income did not have a very strong visual relationship with most variables. However, several post-bachelor’s education variables appeared closely related to one another, raising potential multicollinearity concerns. To address this, the project tested multiple regression models using different combinations of educational attainment and school availability variables.

The findings were mixed. The model using all education and school variables produced an R² value of 0.511, meaning the model explained about 51.1% of the variation in median income. A model using only educational attainment variables produced an R² of 0.472, while a model using only school-per-population variables had a much lower R² of 0.059. These results suggest that educational attainment explains more variation in income than school availability alone. However, adding public and postsecondary school variables to a reduced education model increased the R² from 0.437 to 0.479, meaning school availability did add some information.

Overall, the project found that education and income are related, but the relationship is not especially strong in the models tested. The school system, measured by public and postsecondary schools per population, appears to have only a small impact on explaining income differences. The results suggest that education matters, but income is likely shaped by many additional social, economic, and geographic factors beyond educational attainment and school availability alone.

## Data Profile

'census_data.csv': Contains all of the census data we collect from fetch_census_data.py.
	
The 'census_data.csv' file contains all of the census data and has 936 rows and 12 columns. It contains data from different cities around the U.S. and has information pertaining to median income, population, and how many people there are with different degrees of education (e.g., high school, bachelors, masters, doctorate, etc.). This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.

The dataset was obtained from the U.S. Census Bureau and all of their legal terms and conditions are stated on their website. It states that users of the data are not to use the data “to identify any individual person, household, business or other entity” or combine the data to achieve any of the previously stated goals. The Bureau also states that the user of the information “may not modify or falsely represent content accessed through the API and still claim the source is the Census Bureau.”

The dataset relates to our question about how education relates to income because the dataset provides samples from various cities across the U.S. about the number of people with degrees of higher education as well as the city’s median income.

'postsecondary_schools.csv': Converted .csv file from EDGE_GEOCODE_POSTSECSCH_2425.xlsx.

This CSV file contains 21 columns and 6606 rows. Each row represents a sample from a post-secondary school lists the following attributes of each observation: school identification number, name of institution, reported street address, reported city, reported state, reported ZIP code, state FIPS, county FIPS, county name, locale code, latitude of school location, longitude of school location, core based statistical area, core based statistical area name, metropolitan or micropolitan statistical area indicator, combined statistical area, combined statistical area name, congressional district, state legislative district - lower, state legislative district - upper, and school year. This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.
This dataset was retrieved from the National Center for Education Statistics, an official website of the U.S. government. We could not find information on the website about any legal constraints the dataset may have. The dataset relates to the questions because it contains information about post-secondary schools and other attributes that they have that could help with education demographic and geographic estimates.

'public_schools.csv': Converted .csv file from EDGE_GEOCODE_PUBLICSCH_2425.xlsx.

This CSV file contains 23 columns and 102,179 rows in the dataset. Each row contains information about a public school in the U.S. and has the following attributes: school identification number, school district identification number, name of institution, FIPS state code for operating state, reported location street address, reported location city, reported location state, reported location ZIP code, state FIPS, county FIPS, county name, locale code, latitude of school location, longitude of school location, core based statistical area, core based statistical area name, metropolitan or micropolitan statistical area indicator, combined statistical area, combined statistical area name, congressional district, state legislative district - lower, state legislative district - upper, and school year. This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.

This dataset was retrieved from the National Center for Education Statistics, an official website of the U.S. government. We could not find information on any legal constraints the dataset may have on the website. The dataset relates to the research questions because it contains information about public schools and local education and other attributes that they have that could help with education demographic and geographic estimates.

## Data Quality

## Data Cleaning

## Findings

## Future Work

## Challenges

## Reproducibility

#### Software & Dependency Installation

To run all of the data collection, cleaning, integration, and analysis, you will need the following software installed in this exact way.

- Clone this repository by running `git clone https://github.com/jkim826il/is477project.git` in the terminal on your operating system.
    - Note: This requires Git to be installed. Please install Git from [here](https://git-scm.com/) if you do not have it installed.
- Our analysis needs **Python version 3.14.4** installed. Please install it for your specific operating system here: https://www.python.org/downloads/release/python-3144/. Do NOT install Python using Conda or any other way; you must use the link above. You do NOT need a virtual environment (using venv, conda, or similar). **Do NOT use the Python Install Manager**: that may install the wrong version of Python. Please use the dedicated installers at the bottom of the page.
    - Before clicking "Install Now" on the dedicated installer, make sure check the box "Add python.exe to PATH".
![](/markdown_assets/python_installer.png)
- Open a terminal window and navigate to the root of the project. Run the command `pip install -r requirements.txt`.
    - Doing this should also install Snakemake. Do NOT install Snakemake any other way. Otherwise, our codebase will not run.
    - On Windows, you may get this error message: `error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/`. Follow the link in the error message and click "Install Build Tools". Run the installer. In the prompt that appears, check the box that says "Desktop development with C++" and then click the "Install" button.
![](/markdown_assets/visual_studio_installer.png)
    - Re-run the `pip install -r requirements.txt` command after installing the C++ Build Tools.

#### Running Our Scripts

- Request an API Key from the [U.S. Census website](https://api.census.gov/data/key_signup.html).
- Create a new directory called "private" from the root of the project. Inside that directory, create a text file named `api_key.txt`. Copy and paste the API Key that you receive into the .txt file. 
- After the above step, this is what the project directory should look like:

![](/markdown_assets/project_directory.png)
- Open a terminal window. Navigate to the root of the project. Run the command `snakemake --cores 1`. This should run all of the scripts.
    - If the integrity check fails (it should fail with an `AssertionError`), then run the command `snakemake --cores 1 --delete-all-output`. After that, run `snakemake --cores 1` again.
- **NOTE:** Depending on the system, the $R^2$ values in `r_squared_values.txt` may round or not round the least significant digit. This does not impact any other part of data cleaning/integration/analysis; it only affects this one .txt file. This also does not change the conclusion of our analysis. This is likely happening because we do not have a centralized development environment through something like a Docker container.

## References
