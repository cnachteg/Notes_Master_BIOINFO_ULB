# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:01:19 2015

@author: Joel Rodrigues Vitoria
"""

#Écrivez une fonction init_mat(m,n) qui construit une matrice d'entiers 
#initialisée à la matrice nulle et de dimension m×n.

def init_mat(m, n):
    mat = []
    for i in range(m):
        mat.append([0]*n)
    return mat

#Écrivez une fonction print_mat(M) qui prend une matrice en paramètre et affiche 
#son contenu.
#Affichez les éléments de chaque ligne de la matrice sans passer de ligne et 
#passez une ligne entre chaque nouvelle ligne de la matrice
#Remarque sur les données et les résultats affichés: notez que les matrices de 
#données sont générées à partir des strings fournis en input.

def print_mat(m):
    for i in m:
        print("".join(i))
        
#Écrivez une fonction trace(M) qui prend en paramètre une matrice M de taille n×n 
#et qui calcule sa trace de la manière suivante:
#trace(A)=∑i=1nAii

def trace(M):
    trace = 0
    for i in range(len(M)):
        trace += M[i][i]
    return trace

#Une matrice M={mij} de taille n×n est dite antisymétrique lorsque pour toute paire 
#d'indices i,j, on a mij=−mji. Ecrire une fonction booléenne antisymetrique qui teste 
#si une matrice est antisymétrique.

def antisymetrique(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != -M[j][i]:
                return False
    return True

#Écrivez une fonction produit_matriciel(A,B) qui calcule le produit matriciel C 
#(de taille m×ℓ) entre les matrices A (de taille m×n) et B (de taille n×ℓ). 
#Le produit matriciel se calcule comme suit :
#Cij=∑k=0n−1AikBkj

def produit_matriciel(M, N):
    mat = init_mat(len(M), len(N[0]))
    for i in range(len(M)):
        for j in range(len(N[0])):
            mat[i][j] = sum([M[i][l] * N[l][j] for l in range(len(N))])
    return mat

#Écrivez une fonction xor_matriciel(A,B) qui prend en paramètres deux matrices 
#A et B de même dimensions (de taille m×n), et qui renvoie une matrice résultant
# C contenant les éléments de A xorés aux éléments de B. Cette fonction opère 
# comme suit :
#Cij=Aij⊕Bij,∀i, j:0≤i<n et≤j<m

def xor_matriciel(A, B):
    mat = init_mat(len(A), len(A[0]))
    for j in range(len(A[0])):
        for i in range(len(A)):
            mat[i][j] = A[i][j] ^ B[i][j]
    return mat
    
#Écrivez une fonction rotation_gauche(A) qui prend en paramètre une matrice A 
#sur laquelle elle effectue des rotations gauche sur chaque ligne. Le nombre de 
#déplacements effectués par la rotation est fonction du numéro de la ligne en 
#question; Autrement dit, la ligne i subit une rotation de i positions.
#Comment adapteriez-vous cette fonction pour effectuer une rotation droite?
    
def rotation_gauche(M):
    col = len(M[0])
    for i in range(len(M)):
        line = M[i]*2
        M[i] = line[0+i:col+i]


#Examen de juin 2012
#Soit un tableau A à 3 dimensions de taille m×n×q contenant des entiers quelconques 
#et un tableau P de même taille contenant des entiers compris entre 0 et m×n×q−1, 
#tous distincts. On vous demande de réorganiser le tableau A de la manière suivante : 
#    l'élément à l'indice (a,b,c) du tableau A d'origine devra, après réorganisation, 
#    se trouver à la position numéro P[a][b][c] du tableau A. le tableau P est 
#    appelée tableau de permutation des éléments du tableau A. Chaque élément du 
#    tableau P à l'indice (a,b,c) contient la position où se trouvera l'élément 
#    (a,b,c) de A après l'ensemble des permutations.
#
#On définit la position d'un élément comme l'indice qu'aurait cet élément dans 
#un vecteur qui serait constitué des lignes de A mises côte-à-côte. Plus précisément, 
#la Figure 1 vous montre les positions des différents éléments se trouvant dans 
#un tableau A de dimension 3×3×2. On y voit par exemple que l'élément A[0][2][1] 
#(c'est-à-dire premier plan, troisième ligne, deuxième colonne) contient l'entier 
#7 et est donc en position 7. L'élément A[1][1][0] quant à lui est à la position 12.
#
#On vous demande d'écrire une fonction sol en Python qui reçoit les tableaux A 
#et P tel que décrit plus haut et qui permute les éléments du tableau A en fonction 
#du tableau de permutation P. Le traitement doit être effectué sans utiliser de 
#structure intermédiaire (c'est-à-dire pas de dictionnaire, pas de nouvelle liste 
#ou de tableau, etc.). En d'autres mots, vous avez le droit de modifier le tableau 
#A, le tableau P ainsi que d'utiliser des variables ne contenant que des entiers.
#La Figure 2 vous montre un exemple de tableau A, de tableau P et enfin d'un 
#tableau A′ qui est le tableau A après permutation des éléments grâce au tableau P.
# On y voit que l'entier 9 en position (1,0,2) dans le tableau A (i.e. A[1][0][2]) 
# doit se trouver en position 0 dans le tableau A après réorganisation 
# (donc en A[0][0][0]).

def sol (A, P):
    """ First : parses indexes. Second: transforms position value of P table into
    new_m, new_n and new_q coords. Third: adds value from A[m][n][q] table to
    A[new_m][new_n][new_q], creating a tuple. Forth: verifies every time if fetched
    value is already a tuple. If so, on value on index 0 is copied.
    Fifth: reparses the new A table and only keeps the second value of the tuples."""
    plan = len(A)
    ligne = len(A[0])
    col = len(A[0][0])
    for m in range(plan):
        for n in range(ligne):
            for q in range (col):
                permut_val = P[m][n][q]
                first_coord = divmod(permut_val, ligne * col)
                new_m = first_coord[0]
                sec_coord = divmod(first_coord[1], col)
                new_n = sec_coord[0]
                new_q = sec_coord[1]
                if type(A[m][n][q]) == type((1,2)):
                    A[new_m][new_n][new_q] = (A[new_m][new_n][new_q],A[m][n][q][0])
                else:
                    A[new_m][new_n][new_q] = (A[new_m][new_n][new_q],A[m][n][q])
    for m in range(plan):
        for n in range(ligne):
            for q in range (col):
                A[m][n][q] = A[m][n][q][1]