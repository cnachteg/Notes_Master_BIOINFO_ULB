from Layer import *
import pickle

class NeuralNet():

    def __init__(self, nodesList):
        self.layersList = []
        for i in range (1, len(nodesList)):
            self.layersList.append(Layer(nodesList[i-1], nodesList[i]))
            
    def getWeights(self):
        weights = []
        for lay in self.layersList : 
            for neuron in lay.neurons :
                weights = weights + neuron.weights
        return weights
        
    def setWeights(self, weights):
        index = 0
        for lay in self.layersList : 
            for neuron in lay.neurons : 
                ranges = weights[index:index+neuron.size]
                wrap = []
                for val in ranges : 
                    wrap.append(val)
                neuron.setWeights(wrap)
                index = index+neuron.size
                
    def size(self):
        sum = 0
        for lay in self.layersList : 
            sum += lay.size()
        return sum
        

    def execute(self,layer, inputs) :
        if layer == 0 :
            return self.layersList[layer].getOutputs(inputs)
        else:
            return self.layersList[layer].getOutputs(self.execute(layer-1, inputs))

    def save(self,filename):
        weights = self.getWeights()
        with open(filename, 'wb') as fp:
            pickle.dump(weights, fp)

    def load(self,filename):
        with open (filename, 'rb') as fp:
            weights = pickle.load(fp)
        self.setWeights(weights)