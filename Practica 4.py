from scipy import stats
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

alpha = 0.05

# Test if the mean SalePrice is different from a hypothesized population mean. In this case, 250000
population_mean = 250000

# One-sample t-test
t_stat, p_value = stats.ttest_1samp(df['SalePrice'].dropna(), population_mean)

# Check if null hypothesis is rejected
print("One-Sample T-Test")
print(f"T-statistic: {t_stat}, P-value: {p_value}")
if p_value < alpha:
    print(f"Conclusion: The null hypothesis is rejected (P-value < {alpha}).\n"
          f"The mean SalePrice is significantly different from the population mean of {population_mean}.")
else:
    print(f"Conclusion: The null hypothesis is NOT rejected (P-value >= {alpha}).\n"
          f"The mean SalePrice is not significantly different from the population mean of {population_mean}.")
print("\n")

# Shapiro-Wilk test for normality on SalePrice
shapiro_stat, shapiro_p_value = stats.shapiro(df['SalePrice'].dropna())

# Check if null hypothesis is rejected
print("Shapiro-Wilk Test for Normality")
print(f"Statistic: {shapiro_stat}, P-value: {shapiro_p_value}")
if shapiro_p_value < alpha:
    print(f"Conclusion: The null hypothesis of normality is rejected (P-value < {alpha}).\n"
          "The data is not normally distributed.")
else:
    print(f"Conclusion: The null hypothesis of normality is NOT rejected (P-value >= {alpha}).\n"
          "The data is normally distributed.")
print("\n")

# Levene’s test for homogeneity of variances for SalePrice across Bedrooms groups
levene_stat, levene_p_value = stats.levene(
    df[df['Bedrooms'] == 1]['SalePrice'].dropna(),
    df[df['Bedrooms'] == 2]['SalePrice'].dropna(),
    df[df['Bedrooms'] == 3]['SalePrice'].dropna(),
    df[df['Bedrooms'] == 4]['SalePrice'].dropna()
)

# Check if null hypothesis is rejected
print("Levene's Test for Homogeneity of Variances")
print(f"Statistic: {levene_stat}, P-value: {levene_p_value}")
if levene_p_value < alpha:
    print(f"Conclusion: The null hypothesis of equal variances is rejected (P-value < {alpha}).\n"
          "The variances are not equal across groups.")
else:
    print(f"Conclusion: The null hypothesis of equal variances is NOT rejected (P-value >= {alpha}).\n"
          "The variances are equal across groups.")
print("\n")

# One-way ANOVA for SalePrice across different Bedrooms groups
anova_model = ols('SalePrice ~ C(Bedrooms)', data=df).fit()
anova_table = sm.stats.anova_lm(anova_model, typ=2)
p_value_anova = anova_table['PR(>F)'][0]
print("One-Way ANOVA Test")
print(anova_table)

# Check if null hypothesis is rejected
if p_value_anova < alpha:
    print(f"Conclusion: The null hypothesis is rejected (P-value < {alpha}).\n"
          "There is a significant difference in SalePrice means across different Bedroom groups.")
else:
    print(f"Conclusion: The null hypothesis is NOT rejected (P-value >= {alpha}).\n"
          "There is no significant difference in SalePrice means across different Bedroom groups.")
