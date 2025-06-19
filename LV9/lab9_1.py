import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.preprocessing import image
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

batch_size = 32
img_size = (48, 48)


train_ds = tf.keras.preprocessing.image_dataset_from_directory(
     'dataset/Train',
    labels='inferred',
    label_mode='categorical',
    image_size=img_size,
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=123
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'dataset/Train',
    labels='inferred',
    label_mode='categorical',
    image_size=img_size,
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=123
)

test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'dataset/Test',
    labels='inferred',
    label_mode='categorical',
    image_size=img_size,
    batch_size=batch_size
)


model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(43, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
checkpoint_cb = ModelCheckpoint('best_model.h5', save_best_only=True)
tensorboard_cb = TensorBoard(log_dir=log_dir, histogram_freq=1)


model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=3,
    callbacks=[checkpoint_cb, tensorboard_cb]
)




model.load_weights('best_model.h5')
loss, acc = model.evaluate(test_ds)
print(f"[testna tocnost: {acc:.2f}")
y_true = np.concatenate([y for x, y in test_ds], axis=0)
y_pred_probs = model.predict(test_ds)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true_labels = np.argmax(y_true, axis=1)

cm = confusion_matrix(y_true_labels, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title("Matrica zabune")
plt.show()


try:
    img_path = 'my_sign.jpg'
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
     
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    print(f"Predvidjena klasa: {predicted_class}")
except FileNotFoundError:
    print("slika nije pronadjena.")
plt.show('my_sign.jpg')