##################################################################################
## Travaux pratiques: 6ème séance: la régression linéaire I
##################################################################################

# 1)  Chargez le jeu de données ‘faithful’ et faites un graphique de la durée des 
# éruption du geyser en fonction du temps d’attente.
##################################################################################
data(faithful)
str(faithful)
plot(eruptions~waiting, data = faithful)

# 2) La fonction ‘lm()’ qui génère un objet de type « régression linéaire » s’écrit de la 
# même manière que la fonction ‘aov()’ utilisée précédemment. Utilisez cette fonction 
# ainsi que la fonciton abline() pour construire une régression linéaire.
##################################################################################
mylm = lm(eruptions~waiting, data = faithful)
abline(mylm)

# 3) En fonction des éléments vus au cours, détaillez les éléments fournis par la fonction 
# ‘summary()’ appliqué à l’objet régression.
##################################################################################
summary(mylm)

# La fonction nous permet d'afficher l'ordonnée à l'origine de la droite de régression (-1.87),
# le coéficient angulaire de la droite (0.075), leurs statistiques t respectives, et la probabilité
# d'obtenir une statistique t supérieure à celle-là sous H0 (ordonnées à l'origine nulle et pente nulle, 
# respectivement). Ici, on peut dans les deux cas rejeter H0 avec un seuil alpha de 0.001.
# La fonction nous affiche également le coéficient de détermination R-squared, et l'on
# voit dont que 81.1 % de la variabilité est expliquée par la droite de régression. Enfin, la régression
# est globalement significative, puisque qu'il est très hautement peu probable (p < 10^-16) d'obtenir
# un statistique de F supérieure à celle-ci (1162) si H0 était vrais.



# 4)	Chargez le jeu de données " longley ". A l'aide de la fonction pairs(), 
# examinez les relations bi-variées entre ces variables. Quelle variables selon 
# vous devrait permettre de prédire de number de personnes ayant un emplois ? 
# (variable " Employed ")
##################################################################################
data(longley)
pairs(longley)

# Les variables GNP.deflator, GNP, Population et Year semblent être des variables
# qui permettraient de prédire la variable "Employed" avec un bon niveau de précision


# 5)  A l'aide de cette fonction, faites une régression du nombre de personnes employées 
# en fonction de l'année d'une part (" Year "), et du PNB d'autre part (variable " GNP ").
# Comment interprétez-vous ces deux régressions ? L'une vous semble-t-elle préférable 
# à l'autre ? Pourquoi ?
##################################################################################
myReg = lm(Employed ~ Year, longley)
summary(myReg)
plot(Employed ~ Year, longley)
abline(myReg)

myReg = lm(Employed ~ GNP, longley)
summary(myReg)
plot(Employed ~ GNP, longley)
abline(myReg)

# Les deux régressions sont globalement significatives. En effet la valeur de p associée 
# à la statistique F est dans les deux cas inférieure au seuil alpha de 5%. Les deux régressions
# présentent une ordonnées à l'origine significativement différente de zéro (valeur de p associée
# au test t sur l'intercept < 0.05), et une pente de la droite significativement différente de zéro
# (valeur de p associée au test t sur le coéficient < 0.05). Les deux régressions expliquent une très 
# grande proportion de la variabilité (R2 > 90%. Cependant, la seconde régression présentant un R2
# légèrement plus élevé, elle est à privilégier. 

# 6).	Ajoutez la variable " Armed.Forces " à votre modèle de régression. Cela améliore-t-il 
# le modèle ? A-t-on des raisons de conserver cette variable ?
##################################################################################
myReg = lm(Employed ~ GNP +  Armed.Forces, longley)
summary(myReg)

# La variable Armed.forces ne présente pas un coéficient significativement
# différent de zéro (valeur de p associée à la statistique t > 0.05). On a donc
# aucune raison de maintenir cette variable dans le modèle.

# 7) Ajoutez la variable " Population " à votre modèle de régression. Cela améliore-t-il 
# le modèle ? A-t-on des raisons de conserver cette variable ?
##################################################################################
myReg = lm(Employed ~ GNP + Population, longley)
summary(myReg)

# Cette fois-ci, cette seconde variable améliore légèrement le modèle. En effet, elle 
# a une pente significativement différente de zéro au seuil alhpa de 5%, et le R2 est passé de 0.9674 à 0.9791. 
# On a donc gagné en prédictabilité. Ce gain est mineur, mais significatif

# 8)	Calculez le taux d'emploi, et étudiez si l'année, la population totale, 
# les personnes employées par l'armée, et le PNB permettent de prédire le taux 
# d'emplois. Peut-on simplifier ce modèle ?
##################################################################################
longley$EmpRate = longley$Employed / (longley$Employed + longley$Unemployed)
myReg = lm(EmpRate ~ GNP + Population + Year + Armed.Forces, longley)
summary(myReg)

# On peut simplifier le modèle en enlevant la variable Population qui n'est pas 
# significative.

myReg = lm(EmpRate ~ GNP + Year + Armed.Forces, longley)
summary(myReg)

# Toutes les variables du modèle sont significatives. On ne peut plus simplifier.
# On obtient un modèle final qui est globalement significatif, et qui prédit 92.9% de 
# la variabilite. Il faudra en outre vérifier les conditions d'application de la 
# régression linéaire (cf séance suivante)

# 9) A l’aide la fonction plot(myReg, which = 1) et plot(myReg, which = 2) appliquée 
# à votre objet régression, et du test de Shapiro, vérifiez les conditions d’application 
# de votre modèle. Celles-ci vous semblent-elles rencontrées ?
##################################################################################
plot(myReg, which = 1)
# les résidus ont l'air relativement homogène, mais le nombre de points, très faible
# ne permet pas de se faire une bonne idée sur une base graphique.
plot(myReg, which = 2)
shapiro.test(residuals(myReg))
# Le test de Shapiro indique que les résidus ne semblent pas s'écarter de la normale.









