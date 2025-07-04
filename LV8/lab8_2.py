import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

# Ucitaj sliku
img_original = mpimg.imread('test.png')  # Zamijeni 'test.png' s putanjom do svoje slike
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))

# Prikazi sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()

# Pripremi sliku - ulaz u mrezu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# TODO: ucitaj izgradenu mrezu
model_ucitani = models.load_model('najbolji_model.h5')

# TODO: napravi predikciju za ucitanu sliku pomocu mreze
pretpostavka = model_ucitani.predict(img)
klasa = np.argmax(pretpostavka)

# TODO: ispis rezultat u terminal
print(f'Mreža pretpostavlja da se na slici nalazi znamenka: {klasa}')
