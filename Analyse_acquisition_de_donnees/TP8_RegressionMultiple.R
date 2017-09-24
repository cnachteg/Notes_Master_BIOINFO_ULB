##################################################################################
## Travaux pratiques: 7ème séance: la régression linéaire II
##################################################################################

# 1) Charge le jeu de données (chemin d'acces a mettre a jour)
##################################################################################
myD = read.delim("http://www.ulb.ac.be/sciences/lubies/downloads/ips.txt")
myD = na.omit(myD)

# 2.  Construire un nouvelle variable appelée LGIT qui comprends le logarithme en 
# base 10 (fonction log10()) de la variable myD$AVIT. A l'aide de la fonction as.factor(), 
# convertissez ensuite la variable myD$SUP en facteur.
##################################################################################
myD$LOGIT = log10(myD$AVIT + 1)
myD$SUP = as.factor(myD$SUP)

# 3.	Nous allons tout d'abord cartographier les sites de capture à l'aide des coordonnées. 
#La seconde ligne de commande représente des points avec une taille proportionnelle à la variable LGIT
##################################################################################
plot(Y_COORD ~ X_COORD, myD, pch = 16, col = rgb(0.5,0.5,1,0.3)) 
plot(Y_COORD ~ X_COORD, myD, pch = 16, col = rgb(0.5,0.5,1,0.3), cex = myD$LOGIT)

# 4.  A l'aide de la fonction lm(), construisez un modèle de régression multiple 
# qui prédit le nombre d'ips (variable AVIT) en fonction de toutes les variable 
# prédictives, à l'exception de SUP et des coordonnées X_COORD et Y_COORD. Appelez 
# ce modèle myFullReg et affichez le résumé de ce modèle. Ce modèle est-il satisfaisant ? Pourquoi ? 
##################################################################################
myReg = lm(AVIT ~ ACCQT + CLCC + CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR04 + MARR05, data = myD)
summary(myReg)

# Ce modèle n'est pas satisfaisant car il comprends de nombreuses variables non significatives
# qui ne contribuent donc pas utilement à la prédiction du nombre de scolytes.

# 5.	Les fonctions suivantes vous permettent d'afficher le graphique quantile-quantile 
# des résidus, et le graphique des résidus. Les résidus se distribuent-il de manière normale ? 
# Sont-ils homogènes ?
##################################################################################
plot(myReg, which = 1)
plot(myReg, which = 2)

# Les résidus ne suivent clairement pas une distribution normale, puisqu'ils ne s'alignent
# pas du tout le long d'une ligne d'équivalence entre quantiles des résidus et quantiles d'une
# distribution normale. Par ailleurs, nous ne sommes pas non plus dans des conditions d'homoscédasticité,
# en effet, la variabilité des résidus augmente en même temps que les valeur prédite (forme de cône du 
# graphique des résidues).

# 6.	Construisez à présent le même modèle, mais en modélisant cette fois le 
# logarithme des captures (LGIT) et vérifiez à l'aide des deux graphiques illustrés 
# au point précédent si les conditions d'application ont été améliorées.
##################################################################################
myReg = lm(LOGIT ~ ACCQT + CLCC + CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR04 + MARR05, data = myD)
summary(myReg)
plot(myReg, which = 1)
plot(myReg, which = 2)
# La transformation log10 a clairement amélioré les choses du point de vue de l'homoscédasticité
# et de la normalité des données. Le graphique des résidus présente maintenant une répartition 
# plus homogène au fur et à mesure que les valeurs prédites augmentent. Pour vérifier la normailité 
# des résidus de manière plus formelle, nous pourrions réaliser un test de Shapiro.

# 7.	Simplifiez le modèle en enlevant successivement, pas à pas, les variables les moins 
# significatives (variables qui ont la valeur de t la plus faible en valeur absolue, et la 
# valeur de p la plus grande), jusqu'à aboutir à un modèle dans lequel toutes les variables 
# sont significatives. A quel modèle aboutissez-vous ? Pensez-vous qu'il s'agisse d'un bon modèle ?
##################################################################################
myFullReg = lm(LOGIT ~ ACCQT + CLCC + CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR04 + MARR05, data = myD)
summary(myFullReg)
myReg = lm(LOGIT ~ ACCQT + CLCC + CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR05, data = myD)
summary(myReg)
myReg = lm(LOGIT ~ ACCQT + CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR05, data = myD)
summary(myReg)
myReg = lm(LOGIT ~ CLCM + CLCF + OUVQL + EPIQLP + EPIQLD + MARR05, data = myD)
summary(myReg)
myReg = lm(LOGIT ~ CLCM + OUVQL + EPIQLP + EPIQLD + MARR05, data = myD)
summary(myReg)
myReg = lm(LOGIT ~ CLCM + OUVQL + EPIQLP + MARR05, data = myD)
summary(myReg)
# Oui et non. Le modèle est le meilleurs que nous puissions avoir avec les variables dont nous
# disposons puisque toutes les variables du modèle sont significatives. Le modèle est globalement significatif,
# mais la proportion de variabilité prédite est relativement faible, avec seulement 33.3%.

# 8.	La fonction step() permet d'automatiser la procédure de sélection des variables. Reprenez 
# le modèle de régression myFullReg du point 4, et utilisez ensuite la fonction suivante. 
# L'algorithme a-t-il abouti au même modèle que vous ?
##################################################################################
myStepReg = step(myFullReg, direction = "both")
summary(myStepReg)
# Non, la procédure step a été plus prudente dans l'exclusion des variables et nous présente
# un modèle avec certaines variables qui sont proches du seuil de significativité. Nous aurions 
# intérêt à simplifier encore ce modèle en enlevant les variables OUVQL et EPIQL (pour autant 
# que cette dernière ne soit toujours pas significative après avoir enlevé OUVQL).

# 9.	Ajoutez à présent la variable support (SUP) à votre modèle trouvé au point 7, et 
# appelez ce modèle myFinalReg. Comme vous l'avez vu au point 1, il s'agit d'une variable 
# qualitative à trois niveaux. En examinant le summary() de votre modèle, comment cette 
# variable a-t-elle été incorporée ?
##################################################################################
myFinalReg = lm(LOGIT ~ SUP + CLCM + OUVQL + EPIQLP + MARR05, data = myD)
summary(myFinalReg)
plot(myFinalReg, which = 1)
plot(myFinalReg, which = 2)
# La variable SUP a été incorporée via l'ajout de 2 nouvelles variables binaires (0/1)
# qui décrivent si l'on est un support de type 2 (SUP2), ou de type 3 (SUP3), sachant
# que si l'on est ni SUP2, ni SUP3, on est forcément SUP1.

# 10.	La ligne de commande suivante vous permet d'afficher une analyse de variance 
# sur votre régression. Quelle différence pouvez-vous observer par rapport au summary() 
# de votre modèle.
##################################################################################
summary(aov(myFinalReg))
# Cette analyse nous permet de montrer que la variable SUP (tous niveaux confondus)
# est globalement significative dans le modèle. 


# 11. Nous allons à présent installer une librairie supplémentaire, appellée ncf, la charger,
# puis calculer le corrélogramme des résidus de cette régression. Selon-vous, qu'est-ce qui est 
# représenté ici ?
##################################################################################
install.packages("ncf")
library("ncf")
myD$res = residuals(myFinalReg)
myCorr <- correlog(myD$X_COORD, myD$Y_COORD, myD$res,na.rm=T, increment=500,resamp=0, latlon = F)
plot(myCorr$mean.of.class[1:30],myCorr$correlation[1:30], ylim = c(-0.1,1), type = "b", xlab = "distance (m)", ylab = "correlation")

# Ce corrélogramme montre comment l'autocorrélation spatiale des résidus diminue en fonction 
# de la distance qui sépare les points. Les points séparés par des distance de 500 m (premier point)
# du graphique ont une corrélation de 0.5, dont les résidus voisins géographiquement ne sont 
# pas indépendants. En revanche, les points séparés par des distance > 2500 m ont une
# autocorrélation spatiale proche de zéro. Il y aurait donc lieu, de soit sous-échantillonner 
# pour ne conserver que les points séparés par des distance > 2500 m, soit de construire un modèle
# adapté pour prendre en compte cette autocorrélation spatiale (pas vu au cours).





