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

vrijednosti_kriterijske_funkcije = []
brojevi_klastera = range(1, 21)

for k in brojevi_klastera:
    model = KMeans(n_clusters=k, random_state=0)
    model.fit(ulazni_podaci)
    vrijednosti_kriterijske_funkcije.append(model.inertia_)

plt.figure(figsize=(7, 5))
plt.plot(brojevi_klastera, vrijednosti_kriterijske_funkcije, marker='o')
plt.title("elbow metoda (KMeans)")
plt.xlabel("broj klastera")
plt.ylabel("kriterijska funkcija")
plt.grid(True)
plt.show()

# sto je veci broj klastera to je manja vrijednost kriterijske funkcije
# nakon nekog odredenog broja promjene se vide manje
