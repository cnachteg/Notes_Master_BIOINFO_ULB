from random import random,randrange
from config import *
import math

class population:
	"""docstring for population"""
	def __init__(self,decoder,size_network):
		self.pop = [[]]*size_population
		self.decoder = decoder
		self.size_network = size_network

		for i in range(size_population):
			self.pop[i] = gene(decoder,size_network)

	def get_pop(self):
		return self.pop

	def evolve(self):
		def sort_pop(pop):
			scores = []
			for gene in pop:
				scores.append(gene.fitness)
			sortedList = sorted(zip(pop,scores), key=lambda y: y[1], reverse=True)
			#print(sortedList)
			return [x[0] for x in sortedList]

		def select(pop):
			selection = []
			for i in range(selection_size):
				rand = int(random()*len(pop))
				selection.append(pop[rand])

			selection = sort_pop(selection)

			return selection[0]

		def mate(pop,rate,decoder,size_network):
			parent1 = select(pop)
			parent2 = select(pop)

			child1 = gene(decoder,size_network)
			child2 = gene(decoder,size_network)

			while parent1.get_gene() == parent2.get_gene():
				parent2 = select(pop)

			if random() <= rate:
				rand = int(random()*len(parent2.get_gene()))

				child1_gene = parent1.get_gene()[:rand] + parent2.get_gene()[rand:]
				child2_gene = parent2.get_gene()[:rand] + parent1.get_gene()[rand:]

				child1.update_gene(child1_gene)
				child2.update_gene(child2_gene)

			return [child1,child2]

		def mutate(individual):
			gene = individual.get_gene()
			rand = int(random()*len(gene))

			gene[rand] = gene[rand] * randrange(0,2)


			individual.update_gene(gene)

			return individual

		# keep part of the population based on elitism
		index = int(size_population * elitism);
		if(index % 2 != 0):
			index += 1

		self.pop = sort_pop(self.pop)

		new_pop = self.pop[:index]
		new_generation = []

		while index < size_population:
			children = mate(self.pop,crossover_rate,self.decoder,self.size_network)

			for child in children:
				if random() < mutation_rate:
					child = mutate(child)
				new_generation.append(child)

			index += 2

		new_pop.extend(new_generation)

		self.pop = new_pop

	def get_best(self):
		scores = []
		for gene in self.pop:
			scores.append(gene.fitness)
		#print(scores)
		sortedList = sorted(zip(self.pop,scores), key=lambda y: y[1], reverse=True)
		#print sortedList
		return sortedList[0][0]

	def average_score(self):
		scores = []
		for gene in self.pop:
			scores.append(gene.fitness)
		sortedList = sorted(zip(self.pop,scores), key=lambda y: y[1], reverse=True)
		return (sum(scores)/len(scores)),sortedList[0][1],sortedList[0][0]


class gene:
	"""docstring for translator"""
	def __init__(self,decoder,size_network):
		self.size_network = size_network
		self.decoder = decoder
		self.gene = [0] * self.size_network
		index = 0
		for i in range(self.size_network):
			self.gene[i] = random()*6-3
		self.fitness = self.get_fitness()

	def update_gene(self,gene):
		self.gene = gene
		self.fitness = self.get_fitness()


	def get_gene(self):
		return self.gene

	def get_fitness(self):
		return self.decoder.getFitness(self.gene)

