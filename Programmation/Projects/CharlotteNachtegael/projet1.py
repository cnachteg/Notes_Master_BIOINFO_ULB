34"""
INFO-F101 - Programmation
Projet 1 : M'enfin...
Programme pour calculer le temps de travail de Gaston lors d'une journée
"""
__author__= "Charlotte Nachtegael - 000425654 - Groupe TP 1"
__date__= "07 octobre 2015"


from random import randint, seed
s = int(input("Entrez la seed: "))
seed(s)

time = 540 #début de la journée
working_time = 0

print ("{0:02d}:{1:02d}".format(time//60,time%60), "Début de la journée")
print ("{0:02d}:{1:02d}".format(time//60,time%60), "Commençons bien la journée... avec une pause... *ronfle*")
time += 50 #commence toujours la journée par une pause
while time < 1080: #boucle jusqu'à ce qu'il soit 18h
	if randint(1,3) == 1: #Prunelle envoie un mail pendant la pause
		before_arrival = randint(10,60) #arrive au min 10min après la fin de la pause, au max 60min après la fin de la pause
		time_arrival = time + before_arrival
		print("{0:02d}:{1:02d}".format(time//60,time%60), "Alerte ! Prunelle va arriver à", "{0:02d}:{1:02d}".format(time_arrival//60,time_arrival%60))
		#calcul du temps de travail
		if time_arrival > 1080: #si l'heure d'arrivée est après 18h, ignore
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Comme si j'allais faire des heures sup', m'enfin !")
		elif before_arrival < 20: #Gaston travaille tout de suite
			working_time += before_arrival + 90
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Roooh, ben je vais travailler alors")
			time = time_arrival + 90
		elif before_arrival > 19 and before_arrival < 40: #pause 20 min et travaille
			print("{0:02d}:{1:02d}".format(time//60,time%60), "J'ai juste le temps pour une petite sieste !")
			time += 20
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Pfff... Allez, au travail !")
			working_time += before_arrival + 70
			time = time_arrival + 90
		elif before_arrival > 39 and before_arrival < 50: #pause de 40min et travaille
			print("{0:02d}:{1:02d}".format(time//60,time%60), "J'ai bien le temps pour une loooongue sieste")
			time += 40
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Allez, je travaille, un petit effor-ATCHOUM !")
			working_time += before_arrival + 50
			time = time_arrival + 90
		else: #Pause de 50 min et travaille
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Tant mieux pour lui !... Temps de faire un pause !")
			time += 50
			print("{0:02d}:{1:02d}".format(time//60,time%60), "Temps de travailler, m'enfin !")
			working_time += before_arrival + 40
			time = time_arrival + 90
		
		#après l'heure et demie de travail ou avoir ignoré l'email
		if time_arrival > 1080: #le mail est ignoré
			print ("{0:02d}:{1:02d}".format(time//60,time%60), "Bon, ben, pause !")
			time += 50
		else: #après le travail
			if time > 1080: #Prunelle part après 18h
				working_time = working_time - (time - 1080) #on retire les minutes de travail après 18h
				time = 1080
			else: #Prunelle part avant 18h
				print("{0:02d}:{1:02d}".format(time//60,time%60), "Prunelle est parti... LIBERTÉ °(-o-)°")
				print ("{0:02d}:{1:02d}".format(time//60,time%60), "Bon, ben, pause !")
				time += 50
	else: #Prunelle n'a pas envoyé d'email
		print ("{0:02d}:{1:02d}".format(time//60,time%60), "Bon, ben, pause !")
		time += 50
if time > 1080: #la fin de la journée est 18h
	time = 1080
print("{0:02d}:{1:02d}".format(time//60,time%60), "Fin de journée")
print("Temps total travaillé:", working_time//60,"h",working_time%60, "min")