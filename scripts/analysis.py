import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

integrated = pd.read_csv("./integrated_data/integrated.csv")

# Generate Pair Plot
sns.pairplot(integrated.drop(columns=["name", "cbsa_code"]))
plt.savefig("./analysis/pairplot.png")

# Full Model
all_columns = "+".join(integrated.columns.difference(["name", "cbsa_code", "median_income"]))
new_formula = "median_income~" + all_columns
model = smf.ols(formula=new_formula, data=integrated).fit()
rsquared_1 = model.rsquared

# Educational Attainment Only
columns2 = "+".join(integrated.columns.difference(["name", "cbsa_code", "median_income", "Postsecondary_Schools_per_total_pop", "Public_Schools_per_total_pop"]))
formula2 = "median_income~" + columns2
model2 = smf.ols(formula=formula2, data=integrated).fit()
rsquared_2 = model2.rsquared

# Greater than High School (or equivalent) Only
columns3 = "+".join(integrated.columns.difference(["name", "cbsa_code", "median_income", "Postsecondary_Schools_per_total_pop", "Public_Schools_per_total_pop", "hs_diploma_per_greater_than_25_pop", "ged_per_greater_than_25_pop"]))
formula3 = "median_income~" + columns3
model3 = smf.ols(formula=formula3, data=integrated).fit()
rsquared_3 = model3.rsquared

# Bachelor's or greater
columns4 = "+".join(integrated.columns.difference(["name", "cbsa_code", "median_income", "Postsecondary_Schools_per_total_pop", "Public_Schools_per_total_pop", "hs_diploma_per_greater_than_25_pop", "ged_per_greater_than_25_pop", "associates_per_greater_than_25_pop"]))
formula4 = "median_income~" + columns4
model4 = smf.ols(formula=formula4, data=integrated).fit()
rsquared_4 = model4.rsquared

# Removing some collinear features (HS, GED, Assoc., Bach.)
model5 = smf.ols(formula="median_income~hs_diploma_per_greater_than_25_pop+ged_per_greater_than_25_pop+associates_per_greater_than_25_pop+bachelors_per_greater_than_25_pop", data=integrated).fit()
rsquared_5 = model5.rsquared

# Removed collinear features + schools in area (HS, GED, Assoc., Bach., postsecondary_schools, public_schools)
model6 = smf.ols(formula="median_income~hs_diploma_per_greater_than_25_pop+ged_per_greater_than_25_pop+associates_per_greater_than_25_pop+bachelors_per_greater_than_25_pop+Postsecondary_Schools_per_total_pop+Public_Schools_per_total_pop", data=integrated).fit()
rsquared_6 = model6.rsquared

# Schools per Population Only
model7 = smf.ols(formula="median_income~Postsecondary_Schools_per_total_pop+Public_Schools_per_total_pop", data=integrated).fit()
rsquared_7 = model7.rsquared

with open("./analysis/r_squared_values.txt", "w") as f:
    hello = (
    f"R^2 values for various models:"
    f"\nFull Model: {rsquared_1.astype(float)}"
    f"\nEducational Attainment Only: {rsquared_2.astype(float)}"
    f"\nEducational Attainment, Greater than High School (or equivalent): {rsquared_3.astype(float)}"
    f"\nEducational Attainment, Bachelor's or Greater: {rsquared_4.astype(float)}"
    f"\nHigh School, GED, Associate's, or Bachelor's Only: {rsquared_5.astype(float)}"
    f"\nAbove Model + Schools per Population Data Added: {rsquared_6.astype(float)}"
    f"\nSchools per Population Only: {rsquared_7.astype(float)}"
    )
    f.write(hello)