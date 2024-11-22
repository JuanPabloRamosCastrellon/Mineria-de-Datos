import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Ensure data is ordered by time
# YearBuilt is the time feature, SalePrice is target variable
df_sorted = df[['YearBuilt', 'SalePrice']].dropna().sort_values(by='YearBuilt')

X = df_sorted[['YearBuilt']]
y = df_sorted['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R2 score: {r2}")
print(f"Mean Absolute Error: {mae}")

# Visualize predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title('Linear Regression: Predicted vs Actual SalePrice')
plt.xlabel('YearBuilt')
plt.ylabel('SalePrice')
plt.legend()
plt.show()

# Forecast future values for 2025, 2026, 2027, 2028, 2029, and 2030
future_years = np.array([[2025], [2026], [2027], [2028], [2029], [2030]])
future_predictions = model.predict(future_years)

print("\nFuture Predictions:")
for year, price in zip(future_years.flatten(), future_predictions):
    print(f"Year: {year}, Predicted SalePrice: ${price:.2f}")