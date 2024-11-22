import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Columns for different plots
categorical_columns = ['Bedrooms', 'FullBath', 'HalfBath']
numeric_columns = ['SalePrice', 'TotalValue', 'Acreage', 'YearBuilt']

plt.figure(figsize=(15, 15))

# Pie charts for categorical columns
for column in categorical_columns:
    plt.figure()
    data = df[column].value_counts()
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Pie chart of {column}')
    plt.show()

# Histograms for numeric columns
for column in numeric_columns[:2]:
    plt.figure() 
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()

# Boxplot of SalePrice and TotalValue
plt.figure()
sns.boxplot(data=df[['SalePrice', 'TotalValue']])
plt.title('Boxplot of SalePrice and TotalValue')
plt.show()

# Scatter Plot for SalePrice vs TotalValue
plt.figure()
plt.scatter(df['SalePrice'], df['TotalValue'], alpha=0.5)
plt.title('Scatter plot of SalePrice vs TotalValue')
plt.xlabel('SalePrice')
plt.ylabel('TotalValue')
plt.show()

# Line Plot of YearBuilt vs SalePrice
plt.figure()
df_sorted = df.sort_values(by='YearBuilt')
plt.plot(df_sorted['YearBuilt'], df_sorted['SalePrice'])
plt.title('Line plot of SalePrice over YearBuilt')
plt.xlabel('YearBuilt')
plt.ylabel('SalePrice')
plt.show()
