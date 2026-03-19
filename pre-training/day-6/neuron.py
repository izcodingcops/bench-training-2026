import math


class Neuron:
    def __init__(self, weights, bias, activation):
        self.weights = weights
        self.bias = bias
        self.activation = activation

    def forward_pass(self, inputs):
        output = 0
        for weight, input in zip(self.weights, inputs):
            output += weight * input

        output += self.bias
        return self._activate(output)

    def _activate(self, z):
        if self.activation == 'sigmoid':
            return Neuron._sigmoid(z)
        elif self.activation == 'relu':
            return Neuron._relu(z)
        return None

    @staticmethod
    def _relu(z):
        return max(0, z)

    @staticmethod
    def _sigmoid(z):
        return 1 / (1 + math.exp(-z))


class DenseLayer:
    def __init__(self, n_inputs, n_neurons, activation):
        self.neurons = []
        weights = [0.5] * n_inputs
        bias = 0

        for _ in range(n_neurons):
            self.neurons.append(Neuron(weights, bias, activation))

    def forward_pass(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.forward_pass(inputs))

        return outputs


layer1 = DenseLayer(3, 4, 'relu')
layer2 = DenseLayer(4, 2, 'sigmoid')

x = [0.5, -0.3, 0.8]

layer1_output = layer1.forward_pass(x)
layer2_output = layer2.forward_pass(layer1_output)

print(layer2_output)
