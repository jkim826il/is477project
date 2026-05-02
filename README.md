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
- Open a terminal window. Navigate to the root of the project. Run the command `snakemake --cores 1`. This should run all of the scripts.
    - If the integrity check fails (it should fail with an `AssertionError`), then run the command `snakemake --cores 1 --delete-all-output`. After that, run `snakemake --cores 1` again.

## References