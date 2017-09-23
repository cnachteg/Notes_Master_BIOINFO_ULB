__author__ = 'FlorianP'


import random

import matplotlib.pyplot as plt

import math

from math import exp


def print_board(board):
    for row in board:
        print (" ".join(row))

def probability(epsilon):
    x = random.random()
    if x < epsilon:
        #print ("x =" ,x)
        return "exploration"
    else:
        #print ("x =", x)
        return "exploitation"

def Tprobability(T):
    x = random.random()
    proba0=exp(Qalast[0] / T) / ((exp(Qalast[0] / T)+exp(Qalast[1] / T)+exp(Qalast[2] / T)+exp(Qalast[3] / T)))
    proba1=exp(Qalast[1] / T) / ((exp(Qalast[0] / T)+exp(Qalast[1] / T)+exp(Qalast[2] / T)+exp(Qalast[3] / T)))
    proba2=exp(Qalast[2] / T) / ((exp(Qalast[0] / T)+exp(Qalast[1] / T)+exp(Qalast[2] / T)+exp(Qalast[3] / T)))
    proba3=exp(Qalast[3] / T) / ((exp(Qalast[0] / T)+exp(Qalast[1] / T)+exp(Qalast[2] / T)+exp(Qalast[3] / T)))
    if 0<= x < proba0:
        return 0    #,x,proba0,proba1,proba2,proba3
    elif proba0 <= x < (proba0 + proba1):
        return 1    #,x,proba0,proba1,proba2,proba3
    elif (proba0 + proba1) <= x < (proba0 + proba1 + proba2):
        return 2   # ,x,proba0,proba1,proba2,proba3
    elif (proba0 + proba1 + proba2) <= x <= (proba0 + proba1 + proba2 + proba3):
        return 3   #x,proba0,proba1,proba2,proba3

def action_reward(action):
    if action == 0:
        result = random.normalvariate(2.3,0.6)
    elif action == 1:
        result = random.normalvariate(2.1,0.9)
    elif action == 2:
        result = random.normalvariate(1.5,2)
    elif action == 3:
        result = random.normalvariate(1.3,0.4)
    return result


def Qnext(Qa,Ra,numberaction):
    Qnext =  Qa + (Ra - Qa)/(numberaction + 1)
    return Qnext

def Qa_list():
    Qa1.append(Qalast[0])
    Qa2.append(Qalast[1])
    Qa3.append(Qalast[2])
    Qa4.append(Qalast[3])

def graphperarm(figure,Qatotallist,action,mean):
    plt.figure(figure)
    plt.subplot(223)
    plt.plot(Qatotallist[0], 'darkorange', lw = 1.5,  label = 'Random')
    plt.plot(Qatotallist[1], 'k-',  lw = 1.5, label = 'Epsilon-Greedy, E = 0')
    plt.plot(Qatotallist[2], 'b-',  lw = 1.5, label = 'Epsilon-Greedy, E = 0.1')
    plt.plot(Qatotallist[3], 'r-', lw = 1.5,  label = 'Epsilon-Greedy, E = 0.2')
    plt.plot(Qatotallist[4], 'g-',  lw = 1.5, label = 'Softmax, T = 1')
    plt.plot(Qatotallist[5], 'm-', lw = 1.5,  label = 'Softmax, T = 0.1')
    plt.plot(Qatotallist[6], 'c-', lw = 1.5,  label = 'Epsilon-Greedy, E = 1/sqrt(t)')
    plt.plot(Qatotallist[7], 'y-', lw = 1.5,  label = 'Softmax, T =  4 * (1000-T) / 1000')
    plt.plot((0, times), (mean, mean), 'k--', lw = 2.5,  label = 'Qa%s*, action%s mean' % (action,action))
    legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    for i in legend.legendHandles:
        i.set_linewidth(4.0)

    plt.title("Qa%s* vs Qa%s" % (action,action))
    plt.xlabel('Number of rounds')
    plt.ylabel('Qa%s' % action)
    plt.show()

def histogramme(figure,strategy,title):
    plt.figure(figure)
    ax = plt.subplot()
    names = ['Action1', 'Action2', 'Action3', 'Action4']
    plt.hist([1,2,3,4], 4, weights= numberaction_moyen_list[strategy], color = 'darkred')
    ax.set_xticks([1.4,2.15,2.9,3.7])
    ax.set_xticklabels(names, ha="center", size = 20)
    plt.title(title, size = 20)
    plt.ylabel('% of each action', size = 20)
    plt.show()


epsilonlist= [1,0,0.1,0.2]

Taulist = [1,0.1]
realization = 1000
times = 1000

Qk_list = []
numberaction_moyen_list = [] # en pourcent
Qa1totallist = []
Qa2totallist = []
Qa3totallist = []
Qa4totallist = []

for e in epsilonlist: #EPSILON GREEDY AVEC E = 1 QUI CORRESPOND A RANDOM
    epsilon = e
    Qkmatrix = []
    numberaction_moyen = [0,0,0,0]
    Qa1list = []
    Qa2list = []
    Qa3list = []
    Qa4list = []

    for x in range(times): # creation des matrices board1, board 2 et matrice W
        Qkmatrix.append(["0"] * realization)
        Qa1list.append(0)
        Qa2list.append(0)
        Qa3list.append(0)
        Qa4list.append(0)

    for r in range(realization):
        print ("Realization = ", r)

        numberaction = [0,0,0,0]
        Qalast = [0, 0, 0, 0]

        Qa1 = []
        Qa2 = []
        Qa3 = []
        Qa4 = []

        choices = []
        choice = random.choice(range(4))
        choices.append(choice+1)

        reward = action_reward(choice) #choisis une action au hasard
        numberaction[choice] = numberaction[choice] + 1 #ajoute 1 au decompte des actions
        Qalast[choice] = reward #modifie le Qa en position dependant du choix
        Qa1.append(Qalast[0])
        Qa2.append(Qalast[1])
        Qa3.append(Qalast[2])
        Qa4.append(Qalast[3])
        Qkmatrix[0][r] = str(reward)  # ajoute la valeur aux Qk rassemblant tous les Qk.


        for t in range(1,times):
            proba = probability(epsilon)
            if proba == "exploitation":
                for i in random.sample(range(len(Qalast)),len(Qalast)): #choisir au random un Q max (en cas d'egalite avec les voisins)
                    if Qalast[i] == max(Qalast):
                        choice = i

            elif proba == "exploration":
                choice = random.choice(range(4))

            choices.append(choice +1)
            reward = action_reward(choice)
            Qalast[choice] = Qnext(Qalast[choice],reward,numberaction[choice])
            numberaction[choice] = numberaction[choice] + 1
            Qa1.append(Qalast[0])
            Qa2.append(Qalast[1])
            Qa3.append(Qalast[2])
            Qa4.append(Qalast[3])
            Qkmatrix[t][r] = str(Qalast[choice])

        for i in range(4):
            numberaction_moyen[i] = numberaction_moyen[i] + numberaction[i]/(times * realization / 100)

        for i in range(times):
            Qa1list[i] += Qa1[i] /(times)
            Qa2list[i] += Qa2[i] /(times)
            Qa3list[i] += Qa3[i] /(times)
            Qa4list[i] += Qa4[i] /(times)


    Qk_moyen = [0]


    for index3,x in enumerate(Qkmatrix):
        rewardtot=0
        for index4,y in enumerate(x):
            rewardtot= rewardtot + float(Qkmatrix[index3][index4])
        moyennereward=(rewardtot/realization)
        Qk_moyen.append(moyennereward)

    Qk_list.append(Qk_moyen)
    numberaction_moyen_list.append(numberaction_moyen)
    Qa1totallist.append(Qa1list)
    Qa2totallist.append(Qa2list)
    Qa3totallist.append(Qa3list)
    Qa4totallist.append(Qa4list)

for Tau in Taulist: #SOFTMAX

    Qkmatrix = []
    numberaction_moyen = [0,0,0,0]
    Qa1list = []
    Qa2list = []
    Qa3list = []
    Qa4list = []

    for x in range(times): # creation des matrices board1, board 2 et matrice W
        Qkmatrix.append(["0"] * realization)
        Qa1list.append(0)
        Qa2list.append(0)
        Qa3list.append(0)
        Qa4list.append(0)

    for r in range(realization):
        #print ("Realization = ", r)

        numberaction = [0,0,0,0] # dans la boucle non?
        Qalast = [0, 0, 0, 0] # dans la boucle non?

        Qa1 = []
        Qa2 = []
        Qa3 = []
        Qa4 = []

        choices = []
        choice = random.choice(range(4))
        choices.append(choice+1) #afin d'avoir le num de l'action, plus facile a lire

        reward = action_reward(choice) #choisis une action au hasard
        numberaction[choice] = numberaction[choice] + 1 #ajoute 1 au decompte des actions
        Qalast[choice] = reward #modifie le Qa en position dependant du choix
        Qa1.append(Qalast[0])
        Qa2.append(Qalast[1])
        Qa3.append(Qalast[2])
        Qa4.append(Qalast[3])
        Qkmatrix[0][r] = str(reward)  # ajoute la valeur aux Qk rassemblant tous les Qk.

        for t in range(1,times):

            choice = Tprobability(Tau)

            choices.append(choice +1)
            reward = action_reward(choice)
            Qalast[choice] = Qnext(Qalast[choice],reward,numberaction[choice])
            numberaction[choice] = numberaction[choice] + 1
            Qa1.append(Qalast[0])
            Qa2.append(Qalast[1])
            Qa3.append(Qalast[2])
            Qa4.append(Qalast[3])
            Qkmatrix[t][r] = str(Qalast[choice])

        for i in range(4):
            numberaction_moyen[i] = numberaction_moyen[i] + numberaction[i]/(times * realization / 100)

        for i in range(times):
            Qa1list[i] += Qa1[i] /(times)
            Qa2list[i] += Qa2[i] /(times)
            Qa3list[i] += Qa3[i] /(times)
            Qa4list[i] += Qa4[i] /(times)

    Qk_moyen = [0]


    for index3,x in enumerate(Qkmatrix):
        rewardtot=0
        for index4,y in enumerate(x):
            rewardtot= rewardtot + float(Qkmatrix[index3][index4])
        moyennereward=(rewardtot/realization)
        Qk_moyen.append(moyennereward)

    Qk_list.append(Qk_moyen)
    numberaction_moyen_list.append(numberaction_moyen)
    Qa1totallist.append(Qa1list)
    Qa2totallist.append(Qa2list)
    Qa3totallist.append(Qa3list)
    Qa4totallist.append(Qa4list)

#****************************Pour epsilon variant en fonction du temps*****************************

Qkmatrix = []
numberaction_moyen = [0,0,0,0]

Qa1list = []
Qa2list = []
Qa3list = []
Qa4list = []

for x in range(times): # creation des matrices board1, board 2 et matrice W
    Qkmatrix.append(["0"] * realization)
    Qa1list.append(0)
    Qa2list.append(0)
    Qa3list.append(0)
    Qa4list.append(0)

for r in range(realization):
    print ("Realization = ", r)

    numberaction = [0,0,0,0] # dans la boucle non?
    Qalast = [0, 0, 0, 0] # dans la boucle non?

    Qa1 = []
    Qa2 = []
    Qa3 = []
    Qa4 = []

    choices = []
    choice = random.choice(range(4))
    choices.append(choice+1)

    reward = action_reward(choice) #choisis une action au hasard
    numberaction[choice] = numberaction[choice] + 1 #ajoute 1 au decompte des actions
    Qalast[choice] = reward #modifie le Qa en position dependant du choix
    Qa1.append(Qalast[0])
    Qa2.append(Qalast[1])
    Qa3.append(Qalast[2])
    Qa4.append(Qalast[3])

    Qkmatrix[0][r] = str(reward)  # ajoute la valeur aux Qk rassemblant tous les Qk.

    for t in range(1,times):
        epsilon = 1/(math.sqrt(t))
        proba = probability(epsilon)
        if proba == "exploitation":
            for i in random.sample(range(len(Qalast)),len(Qalast)): #choisir au random un Q max (en cas d'egalite avec les voisins)
                if Qalast[i] == max(Qalast):
                    choice = i
        elif proba == "exploration":
            choice = random.choice(range(4))

        choices.append(choice +1)
        reward = action_reward(choice)
        Qalast[choice] = Qnext(Qalast[choice],reward,numberaction[choice])
        numberaction[choice] = numberaction[choice] + 1
        Qa1.append(Qalast[0])
        Qa2.append(Qalast[1])
        Qa3.append(Qalast[2])
        Qa4.append(Qalast[3])
        Qkmatrix[t][r] = str(Qalast[choice])

    for i in range(4):
        numberaction_moyen[i] = numberaction_moyen[i] + numberaction[i]/(times * realization / 100)
    for i in range(times):
        Qa1list[i] += Qa1[i] /(times)
        Qa2list[i] += Qa2[i] /(times)
        Qa3list[i] += Qa3[i] /(times)
        Qa4list[i] += Qa4[i] /(times)

Qk_moyen = [0]


for index3,x in enumerate(Qkmatrix):
    rewardtot=0
    for index4,y in enumerate(x):
        rewardtot= rewardtot + float(Qkmatrix[index3][index4])
    moyennereward=(rewardtot/realization)
    Qk_moyen.append(moyennereward)

Qk_list.append(Qk_moyen)
numberaction_moyen_list.append(numberaction_moyen)

Qa1totallist.append(Qa1list)
Qa2totallist.append(Qa2list)
Qa3totallist.append(Qa3list)
Qa4totallist.append(Qa4list)

# *******************************Softmax ppour Tau variant***************************************

Qkmatrix = []
numberaction_moyen = [0,0,0,0]
Qa1list = []
Qa2list = []
Qa3list = []
Qa4list = []

for x in range(times): # creation des matrices board1, board 2 et matrice W
    Qkmatrix.append(["0"] * realization)
    Qa1list.append(0)
    Qa2list.append(0)
    Qa3list.append(0)
    Qa4list.append(0)

for r in range(realization):
    #print ("Realization = ", r)

    numberaction = [0,0,0,0] # dans la boucle non?
    Qalast = [0, 0, 0, 0] # dans la boucle non?

    Qa1 = []
    Qa2 = []
    Qa3 = []
    Qa4 = []

    choices = []
    choice = random.choice(range(4))
    choices.append(choice+1) #afin d'avoir le num de l'action, plus facile a lire

    reward = action_reward(choice) #choisis une action au hasard
    numberaction[choice] = numberaction[choice] + 1 #ajoute 1 au decompte des actions
    Qalast[choice] = reward #modifie le Qa en position dependant du choix
    Qa1.append(Qalast[0])
    Qa2.append(Qalast[1])
    Qa3.append(Qalast[2])
    Qa4.append(Qalast[3])
    Qkmatrix[0][r] = str(reward)  # ajoute la valeur aux Qk rassemblant tous les Qk.

    for t in range(1,times):
        Tau = 4* (1000-t) / 1000
        choice = Tprobability(Tau)

        choices.append(choice +1)
        reward = action_reward(choice)
        Qalast[choice] = Qnext(Qalast[choice],reward,numberaction[choice])
        numberaction[choice] = numberaction[choice] + 1

        Qa1.append(Qalast[0])
        Qa2.append(Qalast[1])
        Qa3.append(Qalast[2])
        Qa4.append(Qalast[3])

        Qkmatrix[t][r] = str(Qalast[choice])

    for i in range(4):
        numberaction_moyen[i] = numberaction_moyen[i] + numberaction[i]/(times * realization / 100)
    for i in range(times):
        Qa1list[i] += Qa1[i] /(times)
        Qa2list[i] += Qa2[i] /(times)
        Qa3list[i] += Qa3[i] /(times)
        Qa4list[i] += Qa4[i] /(times)

Qk_moyen = [0]


for index3,x in enumerate(Qkmatrix):
    rewardtot=0
    for index4,y in enumerate(x):
        rewardtot= rewardtot + float(Qkmatrix[index3][index4])
    moyennereward=(rewardtot/realization)
    Qk_moyen.append(moyennereward)

Qk_list.append(Qk_moyen)
numberaction_moyen_list.append(numberaction_moyen)

Qa1totallist.append(Qa1list)
Qa2totallist.append(Qa2list)
Qa3totallist.append(Qa3list)
Qa4totallist.append(Qa4list)


# Reward per rounds
"""
plt.figure(1)
plt.subplot(223)
plt.plot(Qk_list[0], 'darkorange', label = 'Random')
plt.plot(Qk_list[1], 'k-', label = 'Epsilon-Greedy, E = 0')
plt.plot(Qk_list[2], 'b-', label = 'Epsilon-Greedy, E = 0.1')
plt.plot(Qk_list[3], 'r-', label = 'Epsilon-Greedy, E = 0.2')
plt.plot(Qk_list[4], 'g-', label = 'Softmax, T = 1')
plt.plot(Qk_list[5], 'm-', label = 'Softmax, T = 0.1')
plt.plot(Qk_list[6], 'c-', label = 'Epsilon-Greedy, E = 1/sqrt(t)')
plt.plot(Qk_list[7], 'y-', label = 'Softmax, T =  4 * (1000-T) / 1000')
legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
for i in legend.legendHandles:
    i.set_linewidth(4.0)
plt.title("N-armed Bandit")
plt.xlabel('Number of rounds')
plt.ylabel('Average reward')
plt.show()


# per arm:
graphperarm(2,Qa1totallist,1,2.3)
graphperarm(3,Qa2totallist,2,2.1)
graphperarm(4,Qa3totallist,3,1.5)
graphperarm(5,Qa4totallist,4,1.3)
"""

# Histogrammes:
histogramme(6,0,"Selection strategy: Random")
histogramme(7,1,"Selection strategy: Epsilon-Greedy, E = 0")
histogramme(8,2,"Selection strategy: Epsilon-Greedy, E = 0.1")
histogramme(9,3,"Selection strategy: Epsilon-Greedy, E = 0.2")
histogramme(10,4,"Selection strategy: Softmax, T = 1")
histogramme(11,5,"Selection strategy: Softmax, T = 0.1")
histogramme(12,6,"Selection strategy: Epsilon-Greedy, E = 1/sqrt(t)")
histogramme(13,7,"Selection strategy: Softmax, T =  4 * (1000-T) / 1000")

