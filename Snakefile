rule run_all:
    input:
        "analysis/pairplot.png",
        "analysis/r_squared_values.txt"

rule fetch_data_and_check_integrity:
    output:
        "raw_data/census_data.csv",
        "raw_data/postsecondary_schools.csv",
        "raw_data/public_schools.csv"
    shell:
        "python scripts/fetch_census_data.py && python scripts/fetch_and_convert_school_data.py && python scripts/check_integrity.py"

rule process_data:
    input:
        "raw_data/census_data.csv",
        "raw_data/postsecondary_schools.csv",
        "raw_data/public_schools.csv"
    output:
        "processed_data/census_data_cleaned.csv",
        "processed_data/postsecondary_schools_cleaned.csv",
        "processed_data/public_schools_cleaned.csv"
    shell:
        "python scripts/process_census_data.py && python scripts/process_school_data.py"
        
rule integrate_data:
    input:
        "processed_data/census_data_cleaned.csv",
        "processed_data/postsecondary_schools_cleaned.csv",
        "processed_data/public_schools_cleaned.csv"
    output:
        "integrated_data/integrated.csv"
    shell:
        "python scripts/integrate_data.py"

rule analyze_data:
    input:
        "integrated_data/integrated.csv"
    output:
        "analysis/pairplot.png",
        "analysis/r_squared_values.txt"
    shell:
        "python scripts/analysis.py"