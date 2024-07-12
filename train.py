import keras
import numpy as np
from keras import Sequential, layers, Input, initializers, optimizers, Initializer
import visualkeras
import json
from models import model01

model = model01

num_classes = 10
input_shape = (28, 28, 1)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print(x_train.shape)
print(y_train.shape)

model.compile(loss="categorical_crossentropy", optimizer="adamw", metrics=["accuracy"])
visualkeras.layered_view(model, to_file='model01.png')
model.fit(x_train, y_train, batch_size=128, epochs=3, validation_data=(x_test, y_test), validation_batch_size=5)
model.save("models/model01.keras")

model.evaluate(x_test, y_test)