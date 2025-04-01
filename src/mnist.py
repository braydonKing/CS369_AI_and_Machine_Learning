"""
Author: <Braydon King>

I was able to get about the same performance of ~98% with 100 fewer neurons. I did this by dividing the initial layer of
neurons in half then added another layer of 50 neurons that used the "tanh" activation function. The final layer of
nuerons remained the exact same, leaving us with a total Number of 210 Neurons.
"""

import tensorflow as tf

mnist = tf.keras.datasets.mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]

X_train, X_valid, X_test = X_train / 255., X_valid / 255., X_test / 255.

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

tf.random.set_seed(42)
model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28]))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(150, activation="relu"))
model.add(tf.keras.layers.Dense(50, activation="tanh"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.summary()

hidden1 = model.layers[1]

weights, biases = hidden1.get_weights()


model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))

