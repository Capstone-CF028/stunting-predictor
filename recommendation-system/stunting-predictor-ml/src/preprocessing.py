import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/dataset capstone.csv")
print(df.head())

#melihat statistik deskriptif data
print("Statistika Deskriptif")
print(df.describe())

#melihat informasi dataset
print("Informasi Data")
print(df.info())

#melihat data duplikat
duplicate = df.duplicated().sum()
print(f"Duplikasi Data: {duplicate}")

#melihat missing value dataset
missing_value = df.isnull().sum()
print("Missing Value")
print(missing_value)

#melihat distribusi fitur numerik
num_features = df.select_dtypes(include=[np.number])
plt.figure(figsize=(14,10))
for i, column in enumerate(num_features.columns,1):
    plt.subplot(3,4,i)
    sns.histplot(df[column], bins=30, kde=True, color='blue')
    plt.title(f'Distribusi{column}')
plt.tight_layout()
plt.show()

#melihat distribusi fitur kategorikal
cat_features = df.select_dtypes(include=[object])
plt.figure(figsize=(14,10))
for i, column in enumerate(cat_features.columns,1):
    plt.subplot(3,4,i)
    sns.countplot(y=df[column], palette='viridis')
    plt.title(f'Distribusi{column}')
plt.tight_layout()
plt.show()

#melihat korelasi antar fitur
plt.figure(figsize=(12,10))
correlation_matrix = num_features.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap Korelasi')
plt.show()

#menghapus data duplikat 
df = df.drop_duplicates()
duplicate = df.duplicated().sum()
print(f'Jumlah data duplikat : {duplicate}')
