from random import randint
import random
import matplotlib.pyplot as plt

board1 = []
board_W1 = []
board2 = []
total_cooperators_turn = []
moyenne_cooperators_turn = []


realization = 100

nbre_de_c = 120
tour = 1000

S = -0.5
T = 0.5

def print_board(board):
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def change_value_board(board_before,board_after,x,y):
    if board1[index1][index2] != board1[ind1][ind2]:
        if board_before[x][y] == "1":
            possibility = ['0'] * round((1 + (Wj - Wi) / (4* ( max(0,1,T,S) - min(0,1,T,S) ))) / 2  * 100) + ['1'] * round((1- ((1 + (Wj - Wi) / (4* ( max(0,1,T,S) - min(0,1,T,S) ))) / 2))*100)
            board_after[x][y] = random.choice(possibility)
        elif board_before[x][y] == "0":
            possibility = ['1'] * round((1 + (Wj - Wi) / (4* ( max(0,1,T,S) - min(0,1,T,S) ))) / 2  * 100) + ['0'] * round((1- ((1 + (Wj - Wi) / (4* ( max(0,1,T,S) - min(0,1,T,S) ))) / 2))*100)
            board_after[x][y] = random.choice(possibility)
    elif board1[index1][index2] == board1[ind1][ind2]:
        board2[index1][index2] = board1[index1][index2]


def Calculer_W_dans_board_W(index1,index2,board,board_W):
    if board[index1][index2] == "0":
        if result == 0:
            W = 0
            board_W[index1][index2] = str(W)
        elif result == 1:
            W = 1 * T
            board_W[index1][index2] = str(W)
        elif result == 2:
            W = 2 * T
            board_W[index1][index2] = str(W)
        elif result == 3:
            W = 3 * T
            board_W[index1][index2] = str(W)
        elif result == 4:
            W = 4 * T
            board_W[index1][index2] = str(W)
    if board[index1][index2] == "1":
        if result == 0:
            W = 4 * S
            board_W[index1][index2] = str(W)
        elif result == 1:
            W = 3 * S + 1  
            board_W[index1][index2] = str(W)                  
        elif result == 2:
            W = 2 * S + 2
            board_W[index1][index2] = str(W)
        elif result == 3:
            W = 1 * S + 3
            board_W[index1][index2] = str(W)
        elif result == 4:
            W = 4
            board_W[index1][index2] = str(W)


for x in range(20): # création des matrices board1, board 2 et matrice W
    board1.append(["0"] * 20)
    board2.append(["0"] * 20)
    board_W1.append(["0"] * 20)

for x in range(tour): # création des matrices board1, board 2 et matrice W
    total_cooperators_turn.append(["0"] * realization)

for r in range (realization): #nbre de répétitions du test
    print("Realization : ", r)
    

    
    
    for index1,x in enumerate(board1): #reset du board1
        for index2, y in enumerate(x):
            board1[index1][index2]="0"

    for C_number in range(nbre_de_c): #nombre de C initial dans la matrice
        end = "0"
        while end == "0":
            x = random_row(board1)
            y = random_col(board1)
            if board1[x][y] == "0":
                board1[x][y] = "1"
                end = "1"


    for t in range(tour): #nbre de tours dans un même test
        
        total_cooperators = 0 #d[t][r]= str(total_cooperators)
        for index1,x in enumerate(board1):
            for index2,y in enumerate(x):
                if board1[index1][index2] == "1":
                    total_cooperators += 1
        total_cooperators_turn[t][r] = str(total_cooperators)


        for index1,x in enumerate(board1): #Création de la matrice W1
            if 0 < index1 < 19:
                for index2,y in enumerate(x):
                    if 0< index2 < 19:
                        result = int(board1[index1][index2-1]) + int(board1[index1][index2+1]) + int(board1[index1+1][index2]) + int(board1[index1-1][index2])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1)
                    elif index2 == 19:
                        result = int(board1[index1][index2-1]) + int(board1[index1+1][index2]) + int(board1[index1-1][index2]) + int(board1[index1][0])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1) 
                    elif index2 == 0:
                        result = int(board1[index1][index2+1]) + int(board1[index1+1][index2]) + int(board1[index1-1][index2]) + int(board1[index1][19])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1)
            elif index1 == 19:
                for index2,y in enumerate(x):
                    if 0< index2 < 19:
                        result = int(board1[index1][index2-1]) + int(board1[index1][index2+1]) + int(board1[index1-1][index2]) + int(board1[0][index2])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1)   
                    elif index2 == 19:
                        result = int(board1[index1][index2-1]) + int(board1[index1-1][index2]) + int(board1[index1][0]) + int(board1[0][index2])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1) 
                    elif index2 == 0:
                        result = int(board1[index1][index2+1]) + int(board1[index1-1][index2]) + int(board1[index1][19]) + int(board1[0][index2])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1)
            elif index1 == 0:
                for index2,y in enumerate(x):
                    if 0< index2 < 19: 
                        result = int(board1[index1][index2-1]) + int(board1[index1][index2+1]) + int(board1[index1+1][index2]) + int(board1[19][index2])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1) 
                    elif index2 == 19:
                        result = int(board1[index1][index2-1]) + int(board1[index1+1][index2]) + int(board1[19][index2]) + int(board1[index1][0])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1) 
                    elif index2 == 0:
                        result = int(board1[index1][index2+1]) + int(board1[index1+1][index2]) + int(board1[19][index2]) + int(board1[index1][19])
                        Calculer_W_dans_board_W(index1,index2,board1,board_W1)

        for index1,x in enumerate(board2): #Création de la matrice board2
            if 0 < index1 < 19:
                for index2,y in enumerate(x):
                    if 0< index2 < 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1,index2 - 1),(index1 +1,index2),(index1 -1,index2)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2)

                    elif index2 == 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 - 1),(index1 +1,index2),(index1 -1,index2),(index1,0)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2)
                    elif index2 == 0:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1 +1,index2),(index1 -1,index2),(index1,19)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2)
            elif index1 == 19:
                for index2,y in enumerate(x):
                    if 0< index2 < 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1,index2 - 1),(index1 -1,index2),(0,index2)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2)   
                    elif index2 == 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 - 1),(index1 -1,index2),(0,index2),(index1,0)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2) 
                    elif index2 == 0:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1 -1,index2),(0,index2),(index1,19)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2)
            elif index1 == 0:
                for index2,y in enumerate(x):
                    if 0< index2 < 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1,index2 - 1),(index1 +1,index2),(19,index2)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2) 
                    elif index2 == 19:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 - 1),(index1 +1,index2),(19,index2),(index1,0)])
                        Wj = float(board_W1[ind1][ind2])
                        change_value_board(board1,board2,index1,index2) 
                    elif index2 == 0:
                        Wi = float(board_W1[index1][index2])
                        ind1, ind2 = random.choice([(index1,index2 + 1),(index1 +1,index2),(19,index2),(index1,19)])
                        Wj = float(board_W1[ind1][ind2]) 
                        change_value_board(board1,board2,index1,index2)#Création de la matrice board2:
       
        board1 = board2



for index3,x in enumerate(total_cooperators_turn):
    total=0
    for index4,y in enumerate(x):
        total= total + float(total_cooperators_turn[index3][index4])
    moyenne=(total/realization)/4
    moyenne_cooperators_turn.append(moyenne)
print (moyenne_cooperators_turn)


plt.plot(moyenne_cooperators_turn)
plt.title("%i%% C and %i%% D at start, in %i rounds, S = %.1f, T = %.1f" % ((nbre_de_c/4), 100 - (nbre_de_c/4), tour, S, T))
plt.xlabel('Number of rounds')
plt.ylabel('Percentage of C in population')
plt.show
