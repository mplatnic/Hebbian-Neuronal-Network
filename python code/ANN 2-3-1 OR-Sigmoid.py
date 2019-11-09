# https://iamtrask.github.io/2015/07/12/basic-python-network/
# X 	Input dataset matrix where each row is a training example
# y 	Output dataset matrix where each row is a training example
# l0 	First Layer of the Network, specified by the input data
# l1 	Second Layer of the Network, otherwise known as the hidden layer
# l3 	output Layer of the Network
# Syn0 	First layer of weights, Synapse 0, connecting l0 to l1.  (syn for synapse)
# Syn1 	Second layer of weights, Synapse 1, connecting l1 to l2 (output).
# 3 inputs, 4 hidden neurons, 1 output
# SUPERVISED neural network using non linear Sigmoid feedback
# Deep Learning
# Mattrix (4 x 3) dot (3 x 1) = (4 x 1)

# in "nonlinear" pattern there isn't a direct one-to-one relationship between the input and output.
# Instead, there is a one-to-one relationship between a combination of inputs
# we use a second layer In order to first combine pixels into something that can then have
# a one-to-one relationship with the output, we need to add another layer.
# Our first layer will combine the inputs, and our second layer will then map them to the output

import numpy as np


# sigmoid function
# this nonlinearity maps a function called a "sigmoid"
# If the sigmoid's output is a variable "out", then the derivative is simply out * (1-out)
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset for OR
# for XOR add an additional neuron in the hidden layer
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# output dataset
y = np.array([[0, 1, 1, 1]]).T  # T is for mattrix transpose

# seed random numbers to make calculation deterministic. (1) is the sequence used for random
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((2, 3)) - 1  # Mattrix of [2,3] 2 neurons to 3 neurons
syn1 = 2 * np.random.random((3, 1)) - 1  # Mattrix of [3,1] 3 neurons to 1 neuron, the output

for iter in range(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))  # l1 = nonlin (l0 x syn0), matrix-matrix multiplication
    l2 = nonlin(np.dot(l1, syn1))

    # how much did we miss?
    l2_error = y - l2
    if (iter % 1000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l2
    l2_delta = l2_error * nonlin(l2, True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    # "contribution weighted error" because we learn how much each node value in l1
    # "contributed" to the error in l2. This step is called "backpropagating" and is the namesake of the algorithm
    l1_error = l2_delta.dot(syn1.T)   # same as l1_error = np.dot(l2_delta,syn1.T)
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn1 += np.dot(l1.T, l2_delta)
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l2)
