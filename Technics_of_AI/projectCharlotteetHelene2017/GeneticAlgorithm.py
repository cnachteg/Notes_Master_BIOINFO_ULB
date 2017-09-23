#import Decoder
from Population import population, gene
from config import *
import pickle


class GA:
	"""docstring for GeneticAlgorithm"""
	def __init__(self,size_network,decoder):
		self.maxgen = max_generation
		self.gen = 0
		self.decoder = decoder
		self.size_network = size_network

	def print_results(self,pop,gen,logfile):
		with open(logfile,'a') as log:
			average,best_average_score,best_average = pop.average_score()
			log.write("%s\t%s\t%s\n" % (str(gen),str(average),str(best_average_score)))
		with open("res_"+str(max_generation)+"_gen_"+str(gen)+".txt",'w') as file:
			pickle.dump(best_average.get_gene(), file)

	def run(self):
		pop = population(self.decoder,self.size_network)
		# best = pop.pop[0]
		# bestFitness = self.decoder.getFitness(best.get_phenotype())
		# for popul in pop.get_pop():
		# 	print(popul.get_gene())

		while self.gen < self.maxgen:
			print self.gen
			self.print_results(pop,self.gen,logfile)
			pop.evolve()
			self.gen += 1
			# res = pop.get_best()
			# resFitness = self.decoder.getFitness(res.get_phenotype())
			# if bestFitness < resFitness:
			# 	best = res
			# 	bestFitness = resFitness
			#print("***************************************")
			#print("BEST OF THIS GENERATION")
			#print(self.decoder.getFitness(pop.get_best().get_phenotype()))
			#print("***************************************")

		return pop.average_score()[2]


