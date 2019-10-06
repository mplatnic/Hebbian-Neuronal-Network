## Graph simulation tool
https://rechneronline.de/function-graphs/

## Neurophstudio
Neuroph works with JDK7 which is not available
Install JDK8 from https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
JDK12 tested but does not work.

Download from http://neuroph.sourceforge.net/download.html
neurophstudio-windows-2.96.exe

To create and train Perceptron neural network using Neuroph Studio do the following:
1. Create Neuroph Project.
2. Create Perceptron network. (from Project menu Right click on Neural Network then "new" the "Other" ) </br>
then Neural Network then next </br>
then Multi Layer Perceptron

3. Create training set (from main menu choose File > New > Data Set)
4. Train network
5. Test trained network

## Activation Function
Definition of activation function:- Activation function decides, whether a neuron should be activated or not by calculating weighted sum and further adding bias with it. The purpose of the activation function is to introduce non-linearity into the output of a neuron.

Explanation :-
We know, neural network has neurons that work in correspondence of weight, bias and their respective activation function. In a neural network, we would update the weights and biases of the neurons on the basis of the error at the output. This process is known as back-propagation. Activation functions make the back-propagation possible since the gradients are supplied along with the error to update the weights and biases.

Why do we need Non-linear activation functions :-
A neural network without an activation function is essentially just a linear regression model. The activation function does the non-linear transformation to the input making it capable to learn and perform more complex tasks.

Example of non-linear function: A = 1/(1 + exp(-x)) (sigmoid function)
)
Data from: https://www.geeksforgeeks.org/activation-functions-neural-networks/

## Hyperparameters
Hyperparameters are everything that can influence how a neural network performs beyond the basic choice of architecture. This can be fundamental stuff like the number of layers in the network and the number of neurons in each layer, but also more abstract parameters like the learning rate, the batch size, and so forth.

Following data Compiled from: 
https://machinelearningmastery.com/learning-rate-for-deep-learning-neural-networks/  By Jason Brownlee
https://stackoverflow.com/questions/25889637/how-to-use-k-fold-cross-validation-in-a-neural-network

#### Learning rate
During training, the backpropagation of error estimates the amount of error for which the weights of a node in the network are responsible. Instead of updating the weight with the full amount, it is scaled by the learning rate.
The learning rate is a configurable hyperparameter used in the training of neural networks that has a small positive value, often in the range between 0.0 and 1.0. Typical values for a neural network with standardized inputs (or inputs mapped to the (0,1) interval) are less than 1 and greater than 10^−6.<br />
The learning rate is often represented using the notation of the lowercase Greek letter eta (n).<br />
Generally, a large learning rate allows the model to learn faster, at the cost of arriving on a sub-optimal final set of weights. A smaller learning rate may allow the model to learn a more optimal or even globally optimal set of weights but may take significantly longer to train.<br />
Potential issue: Oscillating performance, positive feedback<br />
Solution: create a plot

#### Training epochs 
Passes through the training data

#### Momentum 
The amount of inertia of past updates is controlled via the addition of a new hyperparameter, often referred to as the “momentum” or “velocity” and uses the notation of the Greek lowercase letter alpha (a).<br />
An exponentially weighted average of the prior updates to the weight can be included when the weights are updated. This change to stochastic gradient descent is called “momentum” and adds inertia to the update procedure, causing many past updates in one direction to continue in that direction in the future.<br />
It has the effect of smoothing the optimization process, slowing updates to continue in the previous direction instead of getting stuck or oscillating.<br />
Momentum is set to a value greater than 0.0 and less than one, where common values such as 0.9 and 0.99 are used in practice.<br />

#### Overfitting
The phenomenon by which any learning system matches its training set almost perfectly but constantly fails with unseen data is called overfitting.<br />
Here come in the validation and testing parts of the algorithm. What you do is you split the dataset into three sets -- training, validation and testing (Tr, Va and Te). (80-10-10)% is usually a good proportion.<br />

#### Training and Validation
Now what happens is that the neural network is trained on the Tr set and its weights are correctly updated. The validation set Va is then used to compute the classification error E = M - Y using the weights resulting from the training, where M is the expected output vector taken from the validation set and Y is the computed output resulting from the classification (Y = W * X). If the error is higher than a user-defined threshold then the whole training-validation epoch is repeated. This training phase ends when the error computed using the validation set is deemed low enough.

#### Cross Validation
one can further strengthen the network against over-fitting by performing K-fold cross-validation. This technique involves performing K rounds of training-validation-testing on, different, non-overlapping, equally-proportioned Tr, Va and Te sets.

#### Over/Under fitting - Bias and Variance
In general 
- having high bias reduces the performance of the algorithm on training set 
- while having high variance is high accuracy on training data and reduces performance on unseen data
- When result is Biased towards a specific answer the system is underfitting
- The system is not able to predict for the new and unseen condition. This condition is called overfitting
- Low-complexity models have a low variance, but a high bias. They don’t train very efficiently and don’t learn much
- As the complexity increases, the bias decreases. The model trains better and also achieves better results in test accuracy. But with increasing complexity, the variance is growing, too. While the training accuracy is getting better and better, the test accuracy actually gets worse.  

So how do we find the perfect balance between variance and bias?
 - Coordinate Descent Approach, start small, then gradually go bigger.

## Many simulation tools available:
https://www.researchgate.net/post/What_is_the_best_open_source_package_for_artificial_neural_networks
https://deeplearning4j.org/docs/latest/deeplearning4j-quickstart

