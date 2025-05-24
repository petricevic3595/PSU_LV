import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.cluster.hierarchy import dendrogram, linkage

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
ulazni_podaci = generiraj_skup_podataka(500, nacin=5)

# grupiranje
hijerarhijski_model = linkage(ulazni_podaci, method='ward')

plt.figure(figsize=(10, 6))
dendrogram(hijerarhijski_model)
plt.title("Dendrogram hijerarhijskog grupiranja")
plt.xlabel("Indeksi uzoraka")
plt.ylabel("Udaljenost spajanja")
plt.grid(True)
plt.show()

# dendrogram prikazuje strukturu grupiranja, a izbor metode utječe na oblik i broj klastera.

