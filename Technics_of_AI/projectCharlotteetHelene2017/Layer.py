
from Neuron import *

class Layer():

    def __init__(self, inputs, nodes):
        self.neurons=[]
        for i in range (0,nodes):
            self.neurons.append(Neuron(inputs))
        self.inputs = inputs
    
    #return # of weights    
    def size(self):
        return len(self.neurons) * (self.inputs + 1);
        
    def getOutputs(self, inputsList):
        outputs=[]
        for i in range (0, len(self.neurons)):
            outputs.append(self.neurons[i].actionPot(inputsList))
        return outputs