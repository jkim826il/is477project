#### Overview

Our overall goal of this project is two-fold: 1) Evaluate the role (if any) education plays on income, and 2) Evaluate the role (if any) race plays on either or both education and income. To accomplish this, we will use datasets from the United States Census Bureau, specifically data on household income and educational attainment. After evaluating and cleaning the data, we will use a mix of visualizations and numbers that we compute using the data to evaluate our two goals.

#### Team

Juno will mostly work on the implementation aspect of the project, such as data collection, integration, cleaning, and automated workflow.

Abbie will mostly work on the theoretical/higher-level aspects of the project, such as working with the data life cycle, ethical data handling, and the conceptual organization of the data.

Juno and Abbie will meet regularly in-person throughout the project and before deadlines to work on the project together and to discuss the workload plan for the day/week.

#### Research or Business Question(s)

- Are income and education positively correlated?
- Does race have a significant impact on education and/or income?

#### Datasets

Our datasets are listed here: https://github.com/jkim826il/is477project/blob/a68b41ae434eb26c62efef9f659e41bad5e30e81/raw/links.md. We have a total of 20 datasets, 10 of which are for household income by state and the other 10 are for educational attainment by state. Each category of data is further subdivided by race. These datasets can be integrated together because each of the datasets have an identifier to the state to which the person resides. Each of these datasets allow us to answer a specific part of the research question that we are proposing. For our first goal, we can see the income and educational attainment differences between states and determine if there is a relationship between income and educational attainment. For our second goal, 9 of the 10 datasets for each category represents a specific race. We can see how race impacts income and educational attainment using those 18 datasets.

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
This dataset is limited because the data is subdivided into states. It does not take into account specific geographic areas within states, which may have drastic income and educational attainment differences. Even within the same Illinois county, there can be dramatic differences in income based on ZIP code. Unfortunately, we do not have access to the ZIP code, only the state.

The income data is also not exact. It gives us a range where a specific household’s income is, but not the exact amount. This makes certain techniques, such as linear regression, difficult because each of the possible values are technically categorical, not numerical.

The data collected is based on a small sample of the United States population. This sample is likely smaller than one during a decennial census. This data is from 2024, which is not a year that the census takes place. As a result, the data is subject to sampling variability. It is also possible that this sample does not accurately reflect the population that it claims to represent, despite best efforts by the Census Bureau.

The data is also self-reported. As a result, it is subject to reporting errors. This is particularly an issue when the individuals are self-reporting their race/ethnicity. The Census Bureau categorizes Hispanic/Latino as an ethnicity, not a race, and it is possible that some data (particularly the data for White Alone) may encompass people that some people may not classify as “White.”


#### Gaps
Neither Abbie nor Juno have created an automated end-to-end workflow before, so this is one area where we will need additional input down the line.

Abbie has little experience working with SQL, so if we do decide to use a SQL database, she may need a bit of additional support from Juno (who does have some past SQL experience).
