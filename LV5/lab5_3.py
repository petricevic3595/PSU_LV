'''

b) Kad povećavamo max_depth, model postaje složeniji i bolje uči podatke,
njegova dubina se povećava

c) prilikom korištenja decision tree stablo ne koristi udaljenost između točaka te onda
skaliranje ulaznih veličina nema znatan utjecaj na rezultat




'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

podaci = pd.read_csv('occupancy_processed.csv')

X = podaci[['S3_Temp', 'S5_CO2']].values
y = podaci['Room_Occupancy_Count'].values

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

skal = StandardScaler()
x_train = skal.fit_transform(x_train)
x_test = skal.transform(x_test)

model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mat = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(mat).plot()
plt.title("Matrica zabune")
plt.show()

print("Izvještaj klasifikacije:\n")
print(classification_report(y_test, y_pred, target_names=["Slobodna", "Zauzeta"]))

plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=["Temp", "CO2"], class_names=["Slobodna", "Zauzeta"], filled=True)
plt.title("Stablo odlučivanja")
plt.show()
