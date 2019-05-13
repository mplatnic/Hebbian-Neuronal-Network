# Hebbian-Neuronal-Network
Python code for basic Hebbian Neuronal Network

The Hebbian Learning Rule is a learning rule that specifies how much the weight of the connection between two units should be increased or decreased in proportion to the product of their activation. The rule builds on Hebbs's 1949 learning rule which states that the connections between two neurons might be strengthened if the neurons fire simultaneously. The Hebbian Rule works well as long as all the input patterns are orthogonal or uncorrelated. The requirement of orthogonality places serious limitations on the Hebbian Learning Rule. A more powerful learning rule is the delta rule, which utilizes the discrepancy between the desired and actual output of each output unit to change the weights feeding into it. 

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
