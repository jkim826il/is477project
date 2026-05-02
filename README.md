## Title: To what extent does education impact median household income?

## Contributors

- Juno Kim (NetID: jkim826)
- Abbie Long (NetID: abbiel2)

## Summary

## Data Profile

## Data Quality

## Data Cleaning

## Findings

## Future Work

## Challenges

## Reproducibility

#### Software & Dependency Installation

To run all of the data collection, cleaning, integration, and analysis, you will need the following software installed in this exact way.

- Clone this repository (using `git clone` or similar)
- Our analysis needs **Python version 3.14.4** installed. Please install it for your specific operating system here: https://www.python.org/downloads/release/python-3144/. Do NOT install Python using Conda or any other way; you must use the link above. You do NOT need a virtual environment (using venv, conda, or similar). **Do NOT use the Python Install Manager**: that may install the wrong version of Python. Please use the dedicated installers at the bottom of the page.
    - Before clicking "Install Now" on the dedicated installer, make sure check the box "Add python.exe to PATH".
![](/markdown_assets/python_installer.png)
- Open a terminal window and navigate to the root of the project. Run the command `pip install -r requirements.txt`.
    - Doing this should also install Snakemake. Do NOT install Snakemake any other way. Otherwise, our codebase will not run.
    - On Windows, the Snakemake install may fail due to missing C++ development dependencies. Follow the link in the error message to install Visual Studio. Run the installer and install the C++ dependencies.

#### Running Our Scripts

- Open a terminal window. Navigate to the root of the project. Run the command `snakemake --cores 1`. This should run all of the scripts.

## References