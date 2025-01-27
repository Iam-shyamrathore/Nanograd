
from nanograd.core import Value
from nanograd.nn import MLP

# Example usage of NanoGrad
x1 = Value(2.0, label="x1")
x2 = Value(0.0, label="x2")
w1 = Value(-3.0, label="w1")
w2 = Value(1.0, label="w2")
b = Value(6.8813735870195432, label="b")

# Forward pass for a single neuron
n = (x1 * w1 + x2 * w2 + b).tanh()
n.backward()
print("Gradient of x1:", x1.grad)

# Multi-layer perceptron example
model = MLP(3, [4, 4, 1])
output = model([2.0, 3.0, -1.0])
print("Output of MLP:", output.data)
