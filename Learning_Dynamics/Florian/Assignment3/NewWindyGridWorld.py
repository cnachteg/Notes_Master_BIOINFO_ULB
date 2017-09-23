__author__ = 'FlorianP'

import random

import matplotlib.pyplot as plt
import numpy as np

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

def choixduvoisin(choice,xlist,ylist):
    x = xlist[-1]
    y = ylist[-1]
    if choice == 0: #nord
        x += -1
    elif choice == 1:
        x +=  -1
        y +=  +1
    elif choice == 2:#est
        y += +1
    elif choice == 3:
        x += +1
        y += +1
    elif choice == 4: # sud
        x += +1
    elif choice == 5: #sud ouest
        x += +1
        y += -1
    elif choice == 6:#ouest
        y += -1
    elif choice == 7: #nord ouest
        x += -1
        y += -1

    if x < 0:
        x = 0
    elif x > 6:
        x = 6

    if y < 0:
        y = 0
    elif y > 11:
        y = 11

    return (x,y)

def vent(x,y,xnext,ynext): # a modifier et integrer
    if y== 2 or y == 3 or y == 4 or y ==7:
        xnext = xnext + random.choice ([0,-1,-2]) #le vent valant 1
        if xnext < 0:
            xnext = 0
    elif y == 5 or y == 6:
        xnext = xnext + random.choice([-1,-2,-3]) #le vent valant 2"""
    if xnext < 0:
        xnext = 0
    return xnext

numberofstates = 12*7
numberofactions = 8


gamma = 0.9
alpha = 0.1
episodes = 5000
reward = -1

epsilon = 0.2

numberoftests = []
rewardperepisodes = []

Qboard = []
for j in range(7): # creation de la matrice Qboard, gridworld
    Qboard.append([0] * 12)


coordinatelist = []
for j in range(7):
    for k in range(12):
        coordinatelist.append((j,k))

Qdico = {} #dico coordonees en fonction des actions
for i in range (len(coordinatelist)):
    Qdico[coordinatelist[i]] = [0,0,0,0,0,0,0,0]

for t in range(episodes):
    print("episodes", t)

    xlist = [3] #start
    ylist = [0] #start

    while ((xlist[-1] != 3)  | (ylist[-1] != 9)):

        proba = probability(epsilon)
        Qlist = Qdico[(xlist[-1],ylist[-1])]
        if proba == "exploitation":
           # print (Qlist)
            for i in random.sample(range(len(Qlist)),len(Qlist)): #choisir au random un Q max (en cas d'egalite avec les voisins)
                if Qlist[i] == max(Qlist):
                    actionchoice = i

        elif proba == "exploration":
            actionchoice = random.choice(range(8))

        xvoisin,yvoisin = choixduvoisin(actionchoice,xlist,ylist)

        xvoisinvent = vent(xlist[-1],ylist[-1],xvoisin,yvoisin)

        xlist.append(xvoisinvent)
        ylist.append(yvoisin)
        #calculer le Qmax
        Qmax = max(Qdico[(xvoisin,yvoisin)])

        if xlist[-1] == 3 and ylist[-1] == 9:
            reward = 10
        else:
            reward = -1

        Qdico[(xlist[-2],ylist[-2])][actionchoice] = Qdico[(xlist[-2],ylist[-2])][actionchoice]  + alpha * (reward + gamma * Qmax - Qdico[(xlist[-2],ylist[-2])][actionchoice])

    numberoftests.append(len(xlist))
    rewardtotal = len(xlist) * (-1) + 11
    rewardperepisodes.append(rewardtotal)

print (xlist)
print (ylist)
print ("Nombre de tests au fil du temps", numberoftests)

# ******************************Trouve ton chemin*******************************************

print ('A la recherche du butin:')

xtrack = [3]
ytrack = [0]

while ((xtrack[-1] != 3) |  (ytrack[-1] != 9)):

    Qlist = Qdico[(xtrack[-1],ytrack[-1])]
   # print (Qlist)
    actionchoice = Qlist.index(max(Qlist))

    xvoisin,yvoisin = choixduvoisin(actionchoice,xtrack,ytrack)

    xvoisinvent = vent(xlist[-1],ylist[-1],xvoisin,yvoisin)

    xtrack.append(xvoisinvent)
    ytrack.append(yvoisin)














print ("xtrack :", xtrack)
print ("ytrack :",ytrack)

#************************************bestaction***************

listeaction = ('N','NE','E','SE','S','SW','W','NW')

for j in range(7):
    for k in range(12):
        Qlistfinal = Qdico[(j,k)]
        for i in random.sample(range(len(Qlistfinal)),len(Qlistfinal)): #choisir au random un Q max (en cas d'egalite avec les voisins)
            if Qlistfinal[i] == max(Qlistfinal):
                bestaction = i

        Qboard[j][k] = listeaction[bestaction]

print_board(Qboard)


plt.figure(1)
plt.plot(numberoftests, 'b', lw = 0.5)
plt.title("Number of steps to reach the goal \n with e = %.2f and g = %.2f" % (epsilon,gamma), size = 20)
plt.xlabel('Episodes', size = 20)
plt.ylabel('Number of steps', size = 20)
plt.show()


plt.figure(2)
plt.plot(rewardperepisodes, 'b', lw = 1.5)
plt.title("Reward per episode", size = 30)
plt.xlabel('Episodes', size = 20)
plt.ylabel('Reward', size = 20)
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,-300,10))
plt.plot((0,episodes), (0,0), 'k--', lw = 2)
plt.show()


