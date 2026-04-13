### Juno's Work So Far:

So far, my work has focused on acquiring and analyzing the data for missing values, errors, etc. 

As for acquiring the data, I acquired an API Key from the U.S. Census Bureau (not on GitHub for obvious reasons) and worked on getting the data that we need. I queried the API for data regarding Median Household Income, Total Population, Total Population 25+ years old, and population with a High School Diploma, GED, Associate’s Degree, Bachelor’s Degree, Master’s Degree, Professional Degree, and Doctorate Degree for each “Core Based Statistical Area” (CBSA), which in the API is defined as a metropolitan or micropolitan statistical area. I did do some error checking and replaced common null values that the census defines (for example, a value of -666666666 means that an estimate could not be computed) with a value of “None” before converting this data into a CSV file that we could use for analysis and processing. All of this is done in the `fetch_census_data.py` file (https://github.com/jkim826il/is477project/blob/main/fetch_census_data.py).

The public and postsecondary school data came from this website (https://nces.ed.gov/programs/edge/Geographic/SchoolLocations). I downloaded the 2024-25 “Public School File” and “Postsecondary School File.” These files were ZIP files. After extracting the contents, I took the “EDGE_GEOCODE_xxx_2425.xlsx” files (substitute “xxx” with “POSTSECSCH” for postsecondary and “PUBLICSCH” for public school) and copied them to the “raw_data” directory in our repository (see https://github.com/jkim826il/is477project/tree/main/raw_data). I then converted these .xlsx files into CSV files using Pandas (see `convert_school_data.py`: https://github.com/jkim826il/is477project/blob/main/convert_school_data.py).

I also did some preliminary data quality analysis in OpenRefine. Those findings are in `raw_data/tentative_data_report.md` (https://github.com/jkim826il/is477project/blob/main/raw_data/tentative_data_report.md). The Census Data did not have any missing values or errors, but both the Postsecondary and Public School data did have several issues. Some issues included missing or suspect street addresses, missing county data, and missing CBSAs, among others. The missing CBSA data is likely because those educational institutions are not physically located within a CBSA.

In the school data, I plan on removing data unnecessary for our analysis. This includes the Combined Statistical Area (CSA) data that these datasets include, among other things. After doing some closer evaluation, I will likely delete the universities with a CBSA column value of “N”. These universities are likely not located within a CBSA (CBSAs require an area to reach a certain population threshold to be considered). As for the missing or suspect street addresses, there is a high probability that I just leave those as is. There is likely not an easy way to retrieve the correct addresses of each university, and the accuracy of street addresses is not super important to the research we are doing. As long as the CBSA data is there, we can work with that.

I have not started the Data Cleaning process yet because I wanted to spend more time analyzing the Data Quality before continuing. Since I have not cleaned the data yet, I also was not able to start the data integration workflow, since that requires joining on CBSA, and the CBSA column in the school data has missing values. These tasks will be pushed into the Week 3 and Week 4 tasks.

### Abbie's Work So Far:



### Changes to Our Plan

We did not make changes to the plan after resubmitting our plan on April 2nd. We needed to update our timeline slightly, and that is listed below.

### Updated Timeline:

Week 1 Tasks (3/9-14):

- Define the project scope: identify the project topic, research objectives, and create overall workflow; determine how the project will address the data lifecycle stages required for the project ✅
    - Juno and Abbie
- Identify datasets: locate two datasets from trustworthy sources that are relevant to the research topic and compatible to integrate ✅
    - Juno
- Create Project Plan: due 3/10 at 11:59pm ✅
    - Juno and Abbie

Week 2 Tasks (3/23-4/6):

- Review legal and ethical constraints: evaluate data licenses, copyright restrictions, privacy concerns, and terms of use; document how they will be followed
    - Abbie
- Collect and acquire datasets: download the datasets and store the original datasets in the project repository ✅
    - Juno
- Design file storage and organization category: create a structured directory for organizing files (ex: raw/processed data, documentation, results) and determine the storage format
    - Abbie
- Prepare data integration workflow: develop scripts using Python/Pandas or SQL to merge the datasets using common attributes ❌ ***(pushed to Week 5)***
    - Juno
- Conduct data quality assessment: analyze the datasets to identify issues such as missing values, duplicate records, inconsistent formatting and outliers; document findings ❌ ***(started, but not complete. Will finish in Week 5)***
    - Juno and Abbie
- Perform data cleaning: apply cleaning methods to handle missing values, inconsistent formatting, removing duplicates, and fixing other errors ❌ ***(pushed to Week 5)***
    - Juno and Abbie

Week 3 & 4 Tasks (4/6-4/10):

- Write Interim Status Report: prepare a 1000-1500 word report describing the project scope, datasets, storage strategy, ethical considerations, data acquisition, integration process, and preliminary findings; due 4/13 at 11:59pm ✅
    - Juno and Abbie

Week 5 Tasks (4/13-17):

- Conduct data quality assessment: analyze the datasets to identify issues such as missing values, duplicate records, inconsistent formatting and outliers; document findings
    - Juno and Abbie
- Perform data cleaning: apply cleaning methods to handle missing values, inconsistent formatting, removing duplicates, and fixing other errors
    - Juno and Abbie
- Prepare data integration workflow: develop scripts using Python/Pandas or SQL to merge the datasets using common attributes
    - Juno
- Develop automated workflow: implement an automated end-to-end workflow that executes the complete code including dataset acquisition, cleaning, integration, and analysis
    - Juno
- Ensure reproducibility: document all necessary key information and provide instructions for running the workflow in the README file
    - Abbie

Week 6 Tasks (4/20-24):

- Create metadata: provide metadata describing the datasets, variables, data sources, and processing steps; ensure the documentation supports reuse and discovery
    - Juno and Abbie
- Perform analysis and visualization: conduct analysis of the integrated dataset and generate visualizations or summary statistics to demonstrate the findings
    - Juno and Abbie

Week 7 Tasks (4/27-5/1):

- Prepare final project report: write the final project report describing the complete workflow, data lifecycle model, integration strategy, data quality results, cleaning methods, and ethical considerations
    - Juno and Abbie
- Publish GitHub project release: finalize GitHub repository with scripts, documentation, metadata, datasets, and README; create the final project release for submission by 5/3 at 11:59pm
    - Juno and Abbie
