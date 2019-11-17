# X 	Input dataset matrix where each row is a training example
# y 	Output dataset matrix where each row is a training example
# l0 	First Layer of the Network, specified by the input data
# Syn0 	First layer of weights, Synapse 0, connecting l0 to l1.
# 2 inputs, 1 output
# Weight defined as syn0 = [[1],[1]]

import numpy as np

# sigmoid function
# this nonlinearity maps a function called a "sigmoid"
# If the sigmoid's output is a variable "out", then the derivative is simply out * (1-out)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])  

y = np.array([[0, 1, 1, 1]]).T  # T is for mattrix transpose

# initialize weights
syn0 = np.array([[1],[1]])

# forward propagation
l0 = X
# l1 = sigmoid (l0 x syn0), matrix-matrix multiplication
# [4,1] = [4,2].[2,1] + [4,1]
l1 = sigmoid(np.dot(l0, syn0))
