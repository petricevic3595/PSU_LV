import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

ulazna_slika = mpimg.imread('example.png')

if ulazna_slika.max() <= 1.0:
    ulazna_slika = (ulazna_slika * 255).astype(np.uint8)

slika_2d = ulazna_slika.reshape(-1, 3)

broj_klastera = 10
model_kmeans = KMeans(n_clusters=broj_klastera, n_init=1, random_state=42)
model_kmeans.fit(slika_2d)


centri_boje = model_kmeans.cluster_centers_.astype(np.uint8)
etikete = model_kmeans.labels_
kvantizirana_slika = centri_boje[etikete].reshape(ulazna_slika.shape)


plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(ulazna_slika)
plt.title("Izvorna slika")

plt.subplot(1, 2, 2)
plt.imshow(kvantizirana_slika)
plt.title(f"Kvantizirana slika (k={broj_klastera})")

plt.show()

# kvantizacijom se slika pojednostavljuje korištenjem manje boja
