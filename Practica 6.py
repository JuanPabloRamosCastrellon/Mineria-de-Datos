import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
import numpy as np

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Imputing missing values with the mean
imputer = SimpleImputer(strategy='mean')

# Apply the imputer to X
X_imputed = imputer.fit_transform(df[['TotalValue']])

# Ensure y does not have missing values
y_imputed = df['SalePrice'].dropna()

X = pd.DataFrame(X_imputed, columns=['TotalValue'])
y = y_imputed

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the KNN model with k = 10
knn_model = KNeighborsRegressor(n_neighbors=10)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

r2_knn = r2_score(y_test, y_pred_knn)
print(f"KNN R2 score: {r2_knn}")

# Display predicted vs actual values
print("\nActual vs Predicted SalePrice:")
for actual, predicted in zip(y_test.head(10), y_pred_knn[:10]):
    print(f"Actual: {actual:.2f}, Predicted: {predicted:.2f}")
