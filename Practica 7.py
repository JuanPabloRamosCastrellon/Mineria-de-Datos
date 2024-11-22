import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score

file_path = 'C:/Users/Juan Pablo/Desktop/Mineria-de-Datos/Nashville Housing Data.xlsx'

spreadsheet = pd.ExcelFile(file_path)
spreadsheet.sheet_names
df = pd.read_excel(file_path, sheet_name='Sheet1')
# df.info(), df.head()

# Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')

X_imputed = imputer.fit_transform(df[['TotalValue', 'Acreage']])

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Define the number of clusters
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)

kmeans.fit(X_scaled)
labels = kmeans.labels_

# Inertia, sum of squared distances to the nearest cluster center
inertia = kmeans.inertia_
print(f"Inertia (Sum of squared distances to nearest cluster center): {inertia}")

# Silhouette score: similarity in points in the same cluster, compared to other clusters
silhouette_avg = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {silhouette_avg}")

# DataFrame with original data and assigned clusters
df_clusters = pd.DataFrame(X_imputed, columns=['TotalValue', 'Acreage'])
df_clusters['Cluster'] = labels

plt.figure(figsize=(8, 6))
sns.scatterplot(x='TotalValue', y='Acreage', hue='Cluster', data=df_clusters, palette='Set2')
plt.title('K-means Clustering of TotalValue and Acreage')
plt.xlabel('TotalValue')
plt.ylabel('Acreage')
plt.legend(title='Cluster')
plt.show()