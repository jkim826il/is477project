#### Overview

Our overall goal of this project is two-fold: 1) Evaluate the role (if any) education plays on income, and 2) Evaluate the role the public/postsecondary school system plays on either or both education and income. To accomplish this, we will use datasets from the United States Census Bureau, specifically data on household income and educational attainment, as well as data from the National Center for Education Statistics. After evaluating and cleaning the data, we will use a mix of visualizations and numbers that we compute using the data to evaluate our two goals.

#### Team

Juno will mostly work on the implementation aspect of the project, such as data collection, integration, cleaning, and automated workflow.

Abbie will mostly work on the theoretical/higher-level aspects of the project, such as working with the data life cycle, ethical data handling, and the conceptual organization of the data.

Juno and Abbie will meet regularly in-person throughout the project and before deadlines to work on the project together and to discuss the workload plan for the day/week.

#### Research or Business Question(s)

- Are income and education positively correlated?
- Does the public/postsecondary school system impact on education and/or income?

#### Datasets

We will use the United States Census API to retrieve income and educational attainment data for each “Core Based Statistical Area” (CBSA). We will use the American Community Survey data from 2024, the most recent. We will also use this dataset (https://nces.ed.gov/programs/edge/Geographic/SchoolLocations) from the National Center for Education Statistics, which lists the geographic locations of public and postsecondary schools in the United States. We will use the data from 2024-25, the most recent data available. One of the included columns in the public/postsecondary school dataset is the CBSA code, which we will use to join these two datasets together. This will allow us to link the schools in each CBSA from the public/postsecondary school dataset with the income and educational attainment we retrieve from the Census data.

#### Timeline
Week 1 Tasks (3/9-14):
- Define the project scope: identify the project topic, research objectives, and create overall workflow; determine how the project will address the data lifecycle stages required for the project
  - Juno and Abbie
- Identify datasets: locate two datasets from trustworthy sources that are relevant to the research topic and compatible to integrate
  - Juno
- Create Project Plan: due 3/10 at 11:59pm
  - Juno and Abbie

Week 2 Tasks (3/23-27):
- Review legal and ethical constraints: evaluate data licenses, copyright restrictions, privacy concerns, and terms of use; document how they will be followed
  - Abbie
- Collect and acquire datasets: download the datasets and store the original datasets in the project repository 
  - Juno
- Design file storage and organization category: create a structured directory for organizing files (ex: raw/processed data, documentation, results) and determine the storage format
  - Abbie
Prepare data integration workflow: develop scripts using Python/Pandas or SQL to merge the datasets using common attributes
  - Juno
- Conduct data quality assessment: analyze the datasets to identify issues such as missing values, duplicate records, inconsistent formatting and outliers; document findings
  - Juno and Abbie
- Perform data cleaning: apply cleaning methods to handle missing values, inconsistent formatting, removing duplicates, and fixing other errors
  - Juno and Abbie

Week 3 Tasks (3/30-4/3):
- Write Interim Status Report: prepare a 1000-1500 word report describing the project scope, datasets, storage strategy, ethical considerations, data acquisition, integration process, and preliminary findings; due 3/31 at 11:59pm
  - Juno and Abbie

Week 4 Tasks (4/6-10):
- Develop automated workflow: implement an automated end-to-end workflow that executes the complete code including dataset acquisition, cleaning, integration, and analysis
  - Juno
- Ensure reproducibility: document all necessary key information and provide instructions for running the workflow in the README file
  - Abbie

Week 5 Tasks (4/13-17)
- Create metadata: provide metadata describing the datasets, variables, data sources, and processing steps; ensure the documentation supports reuse and discovery
  - Juno and Abbie
- Perform analysis and visualization: conduct analysis of the integrated dataset and generate visualizations or summary statistics to demonstrate the findings
  - Juno and Abbie

Week 6 Tasks (4/20-24)
- Prepare final project report: write the final project report describing the complete workflow, data lifecycle model, integration strategy, data quality results, cleaning methods, and ethical considerations
  - Juno and Abbie

Week 7 Tasks (4/27-5/1)
- Publish GitHub project release: finalize GitHub repository with scripts, documentation, metadata, datasets, and README; create the final project release for submission by 5/3 at 11:59pm
  - Juno and Abbie


#### Constraints
Because we are using data at the CBSA level, there are certain geographic locations that we may not be including in our analysis. Of note, each CBSA must have a population of at least 10,000. As a result, there are certain areas in the United States that are not in a CBSA. Because of this, there are sections of the rural population that we are not including in this analysis. The reason we decided to use CBSA instead of potentially other geographic options (such as county, city, etc.) is because we wanted to avoid situations where we have limited or no data for a certain geographic area. Using CBSA as our geographic region size allows us to increase our odds that there will be sufficient data in each geographic area that we are analyzing.

The data collected is based on a small sample of the United States population. This sample is likely smaller than one during a decennial census. This data is from 2024, which is not a year that the census takes place. As a result, the data is subject to sampling variability. It is also possible that this sample does not accurately reflect the population that it claims to represent, despite best efforts by the Census Bureau.

The data is also self-reported. As a result, it is subject to reporting errors. This issue can arise when households are reporting their income, as some may either intentionally or unintentionally misreport their household income. Others may misrepresent their educational attainment.


#### Gaps
Neither Abbie nor Juno have created an automated end-to-end workflow before, so this is one area where we will need additional input down the line.

Abbie has little experience working with SQL, so if we do decide to use a SQL database, she may need a bit of additional support from Juno (who does have some past SQL experience).
