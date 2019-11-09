import numpy as np

# The basic rule of thumb is if you really don’t know what activation function to use, 
# then simply use RELU as it is a general activation function and is used in most cases these days.
# If your output is for binary classification then, sigmoid function is very natural choice for output layer. 

#    Sigmoid function
#        f(x) = 1/(1 + exp(-x))
#        Value Range : 0 to 1
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))


#    Tanh function, Tangent Hyperbolic function
#        f(x) = tanh(x) = 2/(1 + e-2x) - 1 = 2 * sigmoid(2x) - 1
#        Value Range : -1 to 1
def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

#    RELU , Stands for Rectified linear unit for hidden layers
#        f(x) = max(0,x)
#        Value Range 0 to inf
#        most widely used activation function

