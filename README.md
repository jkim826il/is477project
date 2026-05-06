## To what extent does education impact median household income?

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

`census_data.csv`: Contains all of the census data we collect from fetch_census_data.py.
	
The `census_data.csv` file contains all of the census data and has 936 rows and 12 columns. It contains data from different cities around the U.S. and has information pertaining to median income, population, and how many people there are with different degrees of education (e.g., high school, bachelors, masters, doctorate, etc.). This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.

The dataset was obtained from the U.S. Census Bureau and all of their legal terms and conditions are stated on their website. It states that users of the data are not to use the data “to identify any individual person, household, business or other entity” or combine the data to achieve any of the previously stated goals. The Bureau also states that the user of the information “may not modify or falsely represent content accessed through the API and still claim the source is the Census Bureau.”

The dataset relates to our question about how education relates to income because the dataset provides samples from various cities across the U.S. about the number of people with degrees of higher education as well as the city’s median income.

`postsecondary_schools.csv`: Converted .csv file from EDGE_GEOCODE_POSTSECSCH_2425.xlsx.

This CSV file contains 21 columns and 6606 rows. Each row represents a sample from a post-secondary school lists the following attributes of each observation: school identification number, name of institution, reported street address, reported city, reported state, reported ZIP code, state FIPS, county FIPS, county name, locale code, latitude of school location, longitude of school location, core based statistical area, core based statistical area name, metropolitan or micropolitan statistical area indicator, combined statistical area, combined statistical area name, congressional district, state legislative district - lower, state legislative district - upper, and school year. This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.
This dataset was retrieved from the National Center for Education Statistics, an official website of the U.S. government. We could not find information on the website about any legal constraints the dataset may have. The dataset relates to the questions because it contains information about post-secondary schools and other attributes that they have that could help with education demographic and geographic estimates.

`public_schools.csv`: Converted .csv file from EDGE_GEOCODE_PUBLICSCH_2425.xlsx.

This CSV file contains 23 columns and 102,179 rows in the dataset. Each row contains information about a public school in the U.S. and has the following attributes: school identification number, school district identification number, name of institution, FIPS state code for operating state, reported location street address, reported location city, reported location state, reported location ZIP code, state FIPS, county FIPS, county name, locale code, latitude of school location, longitude of school location, core based statistical area, core based statistical area name, metropolitan or micropolitan statistical area indicator, combined statistical area, combined statistical area name, congressional district, state legislative district - lower, state legislative district - upper, and school year. This file is located in the raw_data folder in the project repository and a cleaned version can be found in the processed_data folder.

This dataset was retrieved from the National Center for Education Statistics, an official website of the U.S. government. We could not find information on any legal constraints the dataset may have on the website. The dataset relates to the research questions because it contains information about public schools and local education and other attributes that they have that could help with education demographic and geographic estimates.

## Data Quality

How we went about evaluating data quality is located in [data_quality_report.ipynb](/raw_data/data_quality_report.ipynb). The following is a summary of that file as well as some basic analysis we did in OpenRefine. Since we did not clean the data using OpenRefine, we do not have an OpenRefine edit history file.

### Dataset 1: [Census Data](/raw_data/census_data.csv)

#### Completeness

The census data does not have missing values. This is for several reasons. When we fetch the American Community Survey data from the U.S. Census API, we check for the Census’s explicit missing values. Those missing values are:

```
NULL_VALS = {"-666666666", "-888888888", "-999999999"} # Null values for Census Data
```

When we are looping through each of the observations, we check if these “null” values are present and replace them with `None`. When we put this in a DataFrame later (like we do in the report), we should see an NaN value present (which is indicated by the data type of each row). However, as we can see in the full report, the data types do not indicate that a NaN value is present. In cases like this, we should see the data type be either “object” or “float64”, but instead we see “str” and “int64”. This indicates that there are no missing values.

While there are no missing values in the dataset, this data is not necessarily complete. This dataset only contains data for Micro/Metro areas that are a part of a CBSA. This dataset excludes rural and sparsely populated areas because they do not have a large enough population to be a part of a CBSA. As a result, this dataset is not complete in the sense that it is representative of the entire U.S. population.

#### Accuracy

We check for syntactic accuracy issues, particularly with the `names` column. We did not see any syntactic accuracy issues. All of the names of the CBSAs have consistent formatting.

Semantic accuracy is difficult to check as there is not another authoritative source to compare this dataset against. If we wanted to check semantic accuracy, we would just be querying the Census data again. We could compare it to previous years’ data, but it is possible that CBSAs have changed since then. Population also fluctuates over time (it does not necessarily always increase/decrease).

#### Consistency

There are 2 rules that needs to be satisfied:
1. `population_25_plus` must be greater than or equal to the sum of `hs_diploma`, `ged`, `associates`, `bachelors`, `masters`, `professional`, and `doctorate`.
2. `total_population` must be greater than or equal to `population_25_plus`.

Both of these rules are satisfied.

#### Timeliness

This specific dataset will not change over time. We are using the 2024 American Community Survey data from the Census, which once it is published will not change. The values that we see now should be the same even into the future.

This dataset should be appropriate to use. This data is from the most recent published American Community Survey as of April 2026. It should remain appropriate to use for about the next year or until the next American Community Survey is published.

### Dataset 2: [Public School Data](/raw_data/public_schools.csv)

#### Completeness

This dataset does have missing values. Missing data is indicated with either an “M” or an “N” in the respective column.

Specifically in reference to the `CBSA` column, any school that is missing a CBSA has an “N” in the `CBSA` column. This most likely indicates that the public school in question is not in a CBSA. For example, Andalusia High School is located in Andalusia, AL, which is located in Covington County, which is not in a CBSA. Ideally we should be more thorough and check every single entry, but doing so would require much more data (for example, every single city/county in every state) and is likely not feasible given the timeline of the project. This will be considered for future work.

#### Accuracy

This dataset suffers from both syntactic and semantic errors.

We can see that there is inconsistent capitalization and formatting in both the `CITY` and `STREET` columns. Sometimes, city names are capitalized, but other times they are not. "Road" is sometimes written "RD" or "Rd." depending on the entry. These contribute to syntactic errors.

The `STREET` column also suffers from semantic accuracy. For example, 13 public schools have their street address as simply "Main St" with no building number. This is a semantic error, as a school building should have a building number. We can also see that some schools also have multiple building numbers (for example, "9 1 and 12A").

While we can fix the syntactic errors, we do not see a way to fix the semantic errors in a timely manner, if at all. The address data of each school cannot be easily found without scraping websites of schools or asking the schools themselves.

#### Consistency

A rule that must be satisfied is that each CBSA code should match exactly 1 NMCBSA (name of CBSA). This rule is satisfied by all observations. While we can check the `CSA` and `NMCSA` columns, we will remove these columns when we clean the data as we do not need these columns in our analysis.

#### Timeliness

This particular dataset will not change over time. We are using the 2024-25 school location data from the Education Department, which should not change after the data is published. The data we see now should be the same into the future.

This data is from the 2024-25 school year, the most recent data available as of April 2026. This data should be suitable to use until the 2025-26 school year data is published by the Education Department.

### Dataset 3: [Postsecondary School Data](/raw_data/postsecondary_schools.csv)
#### Completeness

This dataset does have missing values. Missing data is indicated with either an “M” or an “N” in the respective column.

Specifically in reference to the `CBSA` column, any school that is missing a CBSA has an “N” in the `CBSA` column. This most likely indicates that the postsecondary school in question is not in a CBSA. For example, the University of West Alabama is located in Andalusia, AL, which is located in Covington County, which is not in a CBSA. Ideally we should be more thorough and check every single entry, but doing so would require much more data (for example, every single city/county in every state) and is likely not feasible given the timeline of the project. This will be considered for future work.

#### Accuracy

This dataset suffers from both syntactic and semantic errors.

We can see that there is inconsistent capitalization in the `CITY` names. One entry in particular is all upper-case, while the other ones are title-cased.

The one upper-case entry is also named "SOUTHFILED USA," which is very likely not the name of a city. Even if we removed the "USA" part, "SOUTHFILED" is also probably not the name of a city (even if "Southfield" would be).

We can likely fix the syntactic errors, but the semantic errors will require a bit more care to fix. We would need to verify and consult multiple sources to verify the facts for those semantic errors.

#### Consistency

A rule that must be satisfied is that each CBSA code should match exactly 1 NMCBSA (name of CBSA). This rule is satisfied by all observations. While we can check the `CSA` and `NMCSA` columns, we will remove these columns when we clean the data as we do not need these columns in our analysis.

#### Timeliness

This particular dataset will not change over time. We are using the 2024-25 school location data from the Education Department, which should not change after the data is published. The data we see now should be the same into the future.

This data is from the 2024-25 school year, the most recent data available as of April 2026. This data should be suitable to use until the 2025-26 school year data is published by the Education Department.

## Data Cleaning

### Dataset 1: [Census Data](/raw_data/census_data.csv)

As noted in the Data Quality section, this dataset did not suffer from missing data. As a result, we did not need to clean this dataset and left it as is.

As mentioned in the Data Quality section, ideally we should also check for semantic accuracy with another dataset, but we did not feel that there was another dataset we could do that with. As a result, there was also no semantic cleaning.

*Note: the dataset [census_data_cleaned.csv](/processed_data/census_data_cleaned.csv) is exactly the same as [census_data.csv](/raw_data/census_data.csv).*

### Dataset 2: [Public School Data](/raw_data/public_schools.csv)

There are a few things we decided to do with this dataset:

We decided to drop any observations that had an “M” or an “N” in the `CBSA` column. The reason we did this is because we were fairly confident that any public school that had an “N” in the `CBSA` column did not belong to a CBSA. Dropping any observations with a “missing” CBSA minimizes the potential issues that may arise when we are integrating the datasets.

We also decided to drop a few columns that we felt were not relevant to our analysis: `CSA`, `NMCSA`, and `SCHOOLYEAR`. We are using CBSA (and not CSA) as our region of choice, so having this column is unnecessary and may cause confusion since CBSA and CSA have very similar acronyms. `SCHOOLYEAR` is also a redundant column to have, since the dataset is from 2024-25, and every `SCHOOLYEAR` value was the same.

We also decided to drop columns that caused issues during integration. We decided to drop the `LEAID` and `OPSTFIPS` columns. The `LEAID` column is contained within the `NCESSCH` column (the LEAID is the first six digits of the `NCESSCH`, as noted in the [documentation](https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_TECHDOC.pdf)). The `OPSTFIPS` column is also not necessary in our analysis because we are just focusing on the number of schools located within a CBSA. We found that this column was causing issues during integration, so we decided to drop it.

We also decided to rename the `NCESSCH` column to `ID`, as each `NCESSCH` uniquely identifies each school. This also reduced issues during integration.

We did not drop rows with missing values that are in columns other than `CBSA`. We did this because we wanted to preserve as much of the original data as possible. Additionally, the only column that we really care about is `CBSA`, so as long as the `CBSA` data was available, we felt okay leaving other missing values in.

### Dataset 3: [Postsecondary School Data](/raw_data/postsecondary_schools.csv)

There are a few things we decided to do with this dataset:

We decided to drop any observations that had an “M” or an “N” in the `CBSA` column. The reason we did this is because we were fairly confident that any public school that had an “N” in the `CBSA` column did not belong to a CBSA. Dropping any observations with a “missing” CBSA minimizes the potential issues that may arise when we are integrating the datasets.

We also decided to drop a few columns that we felt were not relevant to our analysis: `CSA`, `NMCSA`, and `SCHOOLYEAR`. We are using CBSA (and not CSA) as our region of choice, so having this column is unnecessary and may cause confusion since CBSA and CSA have very similar acronyms. `SCHOOLYEAR` is also a redundant column to have, since the dataset is from 2024-25, and every `SCHOOLYEAR` value was the same.

We also decided to rename the `UNITID` column to `ID`, as each `UNITID` uniquely identifies each school. This reduced issues during integration.

We did not drop rows with missing values that are in columns other than `CBSA`. We did this because we wanted to preserve as much of the original data as possible. Additionally, the only column that we really care about is `CBSA`, so as long as the `CBSA` data was available, we felt okay leaving other missing values in.

## Data Integration

We first vertically stacked the postsecondary school and public school data on top of each other.

We went about integrating our data by performing a join on the CBSA code (`cbsa_code` for the Census data, `CBSA` for the school data). We then did an aggregation to count the number of schools per CBSA and stored that data in separate columns.

During integration, we did a bit more data curation. We decided to make the educational attainment data a percentage (between 0 and 1, not out of 100) based on the total population aged 25+ in each CBSA. We also made the number of public/postsecondary schools a percentage, but based on the total population instead.

We felt that making the data a percentage was needed as some CBSAs had a much larger population than others, which had the potential to make our analysis unreliable. This should make the data less sensitive to large outliers.

## Findings

Before running any of the analysis, we first plotted every variable with every other variable (we will refer to this plot as a pairplot for the remainder of this section). This is the result:

![](/analysis/pairplot.png)

From the plot, we can see that median income does not appear to have a strong relationship with any of the other variables (we can see this from the first row). However, we can see that all of the “post-bachelors” variables (5th row, columns 6-8) have a strong relationship with each other. This indicates potential multicollinearity issues if we use all 9 of the potential explanatory variables in a linear regression model. Out of 4 explanatory variables that are “post-bachelor,” we will likely need to drop 3 of them to mitigate the effect of multicollinearity.

We will plot linear regression models to answer our research question. First, a design decision that we made: We did not split the data into training/validation/test datasets or use cross-validation. This is because we do not intend to use this model to make predictions on unseen data; we just want to see the extent of the linear relationship. All of our models use `median_income` as our response variable. We will also round all R^2 values to 3 decimal places. We list more decimal places in /analysis/r_squared_values.txt.

The first model we fit is the model with all potential explanatory variables. After fitting this model, we found that the R^2 value is 0.511. This means that about 51.1% of the response variability is explained by the model. This is not particularly good, and it indicates that educational attainment and the number of schools in an area are not great predictors of income.

The second model we fit was with only the variables relating to educational attainment. This resulted in an R^2 value of 0.472.

The third model we fit has the same variables as the second model but with the high school diploma and GED variables removed. This decreased the R^2 value slightly to 0.470.

The fourth model we fit is the same model as the third model but with the Associate’s degree variable removed. This decreased the R^2 slightly to 0.469.

The fifth model we fit is an attempt to reduce the potential multicollinearity issues that were highlighted in the pairplot. This model only has the High School, GED, Associate’s, and Bachelor’s degree variables only. This had the lowest R^2 value of the models we tested at 0.437.

The sixth model is the same as the fifth model, but with the schools per population variables added. This increased our R^2 value to 0.479. This indicates that the schools per population data actually does add some information to our model.

The seventh model is the model with the schools per population data exclusively. This had the lowest R^2 value of 0.059.

These results show us that the majority of the response variability of our response variable `median_income` is explained by the educational attainment variables. We can see from our seventh model that the R^2 is by far the lowest with only the schools per population data. That said, the schools per population variables do add some information to our model, as removing them immediately dropped the R^2 value.

If we zoom out, however, we can see that the association between median income and educational attainment is pretty low. While schools per population does impact the relationship between median income and educational attainment, it is only by a small amount. As a result, we conclude that the association between median income and educational attainment is not strong, and while the number of schools per population does impact this relationship, it is not in a very meaningful way.

## Future Work

There are a few things we feel that we can work on in the future.

A potential task for the future is to work on validating semantic accuracy. In the Census data, we did not think that there would be another dataset that we felt we could accurately compare values with. That said, if we potentially do more research, it is possible that we can find a dataset that is something we can validate against. We could also use census data from previous years (such as 2023) and see if the changes that we see in the data points are reasonable given past trends. This is difficult to do, but it is something that could theoretically be done if we wanted to seriously evaluate the semantic accuracy of data in the census data.

In the school datasets, something we could do is to validate whether or not the CBSA codes for each school are correct. For each school, we could look online to find their addresses (or maybe such a dataset exists) and verify whether or not that address corresponds to that specific CBSA. This would also solve the issue of having missing or syntactic accuracy issues with the address column, since we would be looking up the address of every school in our dataset. Similar to the previous task with the census data, this would be very difficult and time consuming to do, but if accuracy was of significant importance, this is something that could be important.

Another task we could work on is providing a containerized environment (using Docker or something similar). As we will mention in the “Challenges” section, we had a lot of issues with getting our development environment set up and working. This was due to the fact that our systems had multiple versions of Python installed and different packages installed on different versions or even different Python environments. We also had some issues with rounding when outputting to a text file. A containerized environment would have solved a lot of these issues. This would also make it easier for anyone new that decides to run our analysis, as the container would have the correct version of Python and the packages needed to run our code already installed and ready to go, which reduces the headache that comes with software installation.

Another task that we could work on has to do with our analysis. In the future, we could use a different type of model (other than the linear regression models we used) to analyze the relationship between median household income and education. For example, what results would we end up with if we used a Linear SVM? What patterns could we have seen if we used clustering (such as k-means clustering)? We also could have used different linear model selection techniques, such as backwards elimination, forward selection, and stepwise selection, which would have allowed us to potentially end up with models that are not only more “performative” but also more interpretable. We also could have used regularization techniques, such as LASSO, ridge, and elastic net regression to also determine if we could find a better model than the seven models that we ended up using.

## Challenges

The biggest challenges that we dealt with were getting our workflow to work correctly, reproducibility, and getting our Python environment to work correctly.

Originally, we installed Snakemake using the recommended way listed on [Snakemake’s documentation](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html). The issue with this was that Pixi would create its own Python environment and not use the environment that we had set as the default on our system. As a result, sections of our scripts would not run correctly, often citing missing dependencies (specifically the Openpyxl dependency).

Adding to this problem was the fact that we had multiple versions of Python installed on our systems. Juno, for example, had both a Global Python installation and an installation through Conda (this is likely a remnant of how we installed Python in STAT 207). As a result, different dependencies were installed on different installations. This made running our scripts complicated, as sometimes the execution of our code would fail even though we had installed the Python packages beforehand. This made verifying reproducibility very difficult. Another weird behavior that Juno noticed was that the pip package manager would install dependencies to the Conda environment, even when Global Python was installed on the system and the Conda environment wasn’t active. The workaround that we ended up using was to uninstall all Python installations on our system (Conda, Pixi, etc.) and just install Global Python only.

We also installed Snakemake through pip instead of Pixi or Conda, which ensured that our scripts would run in the correct Python environment.

Another challenge we encountered was reproducibility in general. While issues with Snakemake and Python did contribute to this, we also experienced other challenges in this area. Since we chose not to use a containerized environment, we had to pay careful attention to how we set up our development environment. Since we did not document the steps we took to set up our environment as we went, to write the reproducibility section we needed a way to start over and install everything again to record the steps. The way Juno went about doing this was to create a brand new Windows 11 virtual machine. This allowed us to document each of the software installation steps from scratch. That said, the VM was understandably very slow to set up and use, which added considerable time to the project. Juno spent a significant amount of time just getting Windows 11 to install.

Due to the amount of additional time it took to set up and run the VM, we realized later that it may have been easier (or at the very least more productive from a reproducibility perspective) to set up a containerized environment instead of going out of our way to set up a brand new Windows 11 VM.

We also realized that, depending on the system, Python may or may not round the last (least significant) digit when displaying/printing floating-point values. There is no clear workaround for this, as this depends on the system that you are working on. Setting up a containerized environment would have prevented issues like this from arising, but by the time we realized this we did not have enough time to go back and change it.

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

National Center for Education Statistics. (2024). 2024–25 public school file [Data set]. Education Demographic and Geographic Estimates (EDGE). https://nces.ed.gov/programs/edge/Geographic/SchoolLocations

National Center for Education Statistics. (2024). 2024–25 postsecondary school file [Data set]. Education Demographic and Geographic Estimates (EDGE). https://nces.ed.gov/programs/edge/Geographic/SchoolLocations

U.S. Census Bureau. (2026, April 14). Terms of service: Census Bureau Application Programming Interface. U.S. Department of Commerce. https://www.census.gov/data/developers/about/terms-of-service.html
