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

## Data Cleaning

## Findings

Before running any of the analysis, we first plotted every variable with every other variable (we will refer to this plot as a pairplot for the remainder of this section). This is the result:

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
