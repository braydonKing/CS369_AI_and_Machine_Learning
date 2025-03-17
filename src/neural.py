
"""Authors: <Stas Ivanov>, <Braydon King>
"""

import math
import random
import matplotlib.pyplot as plt


LEARNING_RATE = 1


class InputNeuron:

    def __init__(self, activation=1):
        self.activation = activation
        self.delta = 0


class OutputNeuron:

    def __init__(self, previous_layer):
        self.activation = None
        self.delta = None
        self.previous_layer = [InputNeuron()] + previous_layer  # Add bias node
        self.weights = [random.gauss(0, 1) for _ in self.previous_layer]

    def update_activation(self):
        """
        Update the activation of this neuron, based on its previous layer and weights.
        """
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)

    def update_delta(self, target): #completed!
        """
        Update the delta value for this neuron. Also, backpropagate delta values to neurons in
        the previous layer.
        :param target: The desired output of this neuron.
        """
        a = self.activation
        t = target
        self.delta = -a * (1 - a) * (t - a)
        for unit, weight in zip(self.previous_layer[1:], self.weights[1:]):
            unit.delta += self.delta*weight #Computes the Sigma portion of the equation

    def update_weights(self):
        """
        Update the weights of this neuron.
        """
        for j in range(len(self.previous_layer)):
            self.weights[j] += -LEARNING_RATE * self.previous_layer[j].activation * self.delta


class HiddenNeuron(OutputNeuron): #completed! Did optional challenge of using inheritance instead of copy & pasting

    # You have to write this. It is almost identical to OutputNeuron, but it has a different
    # update_delta method which doesn't take target as an argument.  You can copy and paste or
    # use inheritance.
    def __init__(self, previous_layer):
        super().__init__(previous_layer)
    
    def update_delta(self):
        a = self.activation
        self.delta = a * (1 - a) * sum(n.delta * n.weights[self.index + 1] for n in self.next_layer)


class Network:

    def __init__(self, sizes):
        """
        :param sizes: A list of the number of neurons in each layer, e.g., [2, 2, 1] for a network that can learn XOR.
        """
        self.layers = [None] * len(sizes)
        self.layers[0] = [InputNeuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes) - 1):
            self.layers[i] = [HiddenNeuron(self.layers[i - 1]) for _ in range(sizes[i])]
        self.layers[-1] = [OutputNeuron(self.layers[-2]) for _ in range(sizes[-1])]
        
        # Assign next_layer references for backpropagation
        for i in range(1, len(sizes) - 1):
            for j, neuron in enumerate(self.layers[i]):
                neuron.next_layer = self.layers[i + 1]
                neuron.index = j  # Store the neuron's index for correct weight referencing


    def predict(self, inputs):
        """
        :param inputs: Values to use as activations of the input layer.
        :return: The predictions of the neurons in the output layer.
        """
        # set the input values in the first layer
        for i, val in enumerate(inputs):
            self.layers[0][i].activation = val
        
        # move forward through the network layer by layer and update activations for each neuron based on the previous layer
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_activation()
        return [neuron.activation for neuron in self.layers[-1]]


    def reset_deltas(self):
        """
        Set the deltas for all units to 0.
        """
        for layer in self.layers:
            for neuron in layer:
                neuron.delta = 0

    def update_deltas(self, targets):
        """
        Update the deltas of all neurons, using backpropagation. Assumes predict has already
        been called, so all neurons have had their activations updated.
        :param targets: The desired activations of the output neurons.
        """
        for neuron, target in zip(self.layers[-1], targets):
            neuron.update_delta(target)
        
        for layer in reversed(self.layers[1:-1]):
            for neuron in layer:
                neuron.update_delta()

    def update_weights(self):
        """
        Update the weights of all neurons.
        """
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.update_weights()

    def train(self, inputs, targets):
        """
        Feed inputs through this network, then adjust the weights so that the activations of
        the output neurons will be slightly closer to targets.
        :param inputs: A list activation values for the input units.
        :param targets: A list desired activation values for the output units.
        """
        self.predict(inputs)
        self.reset_deltas()  # Set all deltas to 0
        self.update_deltas(targets)
        self.update_weights()

    def train_with_plot(self, inputs, targets, epochs=1000):
        errors = [] # store mean squared error for each epoch
        for _ in range(epochs):
            total_error = 0
            for i, t in zip(inputs, targets):
                self.train(i, t) # train the network on each input-target pair
                predictions = self.predict(i)
                total_error += mean_squared_error(predictions, t) # total error track
            errors.append(total_error / len(inputs)) # average error
        
        # plot of the error over time
        plt.plot(errors)
        plt.xlabel('Epochs')
        plt.ylabel('Mean Squared Error')
        plt.title('Training Error Over Time')
        plt.show()


def logistic(x):
    """
    Logistic sigmoid squashing function.
    """
    return 1 / (1 + math.exp(-x))

def mean_squared_error(predictions, targets):
    # calculate how far off we are from the correct values
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(targets)

if __name__ == "__main__":
    # EXAMPLE DATASET
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]] # input values
    targets = [[0], [1], [1], [1]] # expected outputs
    
    # simple network with 2 inputs and 1 output
    net = Network([2, 1])
    
    # train the network and plot how the error changes over time
    net.train_with_plot(inputs, targets, epochs=1000)