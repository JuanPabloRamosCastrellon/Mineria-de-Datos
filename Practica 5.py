import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Define the imputer strategy (e.g., fill missing values with the mean)
imputer = SimpleImputer(strategy='mean')

# Apply the imputer to X
X_imputed = imputer.fit_transform(df[['TotalValue']])

# Ensure y does not have missing values
y_imputed = df['SalePrice'].dropna()

X = pd.DataFrame(X_imputed, columns=['TotalValue'])
y = y_imputed

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)

print(f"R2 score: {r2}")

# Scatter plot of the actual values vs. predicted values (test set)
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual SalePrice')
plt.scatter(X_test, y_pred, color='red', label='Predicted SalePrice', alpha=0.6)
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Regression Line')
plt.title('Linear Regression: SalePrice vs TotalValue')
plt.xlabel('TotalValue')
plt.ylabel('SalePrice')
plt.legend()
plt.show()

# Residual plot (difference between actual and predicted values)
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.residplot(x=X_test.values.flatten(), y=residuals, lowess=True, color="purple")
plt.title('Residual Plot')
plt.xlabel('TotalValue')
plt.ylabel('Residuals (Actual - Predicted)')
plt.axhline(0, color='black', linestyle='--')
plt.show()

# Distribution plot of residuals to check for normality
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='orange')
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()
