import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img= img[:,:,0].copy()
print("Dimenzije slike:",img.shape)
svijetla = np.clip(img * 1.5, 0, 1)  
rotirana = np.root90(img,-1)
zrcalo=np.fliplr(img)
res=img[::10,::10]

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
