import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('cars_processed.csv')

# ukupan broj automobila
print("Ukupan broj automobila:", len(df))

# tip stupca u datasetu
print("\nTipovi podataka po stupcima:\n", df.dtypes)

# najveca i najmanja cijena
df_sorted = df.sort_values(by="selling_price")
print("\nAutomobil s najmanjom cijenom:\n", df_sorted.head(1))
print("\nAutomobil s najvećom cijenom:\n", df_sorted.tail(1))

# automobili iz 2012 godine
num_2012 = df['year'].value_counts().get(2012, 0)
print("\nBroj automobila proizvedenih 2012. godine:", num_2012)

# najveca i najmanja kilometraza
df_km_sorted = df.sort_values(by='km_driven')
print("\nAutomobil s najmanje kilometara:\n", df_km_sorted.head(1))
print("\nAutomobil s najviše kilometara:\n", df_km_sorted.tail(1))

# najcesci broj sjedala kod automobila
print("\nNajčešći broj sjedala:", df['seats'].mode()[0])

#prosjecna kilometraza za dizelase i petrolheads
avg_km_diesel = df[df['fuel'] == 'Diesel']['km_driven'].mean()
avg_km_petrol = df[df['fuel'] == 'Petrol']['km_driven'].mean()
print("\nProsječna km za Diesel:", avg_km_diesel)
print("Prosječna km za Petrol:", avg_km_petrol)

# prikaz
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')

# countplot za sve stupce
df_cleaned = df.drop(['name', 'mileage'], axis=1, errors='ignore')
obj_cols = df_cleaned.select_dtypes('object').columns.tolist()

plt.figure(figsize=(15, 10))
for i, col in enumerate(obj_cols):
    plt.subplot(2, 2, i+1)
    sns.countplot(x=col, data=df_cleaned)
    plt.xticks(rotation=45)

#boxplot i histogram
df.boxplot(by='fuel', column=['selling_price'], grid=False)
df.hist(['selling_price'], grid=False)

#heatmap korelacije
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', linewidths=0.5)

plt.tight_layout()
plt.show()
