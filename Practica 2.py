import pandas as pd
import numpy as np
from scipy import stats

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Mean, median, and mode for SalePrice and TotalValue
saleprice_mean = df['SalePrice'].mean()
saleprice_median = df['SalePrice'].median()
saleprice_mode_result = stats.mode(df['SalePrice'], nan_policy='omit')[0]
if isinstance(saleprice_mode_result, np.ndarray):
    saleprice_mode = saleprice_mode_result[0] if saleprice_mode_result.size > 0 else None
else:
    saleprice_mode = saleprice_mode_result

totalvalue_mean = df['TotalValue'].mean()
totalvalue_median = df['TotalValue'].median()
totalvalue_mode_result = stats.mode(df['TotalValue'], nan_policy='omit')[0]
if isinstance(totalvalue_mode_result, np.ndarray):
    totalvalue_mode = totalvalue_mode_result[0] if totalvalue_mode_result.size > 0 else None
else:
    totalvalue_mode = totalvalue_mode_result

# Range of YearBuilt
yearbuilt_range = df['YearBuilt'].max() - df['YearBuilt'].min()

# Variance and standard deviation of Acreage and TotalValue
acreage_variance = df['Acreage'].var()
acreage_std_dev = df['Acreage'].std()

totalvalue_variance = df['TotalValue'].var()
totalvalue_std_dev = df['TotalValue'].std()

# Mode of Bedrooms, FullBath, and HalfBath
bedrooms_mode_result = stats.mode(df['Bedrooms'], nan_policy='omit')[0]
if isinstance(bedrooms_mode_result, np.ndarray):
    bedrooms_mode = bedrooms_mode_result[0] if bedrooms_mode_result.size > 0 else None
else:
    bedrooms_mode = bedrooms_mode_result

fullbath_mode_result = stats.mode(df['FullBath'], nan_policy='omit')[0]
if isinstance(fullbath_mode_result, np.ndarray):
    fullbath_mode = fullbath_mode_result[0] if fullbath_mode_result.size > 0 else None
else:
    fullbath_mode = fullbath_mode_result

halfbath_mode_result = stats.mode(df['HalfBath'], nan_policy='omit')[0]
if isinstance(halfbath_mode_result, np.ndarray):
    halfbath_mode = halfbath_mode_result[0] if halfbath_mode_result.size > 0 else None
else:
    halfbath_mode = halfbath_mode_result

print(f"SalePrice Mean: {saleprice_mean}")
print(f"SalePrice Median: {saleprice_median}")
print(f"SalePrice Mode: {saleprice_mode}")
print(f"TotalValue Mean: {totalvalue_mean}")
print(f"TotalValue Median: {totalvalue_median}")
print(f"TotalValue Mode: {totalvalue_mode}")
print(f"YearBuilt Range: {yearbuilt_range}")
print(f"Acreage Variance: {acreage_variance}")
print(f"Acreage Standard Deviation: {acreage_std_dev}")
print(f"TotalValue Variance: {totalvalue_variance}")
print(f"TotalValue Standard Deviation: {totalvalue_std_dev}")
print(f"Bedrooms Mode: {bedrooms_mode}")
print(f"FullBath Mode: {fullbath_mode}")
print(f"HalfBath Mode: {halfbath_mode}")
