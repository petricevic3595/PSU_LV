import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

def generiraj_skup_podataka(broj_uzoraka, nacin):
    if nacin == 1:
        stanje = 365
        podaci, _ = datasets.make_blobs(n_samples=broj_uzoraka, random_state=stanje)
    elif nacin == 2:
        stanje = 148
        podaci, _ = datasets.make_blobs(n_samples=broj_uzoraka, random_state=stanje)
        matrica = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        podaci = np.dot(podaci, matrica)
    elif nacin == 3:
        stanje = 148
        podaci, _ = datasets.make_blobs(n_samples=broj_uzoraka, centers=4,
                                        cluster_std=[1.0, 2.5, 0.5, 3.0], random_state=stanje)
    elif nacin == 4:
        podaci, _ = datasets.make_circles(n_samples=broj_uzoraka, factor=0.5, noise=0.05)
    elif nacin == 5:
        podaci, _ = datasets.make_moons(n_samples=broj_uzoraka, noise=0.05)
    else:
        podaci = np.array([])
    return podaci

# generiranje 500 podataka
ulazni_podaci = generiraj_skup_podataka(500, nacin=4)

# prikaz podataka
plt.figure(figsize=(6, 5))
plt.scatter(ulazni_podaci[:, 0], ulazni_podaci[:, 1], s=15)
plt.title("Vizualizacija generiranih podataka")
plt.xlabel("Značajka 1")
plt.ylabel("Značajka 2")
plt.grid(True)
plt.show()

# KMeans algoritam
broj_klastera = 3
kmeans_model = KMeans(n_clusters=broj_klastera, random_state=0)
pripadnosti = kmeans_model.fit_predict(ulazni_podaci)
sredisnje_tocke = kmeans_model.cluster_centers_


plt.figure(figsize=(6, 5))
plt.scatter(ulazni_podaci[:, 0], ulazni_podaci[:, 1], c=pripadnosti, s=15, cmap='viridis')
plt.scatter(sredisnje_tocke[:, 0], sredisnje_tocke[:, 1], c='black', s=180, marker='X', label='Centri klastera')
plt.title("Rezultat grupiranja pomoću KMeans algoritma")
plt.xlabel("Značajka 1")
plt.ylabel("Značajka 2")
plt.legend()
plt.grid(True)
plt.show()

# ako promjenimo nacin na koji se generiraju podaci dobijemo drugi oblik na grafu
