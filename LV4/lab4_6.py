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
print("Prvih 5 redaka podataka:")
print(df.head())

# izbacivanje viska
df = df.drop(columns=['name'])
print("Preostale kolone nakon izbacivanja nepotrebnih veličina:")
print(df.columns)

# kategoricne varijable
df = pd.get_dummies(df, columns=['fuel', 'seller_type', 'transmission', 'owner'], drop_first=True)

#ulazne i izlazne varijable
X = df.drop(columns=['selling_price'])
y = df['selling_price']

#podjela na trening i test
X_tren, X_test, y_tren, y_test = train_test_split(X, y, test_size=0.2, random_state=300)


skaliraj = StandardScaler()
X_tren_s = skaliraj.fit_transform(X_tren)
X_test_s = skaliraj.transform(X_test)

#treniranje modela
model = LinearRegression()
model.fit(X_tren_s, y_tren)


#pretpostavka
y_pred_tren = model.predict(X_tren_s)
y_pred_test = model.predict(X_test_s)


print("--- Rezultati evaluacije s kategoričkim varijablama ---")
print("R2 (Trening):", r2_score(y_tren, y_pred_tren))
print("R2 (Test):", r2_score(y_test, y_pred_test))
print("RMSE (Test):", np.sqrt(mean_squared_error(y_test, y_pred_test)))
print("MAE (Test):", mean_absolute_error(y_test, y_pred_test))
print("Maksimalna pogreška (Test):", max_error(y_test, y_pred_test))

#plot show
plt.figure(figsize=[13, 10])
graf = sns.regplot(x=y_pred_test, y=y_test, line_kws={'color': 'green'})
graf.set(xlabel='Predviđena cijena', ylabel='Stvarna cijena', title='Model s kategoričkim varijablama')
plt.show()
