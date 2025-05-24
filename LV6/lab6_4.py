import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans


slika = mpimg.imread('example_grayscale.png')


if len(slika.shape) == 2:
    slika = np.stack([slika] * 3, axis=-1)



ulazni_podaci = slika.reshape(-1, 3)


broj_klastera = 10


kmeans_model = KMeans(n_clusters=broj_klastera, n_init=1, random_state=0)
kmeans_model.fit(ulazni_podaci)


boje = kmeans_model.cluster_centers_.astype('uint8')
oznake = kmeans_model.labels_
kvantizirana_slika = boje[oznake].reshape(slika.shape)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(slika)
plt.title("Izvorna slika")

plt.subplot(1, 2, 2)
plt.imshow(kvantizirana_slika)
plt.title(f"Kvantizacija slike (k = {broj_klastera})")
plt.tight_layout()
plt.show()

velicina_originala = slika.size * slika.itemsize
velicina_kvantizirane = broj_klastera * ulazni_podaci.shape[0] * ulazni_podaci.itemsize
kompresija = velicina_originala / velicina_kvantizirane


print(f" kompresija s {broj_klastera} klastera: {kompresija:.2f}x")

# povećanjem broja klastera, kvantizirana slika postaje vizualno
# sličnija originalu, ali se smanjuje postignuta kompresija.

