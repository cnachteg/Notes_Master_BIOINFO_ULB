from NeuralNet import *
from GeneticAlgorithm import *
from config import *
from pacman import *
import time

class Decoder() : 
    def __init__(self):
        self.here = True
        
    def getFitness(self,gene):
    	def save(phenotype,filename):
        	with open(filename, 'wb') as fp:
        		pickle.dump(gene, fp)

    	save(gene,filename)
    	Args = ["-l",layout_style, "-p", "AINeuralAgent", "-g", "FixedGhost", "-q",
    			"-a","neural_file="+filename,"-n",str(num_training)]
    	args = readCommand( Args ) # Get game components based on input
    	start = time.time()
    	fitness = runGames( **args )
    	elapsed = time.time()-start
    	#print(elapsed)

    	return fitness
       
       
def main():
    #properties en java est une classe ... mettre dans un fichier?  
    #done with config
    
    #generate randomize NeuralNet. # inputs match # inputs pacManAI et # outputs match # outputs pacManAi
    net = NeuralNet(l_nodes)
    net.save(output)

    decoder = Decoder()

    geneticAlgo = GA(net.size(),decoder)
    best = geneticAlgo.run()
    bestpheno = best.get_gene()
    net.setWeights(bestpheno)
    net.save(output)
    #print(decoder.getFitness(bestpheno))


    
       
'''       public static void main(String[] args) throws Exception {
		Properties props = new Properties();
		props.load(new FileInputStream(new File(GeneticAlgorithm.PROPERTIES)));
		props.load(new FileInputStream(new File("./pacman.properties")));
		props.setProperty("game.neural", NEURAL_FILE);		// Point to the generated neural net
		props.setProperty("game.enable.ai", "true");		// Enable PacMan AI
		props.setProperty("game.fps", "10000");				// Run game at infinite speed
		File output = new File(NEURAL_FILE);	// Output file for the neural net
		
		// Generate a randomized neural net with an arbitrary number of layers
		// with an arbitrary number of nodes in each layer. The only restriction is
		// that the number of inputs must match the number of inputs in PacManAi
		// and the number of outputs must match the number of outputs in PacManAi.
		NeuralNet net = new NeuralNet(13, 10, 8, 4);
		net.save(output);
		
		GeneticGene[] genes = new GeneticGene[net.size()];
		for(int i = 0; i < genes.length; i++)
			genes[i] = new GeneticGene(null, 40, -3.0, 3.0);

		// Initialize the decoder and run the algorithm using the loaded properties
		PacManDecoder decoder = new PacManDecoder(genes, Game.load(props));
		GeneticChromosome best = GeneticAlgorithm.run(decoder, props);
		
		// Set the weights of the neural net to be the best chromosome in the population
		// and then save this neural net to the output file. THe program terminates once
		// this condition has been met.
		String bits = best.getGenotype();
		double[] phenotype = decoder.getPhenotype(bits);
		net.setWeights(phenotype);
		System.out.println(net.getWeights());
		net.save(output);
	}'''

if __name__ == '__main__':
	main()
