import numpy as np

def Sigmoid(x):
  return 1/(1+np.exp(-x))

def Sigmoid_deriv(x):
  return x*(1-x)
  
# input dataset
X = np.array([  [0,0],
                [0,1],
                [1,0],
                [1,1] ])  
                
# output dataset            
y = np.array([[0],[1],[1],[1]])

# seed random numbers to make calculation deterministic. (1) is the sequence used for random
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((2,1)) - 1    # random=[0,1], we want weight=[-1,1], random(line,column), syn0 is vertical

l0 = X

for iter in range(10000):

    # forward propagation
    S = Sigmoid(np.dot(l0,syn0))  #l1 = nonlin (l0 x syn0), matrix-matrix multiplication

    # how much did we miss?
    l1_error = y - S

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * Sigmoid_deriv(l1)

    # update weights
    syn0 = syn0 + np.dot(l0.T,l1_delta)

print ("Output After Training:")
print (S)
