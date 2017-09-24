
import random
import math

class Neuron() :

    def __init__(self, inputsSize) :
        self.weights = []
        for i in range(inputsSize + 1):
            self.weights.append(random.random()*6-3)
        self.size = len(self.weights)
            
    def setWeights (self, weightsList) : 
        self.weights = weightsList
        
    def actionPot(self, inputsList):
        slope = 1.0
        sum = self.weights[self.size - 1]
        for i in range(len(inputsList)):
            sum += inputsList[i]*self.weights[i]
        return 1.0/(1 + math.exp(-sum*slope))