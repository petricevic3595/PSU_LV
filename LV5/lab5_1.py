'''
Room occupancy classification 

R.Grbic, 2024.

1.a) Kada su temperatura i CO2 niži, prostorija je većinom slobodna,međutim kako temperatura
raste i kako raste koncentracija CO2 pretpostavlja se da je soba zauzeta što ima smisla s obzirom
da ljudi ispuštaju CO2 prilikom disanja tj izdisanja.

b) Skup sadrži 10129 primjera

c) Podaci su podjeljeni u dvije klase: zauzeta i slobodna prostorija


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ucitaj podatke za ucenje
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

# Scatter plot
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()
