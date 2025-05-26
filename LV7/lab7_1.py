import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

(trn_x, trn_y), (tst_x, tst_y) = keras.datasets.mnist.load_data()


for i in range(3, 8):
    plt.imshow(trn_x[i], cmap='gray')
    plt.title(f"Znak: {trn_y[i]}")
    plt.axis('off')
    plt.show()


trn_x = trn_x.astype("float32") / 255
tst_x = tst_x.astype("float32") / 255

trn_x = trn_x.reshape(-1, 784)
tst_x = tst_x.reshape(-1, 784)

trn_y_ohe = keras.utils.to_categorical(trn_y, 10)
tst_y_ohe = keras.utils.to_categorical(tst_y, 10)


mreža = Sequential()
mreža.add(Dense(64, activation='relu', input_shape=(784,)))
mreža.add(Dense(10, activation='softmax'))

mreža.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])


rez = mreža.fit(trn_x, trn_y_ohe, epochs=5, batch_size=32, verbose=0)


trn_eval = mreža.evaluate(trn_x, trn_y_ohe, verbose=0)
tst_eval = mreža.evaluate(tst_x, tst_y_ohe, verbose=0)
print(f"Točnost učenja: {trn_eval[1]:.2f}")
print(f"Točnost testiranja: {tst_eval[1]:.2f}")


pred_y = mreža.predict(tst_x)
pred_kl = np.argmax(pred_y, axis=1)

mat_zab = confusion_matrix(tst_y, pred_kl)
ConfusionMatrixDisplay(mat_zab, display_labels=range(10)).plot()
plt.show()

netoč = np.where(tst_y != pred_kl)[0]
for i in range(5):
    idx = netoč[i]
    plt.imshow(tst_x[idx].reshape(28, 28), cmap='gray')
    plt.title(f"Točno: {tst_y[idx]}, Pogrešno: {pred_kl[idx]}")
    plt.axis('off')
    plt.show()
