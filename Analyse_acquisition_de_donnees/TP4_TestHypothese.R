##################################################################################
## Travaux pratiques: 3ème séance: rappel sur les tests d'hypothèse et le test
## de Student
##################################################################################

#1) Chargez le jeu de données iris
##################################################################################
data(iris)
str(iris)

#2) Calculez i) la moyenne de la longueur de sépales (que vous appellerez SepMn), 
# l'écart-type de cette moyenne (SepSd) et les bornes supérieures (SepMnUpperCI) 
# et inférieures (SepMnLowerCI) de l'intervalle de confiance de cette moyenne.  
# Calcul de la Moyenne
##################################################################################
SepMn = mean(iris$Sepal.Length)
# Calcul de l'écart-type
SepSd = sd(iris$Sepal.Length)
# Calcul de l'intervalle de confiance avec t de Student
myIC = qt(0.975, 149)* SepSd/(150^0.5)
# Calcul de la borne supérieure de l'intervalle de confiance
SepMnUpperCI = SepMn + myIC
# Calcul de la borne inférieure de l'intervalle de confiance
SepMnLowerCI = SepMn - myIC

#3) Selon vous, cette moyenne diffère-t-elle significativement de 0, pourquoi ? 
##################################################################################
# Oui, cette moyenne diffère signiticativement de zéro puisque 
# l'intervalle de confiance à 95% n'inclu pas zéro 

# 4)	Réalisez une boite de dispersion de la longueur de sépales en fonction de l'espèce. 
# Les longueurs de sépale sont-elles semblables entre les espèces ?
##################################################################################
boxplot(Sepal.Length ~ Species, data = iris)
# Non, les médianes des longueurs de sépale sont différentes selon les espèces
# En outre, les bornes des boites de dispersion (permier et troisième quartiles)
# de l'espèce setosa et versicolor ne se recoupent pas, il est donc très probable
# que ces différences soient significatives. Il y a un faible recouvement entre les limites
# des boites de dispersion de versicolor et virginica, et la différence entre ces deux espèces 
# semble donc moins importante.

#5) Construisez un jeux de donnée par espèce, à l'aide de la fonction subset(). 
##################################################################################
Ver = subset(iris, Species == "versicolor")
Set = subset(iris, Species == "setosa")
Vir = subset(iris, Species == "virginica")

#6)	Calculez la moyenne, l'écart-type, et les bornes supérieures et inférieures 
# de l'intervalle de confiance pour la longueur de sépales des individus de l'espèce 
# I. versicolor, et de l'espèce I. setosa. 
##################################################################################
# Versicolor
VerMean = mean(Ver$Sepal.Length)
VerSD = sd(Ver$Sepal.Length)
VerIC = qt(0.975, 49)* VerSD/(50^0.5)
VerUpperIC = VerMean + VerIC
VerLowerIC = VerMean - VerIC
# Setosa
SetMean = mean(Set$Sepal.Length)
SetSD = sd(Set$Sepal.Length)
SetIC = qt(0.975, 50)* SetSD/(50^0.5)
SetUpperIC = SetMean + SetIC
SetLowerIC = SetMean - SetIC

# 7)	Selon vous, les moyennes de longueur de sépale de ces deux espèces peuvent-elles
# être égales ? Justifiez votre réponse sur base des valeurs estimées au point 6)
##################################################################################
# Lorsque l'on construit les intervalle des confiance autour de ces deux
# moyennes, on constate qu'il n'y a pas de recouvrement, il est donc extrèmement 
# peu probable que ces moyennes soient égales.

# 8)	La fonction t.test() permet de faire un test t de comparaison de moyenne entre 
# deux séries d'observations. A l'aide des jeux de données créés au point 5) faites les 
# tests suivants pour comparer les longueurs de sépales:
#a.	Comparaison de moyenne de  I. versicolor et de I. setosa, test bilatéral
#b.	Comparaison de moyenne de  I. versicolor et de I. setosa, test unilatéral
#c.	Comparaison de moyenne de  I. versicolor et de I. virginica, test bilatéral
#d.	Comparaison de moyenne de  I. virgnica et de I. setosa, test bilatéral
##################################################################################
#8.1) Test t de comparaison de moyennes
t.test(Ver$Sepal.Length, Set$Sepal.Length)
# On rejette H0 au profit de H1: les moyennes sont différentes
#8.2)
t.test(Ver$Sepal.Length, Set$Sepal.Length, alternative = "greater")
# On rejette H0 au profit de H1: la moyenne des longueurs de sépales de Versicolor 
# est supérieure à celle de Setosa
#8.3)
t.test(Ver$Sepal.Length, Vir$Sepal.Length)
# On rejette H0 au profit de H1: les moyennes sont différentes
#8.4)
t.test(Vir$Sepal.Length, Set$Sepal.Length)
# On rejette H0 au profit de H1: les moyennes sont différentes

# 9) Tapez les commandes suivantes
##################################################################################
myseq = seq(from = -15, to = 15,by = 0.1)
plot(myseq, dt(myseq, 86.538), type = "l",
ylim = c(0,0.5), xlim = c(-15,15),
ylab = "Density", xlab = "Quantile")

# 10)	Selon vous, qu'est-ce qui est représenté ici ?  
##################################################################################
# Ce qui est représenté ici, c'est la distribution des valeurs prises par la
# distribution t de Student sous H0 pour le premier des tests t réalisés ci-dessus. 
# On peut reporter la valeur de la statistiques observée pour ce test t = 10.521
# sur l'axe des x, et constater qu'obtenir une telle valeur de t sous H0 est hautement 
# improbable, et bien à droite de la valeur de t correspondant à un seuil alpha de 0.05,
# ce qui confirme que l'on a bien une différence significative entre les deux moyennes.
 

# 11)  A l’aide de la fonction ‘power.t.test()’ faite un calcul de puissance du test t, 
# pour une différence de moyenne de 1, et un écart-type correpondant à la moyenne des 
# écart-types des 3 espèces. La puissance du test vous semble-t-elle bonne ? 
##################################################################################
# Calcul de la moyenne des trois écart-types
meansd = mean(sd(Vir$Sepal.Length),sd(Set$Sepal.Length),sd(Ver$Sepal.Length))
# Calcul de la puissance avec 50 observations par échantillon, et un effet de 1
power.t.test(50, delta = 1, sd = meansd)
# Oui, on a une puissance qui vaut 1, donc il serait impossible de passer à côté d'un tel
# effet.

# Quelle serait cette puissance s’il n’y avait que 5 mesures par espèce ?
##################################################################################
power.t.test(5, delta = 1, sd = meansd)
# La puissance serait réduite à 0.58, donc il y aurait une assez grande probabilité
# (p = 0.411) de se tromper en concluant à l'absence d'effet avec un échantillon de
# si petite taille.



