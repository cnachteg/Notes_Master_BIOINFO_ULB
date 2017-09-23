""" INFO-F409 - Learning Dynamics: Assignment 3
N-armed bandit with Random, e-greedy and Softmax
One Plot of the average reward with all algorithms
One graphper arm showing the expected reward with the actual reward all action
selection on the same plot
A histogram per algorithm showing the number of times each action is selected
"""

import matplotlib.pyplot as plt
import numpy as np


def random(n,expected_rewards,list_sigma):
	"""
	:param n: number of arms
	:param expected_rewards: list of the mean distribution of the reward
	Q* for each arm
	:param sigma: list of standard deviation for normal distribution wooth mean Q*
	"""

	Q = np.zeros(n)
	choice = np.zeros(n)
	a = np.array([i for i in range(n)])
	Q_overtime = np.array([np.zeros(n)])
	reward_list = np.array([])

	#random action at each turn
	for i in range (1000):
		current_a = np.random.randint(n)
		mean, sigma = expected_rewards[current_a],list_sigma[current_a]
		reward = np.random.normal(mean,sigma)
		choice[current_a] += 1
		Q[current_a] +=  (1/choice[current_a]) * (reward - Q[current_a])
		Q_overtime = np.append(Q_overtime,[Q],axis=0)
		reward_list = np.append(reward_list,reward)

	return Q_overtime, choice, reward_list


def e_greedy(n,expected_rewards,list_sigma,e_str):
	"""
	:param n: number of arms
	:param expected_rewards: list of the mean distribution of the reward
	Q* for each arm
	:param sigma: list of standard deviation for normal distribution wooth mean Q*
	:param e: e parameter for the greedy algorithm
	"""

	Q = np.zeros(n)
	choice = np.zeros(n)
	a = np.array([i for i in range(n)])
	Q_overtime = np.array([np.zeros(n)])
	reward_list = np.array([])


	for t in range(1000):
		e = eval(e_str)
		best = np.random.choice(np.array([0,1]),p=[e,1-e])

		# random choice
		# first turn is random if epsilon = 0
		if best == 0 or (t == 0 and e == 0):
			current_a = np.random.randint(n)

		# best Q choice
		else:
			current_a = np.argmax(Q)

		mean, sigma = expected_rewards[current_a],list_sigma[current_a]
		reward = np.random.normal(mean,sigma)
		choice[current_a] += 1
		Q[current_a] +=  (1/choice[current_a]) * (reward - Q[current_a])
		Q_overtime = np.append(Q_overtime,[Q],axis=0)
		reward_list = np.append(reward_list,reward)


	return Q_overtime, choice, reward_list


def softmax(n, expected_rewards, list_sigma, tau_str):
	"""
	:param n: number of arms
	:param expected_rewards: list of the mean distribution of the reward for each arm
	:param sigma: list of standard deviation for normal distribution with mean Q*
	:param t: tau parameter for the softmax algorithm
	"""

	Q = np.zeros(n)
	choice = np.zeros(n)
	a = np.array([i for i in range(n)])
	Q_overtime = np.array([np.zeros(n)])
	reward_list = np.array([])

	# selection of the action according to probability calculated according to Boltzmann Distribution
	for t in range(1000):
		tau = eval(tau_str)
		probability = probability_calcul(Q,tau)

		current_a = np.random.choice(a,p=probability)
		mean, sigma = expected_rewards[current_a],list_sigma[current_a]

		reward = np.random.normal(mean,sigma)
		choice[current_a] += 1
		Q[current_a] +=  (1/choice[current_a]) * (reward - Q[current_a])
		Q_overtime = np.append(Q_overtime,[Q],axis=0)
		reward_list = np.append(reward_list,reward)

	return Q_overtime, choice, reward_list


def probability_calcul(Q_list,t):
	"""
	:param Q_list: list of Q-values
	:param t: computational temperature
	:return: Probabilities according to Boltzmann distribution
	"""
	den = np.sum(np.exp(Q_list/t))
	prob = np.array([])

	for Q in Q_list:
		num = np.exp(Q/t)
		prob = np.append(prob,num/den)

	return prob


def average_reward(average_rewards):
	"""
	Plot the average reward over time for each algorithm
	"""
	names = ('Random','e-greedy 0','e-greedy 0.1','e-greedy 0.2',
			'Softmax 1', 'Softmax 0.1','e-greedy time variant','Softmax time variant')

	fig = plt.figure()
	ax = plt.axes()
	colors = ['r','g','b','y','k','m','c','gray','brown']
	list_names = list(names)
	x = np.arange(1000)

	for reward in average_rewards:
		ax.plot(x,reward,color=colors.pop(), linewidth=2, label=list_names.pop(0))
	fig.suptitle('Plot of the average reward')
	ax.set_xlim([0,1000])

	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

	plt.show()


def plot_each_arm(Q_results, Q_star,n):
	"""
	Plot the Q*a vs Qa for each algorithm
	"""
	names = ('Random','e-greedy 0','e-greedy 0.1','e-greedy 0.2',
			'Softmax 1', 'Softmax 0.1','e-greedy time variant','Softmax time variant')

	for i in range(n):
		fig = plt.figure()
		ax = plt.axes()
		colors = ['r','g','b','y','k','m','c','gray','brown']
		ax.axhline(Q_star[i],color=colors.pop(), linewidth=4, linestyle='--', label='Q*')
		list_names = list(names)
		x = np.arange(1001)

		for result in Q_results:
			one_arm = result[:,i]
			ax.plot(x,one_arm,color=colors.pop(), linewidth=2, label=list_names.pop(0))
		fig.suptitle(r'Plot of $Q_a$ vs $Q^*_a$ for the action ' + str(i + 1))
		ax.set_xlim([0,1000])

		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

		# Put a legend to the right of the current axis
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

		plt.show()


def histo_choice(choice_results,n):
	"""
	Plot the distribution of the selection of the actions for each algorithm
	"""
	names_algo = ['Random','e-greedy 0','e-greedy 0.1','e-greedy 0.2',
			'Softmax 1', 'Softmax 0.1','e-greedy time variant','Softmax time variant']

	x_pos = np.arange(n)

	names = []

	for i in range(n):
		names.append('Action %s' % (i+1))

	for algorithm in choice_results:
		list_names = list(names)

		fig = plt.figure()
		fig.suptitle('Count of the selection of each arm for the algorithm %s' % (names_algo.pop(0)))
		ax = fig.add_subplot(111)
		
		ax.bar(x_pos,algorithm,align='center')
		
		plt.xticks(x_pos, names)
		ax.set_ylabel('Number of times selected')
		ax.set_ylim([0,1000])

		plt.show()


def main_plot(Q_star,Q_results,choice_results,rewards,n):
	average_reward(rewards)
	plot_each_arm(Q_results,Q_star,n)
	histo_choice(choice_results,n)

def save_results(Q,choice,reward,Q_results,choice_results,reward_results):
	Q_results.append(Q)
	choice_results.append(choice)
	reward_results.append(reward)

	return Q_results,choice_results,reward_results

def mean_results(Q,choice,reward,Q_results,choice_results,reward_results):
	Q_results.append(np.mean(np.array(Q),axis=0))
	choice_results.append(np.mean(np.array(choice),axis=0))
	reward_results.append(np.mean(np.array(reward),axis=0))

	Q = []
	reward = []
	choice = []

	return Q, choice, reward, Q_results,choice_results,reward_results


#----------------------------------------------------------------------------


def ex1_2(Q_star,list_sigma):
	Q_results = []
	choice_results = []
	reward_results = []

	current_Q =[]
	current_choice = []
	current_reward = []

	for i in range(2000):
		Q, choice, reward = random(4,Q_star,list_sigma)
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)


	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0.1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0.2')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = softmax(4,Q_star,list_sigma,'1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)


	for i in range(2000):
		Q,choice,reward = softmax(4,Q_star,list_sigma,'0.1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	main_plot(Q_star,Q_results,choice_results,reward_results,4)


def ex3(Q_star,list_sigma):
	Q_results = []
	choice_results = []
	reward_results = []

	current_Q =[]
	current_choice = []
	current_reward = []

	for i in range(2000):
		Q, choice, reward = random(4,Q_star,list_sigma)
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)


	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0.1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'0.2')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = softmax(4,Q_star,list_sigma,'1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)


	for i in range(2000):
		Q,choice,reward = softmax(4,Q_star,list_sigma,'0.1')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = e_greedy(4,Q_star,list_sigma,'1/np.sqrt(t+1)')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	for i in range(2000):
		Q,choice,reward = softmax(4,Q_star,list_sigma,'4*((1000-t+1)/1000)')
		current_Q, current_choice, current_reward = save_results(Q, choice, reward, current_Q, current_choice, current_reward)

	current_Q, current_choice, current_reward, Q_results, choice_results, reward_results = mean_results(current_Q, current_choice, current_reward, Q_results, choice_results, reward_results)

	main_plot(Q_star,Q_results,choice_results,reward_results,4)


if __name__ == "__main__":
	Q_star = [2.3,2.1,1.5,1.3]
	list_sigma = [0.9,0.6,0.4,2]

	ex1_2(Q_star,list_sigma)
	ex1_2(Q_star,2*list_sigma)
	ex3(Q_star,list_sigma)