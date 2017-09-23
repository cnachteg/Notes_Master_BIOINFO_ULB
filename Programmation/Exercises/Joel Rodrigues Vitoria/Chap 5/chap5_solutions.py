# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:16:46 2015

@author: Joel Rodrigues Vitoria
"""

#Écrivez une fonction my_insert qui prend une liste triée sorted_list et un 
#entier n en paramètres. La fonction devra renvoyer une liste correspondant à 
#la liste reçue triée par ordre non décroissant, où n a été insérée tout en la 
#maintenant triée. Vous pouvez supposer que la liste est bien formée de valeurs 
#entières triées. Essayer de tester les autres cas d'erreur et dans ce cas de 
#renvoyer None.


def my_insert(sorted_list, n):
    try:
        if type(n)==type(1):
            sorted_list.append(n)
            return sorted(sorted_list)
    except:
        return None


#Même exercice que le précédent, mais ici la fonction modifie la liste donnée 
#en paramètre et renvoie None.
#Quelle version entre celle-ci et celle de l'exercice précédant est la plus 
#"propre" au niveau du style de programmation ?

def my_insert(sorted_list, n):
    if type(n)==type(1):
        sorted_list.append(n)
        return sorted_list.sort()
    else:
        raise ValueError('N is not an integer')
    
#Écrivez une fonction my_count qui prend une liste lst et un élément e en 
#paramètres. La fonction doit renvoyer le nombre de fois que l’élément e 
#apparaît dans la liste. 0 est retourné si my_count n'a pas le bon type.

def my_count(lst, e):
    try:
        return lst.count(e)
    except:
        return 0

#Ecrivez une fonction my_remove qui prend une liste lst et un élément e en 
#paramètre et qui effacera la première apparition de l'élément e dans la liste.
# N'oubliez pas de tester tous les cas possibles. Définissez une version qui 
# modifie lst et renvoie None et une autre qui ne modifie pas lst et renvoie 
# la liste modifiée.


def my_remove(lst, e):
    try:
        lst2 = lst
        lst2.pop(lst2.index(e))
        return lst2
    except:
        raise ValueError('Error occured')

def my_remove(lst, e):
    try:
        lst.pop(lst.index(e))
    except:
        raise ValueError('Error occured')

#Ecrivez une fonction my_map qui prend une liste lst et une fonction f en 
#paramètres et qui renverra une nouvelle liste où un élément à la i-ieme position 
#contiendra la valeur de retour de la fonction f appliquée au i-ieme élément de la 
#liste lst. A nouveau, n'oubliez pas de tester tous les cas possibles.

def my_map(lst, f):
    for i in range(len(lst)):
        lst[i] = f(lst[i])
    return lst
        
#Ecrivez une fonction my_filter qui prend une liste lst et une fonction f en 
#paramètres. Cette fonction renverra une nouvelle liste constituée des éléments 
#de la liste lst pour lesquels la fonction f renvoie True.


def my_filter(lst, f):
    return [x for x in lst if f(x)==True]

#Ecrivez une fonction my_enumerate qui prend une liste lst en paramètre. Cette 
#fonction renverra une liste de tuples à deux composantes. Chaque tuple devra 
#avoir en premier élément l'indice i et en deuxième élément le i-ieme élément 
#de la liste lst. Veuillez tester votre programme et repérer clairement ses 
#limites d'utilisation.

def my_enumerate(lst):
    rlst = []
    for i in range(len(lst)):
        rlst.append((i,lst[i]))
    return rlst
    
#Ecrivez une fonction my_reduce qui prend en paramètres une liste lst, une fonction 
#f (à deux paramètres) et un élément e. La fonction devra être initialement 
#appliquée à l'élément e et au premier élément de la liste lst. Ensuite, il 
#faudra successivement appliquer la fonction f sur le résultat du précédent appel 
#de fonction et l'élément suivant de la liste. Si la liste est vide le résultat est e.
#Exemple : reduce([1,2,3,4], somme, 0) où somme est défini par
#def somme(a,b):
#   return a+b
#renverra 10 (((((0+1)+2)+3)+4))
    
def my_reduce(lst, f, e):
    if lst:
        result=f(e, lst[0])
        for i in range(1,len(lst)):
            result = f(result, lst[i])
        return result
    else:
        return e

#Ecrivez une fonction my_print qui prend en paramètres une séquence lst et un 
#tuple separator de taille 3. La fonction devra afficher une chaîne de caractères 
#contenant dans l'ordre :
#le premier élément de separator ;
#chaque élément de la séquence lst en insérant, entre chaque élément, le deuxième 
#élément de separator ;
#le troisième élément de separator.
#Exemple:
#>>> my_print([1, 2, 3, 4], ('[', '->', ']'))
#affichera
#[1->2->3->4]

def my_print(lst, sep):
    if lst:
        string = sep[0]
        for i in lst[:-1]:
            string += str(i)
            string += sep[1]
        string+= str(lst[-1])
        string += sep[2]
        print(string)
    else:
        print(sep[0]+sep[2])

#Ecrivez une fonction my_invert qui inverse (en place) l'ordre des éléments 
#dans une liste lst qui lui est donnée en paramètre sans utiliser une autre 
#structure telle qu'une autre liste. Exemple:
#my_invert([1, 2, 3, 4])
#renverra
#[4,3,2,1]

def my_invert(lst):
    rlist = []
    for i in range(-1, -len(lst)-1, -1):
        rlist.append(lst[i])
    return rlist
    
#On se donne une liste qui encode une séquence t. Chaque élément de cette liste 
#est un tuple de deux éléments: le nombre de répétitions successives de l'élément 
#x dans t, et l'élément x lui-même. Les éléments successifs répétés forment la 
#séquence t.
#Ecrivez une fonction decompresse, qui reçoit une telle liste en paramètre et 
#renvoie la séquence t sous forme d'une nouvelle liste.
#Exemple~:
#>>> ll = [(4, 1), (2, 2), (2, 'test'), (3, 3), (1, 'bonjour')]
#>>> decompresse (ll)
#[1, 1, 1, 1, 2, 2, 'test', 'test', 3, 3, 3, 'bonjour']

def decompresse(ll):
    rlist=[]
    for t in ll:
        for i in range(t[0]):
            rlist.append(t[1])
    return rlist