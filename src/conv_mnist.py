# Adapted from Géron
"""

Author: <Braydon King>
I was able to get the same level of performance by reducing the size of each layer by two and changing the activation
functions. In order to get the same level of performance on the test set I had to train it for double the amount of
epochs. The program takes about 2-5 minutes to run depending on the machine.

"""

import tensorflow as tf

# Load the data
mnist = tf.keras.datasets.mnist.load_data()
(X_train_full, y_train_full), (X_test, y_test) = mnist
X_train, y_train = X_train_full[:-5000], y_train_full[:-5000]
X_valid, y_valid = X_train_full[-5000:], y_train_full[-5000:]
X_train, X_valid, X_test = X_train / 255., X_valid / 255., X_test / 255.

# Set the random number seed
tf.random.set_seed(42)

#Define convolutional neural network
model = tf.keras.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=[28, 28, 1]))
model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='linear', kernel_initializer='he_uniform'))
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='selu', kernel_initializer='he_uniform'))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(10, activation="softmax"))

# Compile the model
model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_valid, y_valid))

# Evaluate the model on test data
model.evaluate(X_test, y_test)

# Plot the learning curve
import matplotlib.pyplot as plt
import pandas as pd

pd.DataFrame(history.history).plot(
    figsize=(8, 5), xlim=[0, 29], ylim=[0, 1], grid=True, xlabel="Epoch",
    style=["r--", "r--.", "b-", "b-*"])
plt.legend(loc="lower left")  # extra code
plt.show()
