Many Tools available:
https://www.researchgate.net/post/What_is_the_best_open_source_package_for_artificial_neural_networks
https://deeplearning4j.org/docs/latest/deeplearning4j-quickstart

## Neurophstudio
Neuroph works with JDK7 which is not available
Install JDK8 from https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
JDK12 tested but does not work.

Download from http://neuroph.sourceforge.net/download.html
neurophstudio-windows-2.96.exe

To create and train Perceptron neural network using Neuroph Studio do the following:
1. Create Neuroph Project.
2. Create Perceptron network. (from main menu choose File > New > Neural Network > Perceptron)
3. Create training set (from main menu choose File > New > Data Set)
4. Train network
5. Test trained network


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

#### Overfitting

I am taking the world-famous plot below from wikipedia to show how the validation set helps prevent overfitting. The training error, in blue, tends to decrease as the number of epochs increases: the network is therefore attempting to match the training set exactly. The validation error, in red, on the other hand follows a different, u-shaped profile. The minimum of the curve is when ideally the training should be stopped as this is the point at which the training and validation error are lowest.

![Overfitting](https://i.stack.imgur.com/8Kguj.png)


br />
