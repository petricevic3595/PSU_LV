import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

#ucitavanje podataka
df = pd.read_csv('cars_processed.csv')

# izbacivanje viska
df = df.drop(columns=['name'])

#ulazne i izlazne varijable
X = df[['km_driven', 'year', 'engine', 'max_power']]
y = df['selling_price']

#podjela na trening i test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#treniranje modela
model = LinearRegression()
model.fit(X_train_scaled, y_train)

#pretpostavka
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)


print("Evaluacija modela:")
print(f"R2 (Train): {r2_score(y_train, y_train_pred):.4f}")
print(f"R2 (Test): {r2_score(y_test, y_test_pred):.4f}")
print(f"RMSE (Test): {np.sqrt(mean_squared_error(y_test, y_test_pred)):.4f}")
print(f"MAE (Test): {mean_absolute_error(y_test, y_test_pred):.4f}")
print(f"Max error (Test): {max_error(y_test, y_test_pred):.4f}")

#plot show
plt.figure(figsize=(10, 6))
sns.regplot(x=y_test_pred, y=y_test, line_kws={"color": "red"})
plt.xlabel("Predicted Price")
plt.ylabel("Actual Price")
plt.title("Stvarna vs Predviđena cijena automobila (Test skup)")
plt.grid(True)
plt.show()

#ulazne varijable i utjecaj
feature_sets = [
    ['km_driven', 'year'],
    ['km_driven', 'year', 'engine'],
    ['km_driven', 'year', 'engine', 'max_power']
]

for features in feature_sets:
    X_train_fs = X_train[features]
    X_test_fs = X_test[features]
    
    X_train_fs_scaled = scaler.fit_transform(X_train_fs)
    X_test_fs_scaled = scaler.transform(X_test_fs)
    
    model.fit(X_train_fs_scaled, y_train)
    y_test_fs_pred = model.predict(X_test_fs_scaled)
    
    print(f"\nEvaluacija za ulazne veličine: {features}")
    print(f"R2 (Test): {r2_score(y_test, y_test_fs_pred):.4f}")
    print(f"RMSE (Test): {np.sqrt(mean_squared_error(y_test, y_test_fs_pred)):.4f}")
    print(f"MAE (Test): {mean_absolute_error(y_test, y_test_fs_pred):.4f}")
