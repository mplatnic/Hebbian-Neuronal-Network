# https://iamtrask.github.io/2015/07/12/basic-python-network/
# X 	Input dataset matrix where each row is a training example
# y 	Output dataset matrix where each row is a training example
# l0 	First Layer of the Network, specified by the input data
# l1 	Second Layer of the Network, otherwise known as the hidden layer
# Syn0 	First layer of weights, Synapse 0, connecting l0 to l1.
# 2 inputs, 1 output
# SUPERVISED neural network using non linear Sigmoid feedback


import numpy as np
import random

# sigmoid function
# this nonlinearity maps a function called a "sigmoid"
# If the sigmoid's output is a variable "out", then the derivative is simply out * (1-out)
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset  [4,2]
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])  

# output dataset  [4,1]
y = np.array([[0, 1, 1, 1]]).T  # T is for mattrix transpose

# seed random numbers to make calculation deterministic. (1) is the sequence used for random
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((2, 1)) - 1    # [2,1]    2 neurons input
# initialize bias
bias = random.random()

for iter in range(50000):
    # forward propagation
    l0 = X
    # l1 = nonlin (l0 x syn0), matrix-matrix multiplication
    # [4,1] = [4,2].[2,1] + [4,1]
    l1 = nonlin(np.dot(l0, syn0)) + bias

    # how much did we miss?  [4,1]  (target-output)
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    # [4,1]  = [4,1]* const
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    # mu is learning rate
    # Syn0new = syn0 + mu*(Partial derivative L1_error and syn0)
    # Syn0new = syn0 + mu*(l1_error*sigmoid_deriv(l1)*l0)
    # Syn0new = syn0 + mu*(l1_delta*l0)
    # [2,1] = [2,4].[4,1]
    syn0 += np.dot(l0.T, l1_delta)

    # update bias
    bias += np.sum(l1_delta)


print("Output After Training:")
print(l1)

print("Weight:")
print(syn0)
print("Bias:")
print(bias)

