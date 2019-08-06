Robotics using Arduino and ANN

Example of Robots learning to walk using ANN:
4 legs: https://www.youtube.com/watch?v=JO1rUVuv_68
https://www.youtube.com/watch?v=MeIh17FivVM  , https://www.youtube.com/watch?v=w6vF1CQLUpY
https://www.youtube.com/watch?v=3lrG2oU6yfc
(Printing legs for the robot: https://www.thingiverse.com/thing:2311678)

2 wheels balancing robot: https://www.youtube.com/watch?time_continue=27&v=WApvpk6W4Zw
(https://www.instructables.com/id/Arduino-Neural-Network-Self-Balancing-Two-Wheel-Ro/)

Crawling:
https://www.youtube.com/watch?time_continue=56&v=f1lv-Kojotk
(Code available on https://www.instructables.com/id/Q-Learning-machine-Learning-Crawler/)



Work based on http://robotics.hobbizine.com/arduinoann.html

Neural networks learn by example
ANN (Artificial Neural Network) used when the exact input to a system won't be known and where there may be missing or extraneous information.
Consider the problem of recognizing handwritten characters. The general shapes of the alphabet can be known ahead of time, but the actual input will always vary.

http://robotics.hobbizine.com/pics/nncell.png

A neuron as a tiny electro-chemical switch which turns on when stimulated. Neurons are connected to one another in vast networks. 
A neuron will have multiple neurons feeding into it and the strength of these connections will vary. 
If there is a strong connection from an input, it will provide a lot of stimulus; a weaker connection will provide less.
 a software-based artificial neural network, neurons and their connections are constructed as mathematical relationships. 
 
When the software is presented with an input pattern, it feeds this pattern through the network, 
systematically adding up the inputs to each neuron, calculating the output for that neuron, and using that output to feed the appropriate inputs to other neurons in the network.
Determining the strength of the connections between neurons, also known as the weights, becomes the principal preoccupation 
in neural network application. In the backpropagation algorithm, the network is originally initialized with random weights. 

When the network is then presented with a training set of inputs and outputs: 
As the inputs are fed through the system, the actual output is compared to the desired output and the error is calculated. 
This error is then fed back through the network and the weights are adjusted incrementally according to a learning algorithm. 






See also Genetic Algorithm, creating chromosomes after testing them mutate those with best results to create new chromosomes.
(https://www.youtube.com/watch?v=eCDU8mMcU5I)???
