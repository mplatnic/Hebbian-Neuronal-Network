# Artificial-Intelligence

A.I. is divided in many fields;

Machine learning made of Deep learning, Supervised and Unsupervised Learning

Natural Language Processing
Expert systems
Speech
Vision
..
# Supervised Learning

## Introduction: Hebbian Neuronal Network 

The Hebbian Learning Rule is a learning rule that specifies how much the weight of the connection between two units should be increased or decreased in proportion to the product of their activation. The rule builds on Hebbs's 1949 learning rule which states that the connections between two neurons might be strengthened if the neurons fire simultaneously. The Hebbian Rule works well as long as all the input patterns are orthogonal or uncorrelated. The requirement of orthogonality places serious limitations on the Hebbian Learning Rule. A more powerful learning rule is the delta rule, which utilizes the discrepancy between the desired and actual output of each output unit to change the weights feeding into it. 

<img src="https://blog-c7ff.kxcdn.com/blog/wp-content/uploads/2017/04/original.jpg" width="600">
<img src="https://qph.fs.quoracdn.net/main-qimg-100c2ff22d7fbed74bb52f9d4be0c6de" width="600">

In real neurons, time-domain signal pulses travel along the dendrites, and then arrive at the neuronal body independently, and are integrated in time and space inside it (some excite, some inhibit). When the neuronal body is triggered, it produces a time-dependent set of pulses down its axon, that split up as it branches and take time to travel out to the synapses, which themselves exhibit a non-linear, delayed, time-dependent integration as the chemical neurotransmitter signal passes across the synapse to eventually trigger a signal in the post-synaptic dendrite. There is a strengthening of the synapse, or learning, in the process, if the neurons on both sides of it fire together within a certain interval, called Hebbian learning. (https://www.quora.com/What-is-the-simplest-example-for-a-Hebbian-learning-algorithm-in-terms-of-AI)

<img src="https://qph.fs.quoracdn.net/main-qimg-67d44168ddd8781707551d306298a0c2" width="500">

Mathematically, we can describe Hebbian learning as:

    w#ij [ n + 1 ] = w#ij [ n ] + ε x x#i [ n ] x x#j [ n ] 
    Δw#ij=ε·pre#i·post#j

Here, ε is a learning rate coefficient, and x are the outputs of the ith and jth elements. 

It was proposed by Rumelhart and Zipser (1985) and is referred to as the competitive learning rule:

    Δw#ij=ε·pre#i·post#j−ε·post#j·w#ij
    Δw#ij=ε·post#j·(pre#i−w#ij)

Oja Rule:    
   
    Δw#ij=ε·post#j·(pre#i−post#j.w#ij)
    Δw#ij=ε·(post#j·pre#i−post#j^2.w#ij)

## Basics on Mattrix multiplication:

<img src="https://www.mathsisfun.com/algebra/images/matrix-multiply-b.svg" width="320">

(1, 2, 3) • (8, 10, 12) = 1×8 + 2×10 + 3×12 = 64

<img src="https://www.mathsisfun.com/algebra/images/matrix-multiply-c.svg" width="400">

## Note on Sigmoid function:


This is our "nonlinearity". While it can be several kinds of functions, this nonlinearity maps a function called a "sigmoid". A sigmoid function maps any value to a value between 0 and 1. 

<img src="https://iamtrask.github.io/img/sigmoid.png" width="400">

The derivative of the sigmoid for error backward correction:

<img src="https://iamtrask.github.io/img/sigmoid-deriv-2.png" width="400">

used for: l1_delta = l1_error * nonlin(l1,True)

When we multiply the "slopes" by the error, we are reducing the error of high confidence predictions. Look at the sigmoid picture again! If the slope was really shallow (close to 0), then the network either had a very high value, or a very low value. This means that the network was quite confident one way or the other. However, if the network guessed something close to (x=0, y=0.5) then it isn't very confident. We update these "wishy-washy" predictions most heavily, and we tend to leave the confident ones alone by multiplying them by a number close to 0.

ADDITIONAL LINKS:
An easy-to-follow scikit-learn tutorial that will help you get started with Python machine learning
https://pythonprogramming.net/flat-clustering-machine-learning-python-scikit-learn/

How to create a poet / writer using Deep Learning (Text Generation using Python)?
https://www.analyticsvidhya.com/blog/2018/03/text-generation-using-python-nlp/
