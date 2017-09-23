"""
INFO-F409 Learning Dynamics: Stochastic Reward Game
"""

import numpy as np
import matplotlib.pyplot as plt


def JAL(n, expected_rewards, list_sigma, tau_str):
    """
	:param n: number of arms
	:param expected_rewards: list of the mean distribution of the reward for each arm
	:param sigma: list of standard deviation for normal distribution with mean Q*
	:param t: tau parameter for the softmax algorithm
	"""

    Q_joint = np.zeros((n, n))
    choice = np.zeros((n, n))
    a = np.array([i for i in range(n)])  # row
    b = np.array([i for i in range(n)])  # column

    reward_list = np.array([])

    EV_a = np.zeros(n)
    EV_b = np.zeros(n)

    for t in range(5000):
        tau = eval(tau_str)
        prob_a = probability_calcul(EV_a, tau)
        prob_b = probability_calcul(EV_b, tau)

        current_a = np.random.choice(a, p=prob_a)
        current_b = np.random.choice(b, p=prob_b)
        mean, sigma = expected_rewards[current_a][current_b], list_sigma[current_a][current_b]

        reward = np.random.normal(mean, sigma)
        choice[current_a][current_b] += 1
        Q_joint[current_a][current_b] += (1 / choice[current_a][current_b]) * (reward - Q_joint[current_a][current_b])
        reward_list = np.append(reward_list, reward)

        EV_a, EV_b = eval_action(Q_joint, choice)

    return reward_list


def eval_action(Q_joint, choice):
    """
    Calculate the evaluated value of each action according to the belied of what the other agent will play
    """
    Q_individual = Q_joint * (choice / np.sum(choice))
    EV_a = np.sum(Q_individual, axis=1)
    EV_b = np.sum(Q_individual, axis=0)

    return EV_a, EV_b


def probability_calcul(Q_list, t):
    """
    Calculate the probabilities according to the Boltzmann distribution
    """
    den = np.sum(np.exp(np.longfloat(Q_list / t)))
    prob = np.array([])

    for Q in Q_list:
        num = np.exp(np.longfloat(Q / t))
        prob = np.append(prob, num / den)

    return prob


def FMQ(n, expected_rewards, list_sigma, tau_str, c):
    """
    """
    Q_a = np.zeros(n)
    Q_b = np.zeros(n)
    choice_a = np.zeros(n)
    choice_b = np.zeros(n)
    a = np.array([i for i in range(n)])
    b = np.array([i for i in range(n)])
    best_reward_a = np.zeros(n)
    nb_best_a = np.zeros(n)
    best_reward_b = np.zeros(n)
    nb_best_b = np.zeros(n)

    reward_list = np.array([])

    # the actions are evaluated according to the frequency of the highest reward receuved until now
    for t in range(5000):
        EV_a = eval_action_FMQ(Q_a, best_reward_a, nb_best_a, c)
        EV_b = eval_action_FMQ(Q_b, best_reward_a, nb_best_b, c)

        tau = eval(tau_str)
        prob_a = probability_calcul(EV_a, tau)
        prob_b = probability_calcul(EV_b, tau)

        current_a = np.random.choice(a, p=prob_a)
        current_b = np.random.choice(b, p=prob_b)

        mean, sigma = expected_rewards[current_a][current_b], list_sigma[current_a][current_b]

        reward = np.random.normal(mean, sigma)

        best_reward_a, nb_best_a = update_best(reward, best_reward_a, nb_best_a, current_a)
        best_reward_b, nb_best_b = update_best(reward, best_reward_b, nb_best_b, current_b)

        choice_a[current_a] += 1
        choice_b[current_b] += 1

        Q_a[current_a] += (1 / choice_a[current_a]) * (reward - Q_a[current_a])
        Q_b[current_b] += (1 / choice_b[current_b]) * (reward - Q_b[current_b])

        reward_list = np.append(reward_list, reward)

    return reward_list


def eval_action_FMQ(Q, best_reward, nb_best, c):
    """
    Calculate the evaluated value of the actions according to the frequency of the highest reward received until now
    """
    second_term = best_reward * nb_best * c
    EV = Q + second_term

    return EV


def update_best(reward, best_reward, nb_best, action):
    """
    Update the frequency of the highest reward received until now, or change the highest reward to the new one
    """
    if reward > best_reward[action]:
        best_reward[action] = reward
        nb_best[action] = 1

    elif reward == best_reward[action]:
        nb_best[action] += 1

    return best_reward, nb_best


def plot(reward_JAL, reward_FMQ, list_sigma):
    """
    Plot the average reward for each algortihm over time
    """
    fig = plt.figure()
    ax = plt.axes()

    x = np.arange(5000)

    ax.plot(x, reward_JAL, color='r', linewidth=1, label='JAL')
    ax.plot(x, reward_FMQ, color='g', linewidth=1, label='FMQ')

    fig.suptitle(r'Plot of the average reward vs time steps with ($sigma,sigma_0,sigma_1$) =' + str(list_sigma))

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

    ax.set_xlim([0, 5000])


def main(list_sig):
    sigma, sigma_0, sigma_1 = list_sig
    Q_star = [[11, -30, 0], [-30, 7, 6], [0, 0, 5]]
    list_sigma = [[sigma_0, sigma, sigma], [sigma, sigma_1, sigma], [sigma, sigma, sigma]]

    reward_list_JAL = []
    reward_list_FMQ = []
    for i in range(1000):
        reward_list_JAL.append(JAL(3, Q_star, list_sigma, '1'))
        reward_list_FMQ.append(FMQ(3, Q_star, list_sigma, '1', 10))

    reward_list_JAL = np.array(reward_list_JAL)
    reward_list_FMQ = np.array(reward_list_FMQ)

    final_JAL = np.mean(reward_list_JAL, axis=0)
    final_FMQ = np.mean(reward_list_FMQ, axis=0)

    plot(final_JAL, final_FMQ, list_sig)


if __name__ == "__main__":
    # ex 1
    main((0.2, 0.2, 0.2))

    # ex 2
    main((0.1,4,0.1))

    # ex 3
    main((0.1,0.1,4))
