import numpy as np
import matplotlib.pyplot as plt


def provjera(kvadrat,redovi,stupci):
    black = np.zeros((kvadrat,kvadrat))
    white = np.ones((kvadrat,kvadrat))*255
    red1 = np.hstack([black,white]*(stupci//2))
    
    if stupci % 2 != 0:
        red1 = np.hstack([red1,black])
    
    red2 = np.hstack([white,black]*(stupci//2))
    if stupci % 2 != 0:
        red2 = np.hstack([red2, white])

    polje = np.vstack([red1,red2] * (redovi//2))
    if redovi % 2 != 0:
        polje = np.vstack([polje,red1])
    return polje

img = provjera(50,4,5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()