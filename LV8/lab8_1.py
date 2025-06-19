from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# TODO: strukturiraj konvolucijsku neuronsku mrezu
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# TODO: definiraj callbacks
pozivi = [
    callbacks.TensorBoard(log_dir='dnevnik', update_freq=100),
    callbacks.ModelCheckpoint(filepath='najbolji_model.h5',
                              monitor='val_accuracy',
                              save_best_only=True,
                              mode='max')
]

# TODO: provedi treniranje mreze pomocu .fit()
model.fit(x_train_s, y_train_s,
          epochs=10,
          batch_size=64,
          validation_split=0.1,
          callbacks=pozivi)

#TODO: Ucitaj najbolji model
ucitana_mreza = keras.models.load_model('najbolji_model.h5')

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
gubitak_ucenje, tocnost_ucenje = ucitana_mreza.evaluate(x_train_s, y_train_s, verbose=0)
gubitak_test, tocnost_test = ucitana_mreza.evaluate(x_test_s, y_test_s, verbose=0)
print(f'Točnost na skupu za učenje: {tocnost_ucenje:.4f}')
print(f'Točnost na testnom skupu: {tocnost_test:.4f}')

# TODO: Prikazite matricu zabune na skupu podataka za testiranje
predikcije = ucitana_mreza.predict(x_test_s)
pred_klase = np.argmax(predikcije, axis=1)
stvarne_klase = np.argmax(y_test_s, axis=1)

matrica = confusion_matrix(stvarne_klase, pred_klase)
print("Matrica zabune (testni skup):")
print(matrica)
