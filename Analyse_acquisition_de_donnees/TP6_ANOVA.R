##################################################################################
## Travaux pratiques: 4ème séance: l'ANOVA à 1 facteur
##################################################################################

# 1)	Chargez le jeu de données PlantGrowth
##################################################################################
data(PlantGrowth)
str(PlantGrowth)

# 2)	Affichez les boites de dispersion de la variable weight en fonction de la 
# variable de groupement. 
##################################################################################
boxplot(weight ~ group, data = PlantGrowth)
# Sur une base visuelle, on peut constater que la différence entre le traitement 1
# et le traitement 2 a l'air importante, puisqu'il n'y a pas de recouvrement entre
# les boîtes de dispersion. Il faudra cependant recourir au test statistique pour
# le prouver avec un seuil de probabilité déterminé.

#3)	La fonction ci-dessous réalise une analyse de variance et stocke les résultats 
# de celle-ci dans un objet appelé myAOV :
##################################################################################
myAOV = aov(weight ~ group, data = PlantGrowth)


# 4)	La fonction summary(myAOV) vous permet d'afficher les résultats de l'analyse 
# variance. Qu'est-ce qui a été testé ici ? Précisez les hypothèses H0 et H1. Quelles 
# sont les conclusions que vous pouvez tirer de ce test ?
##################################################################################
summary(myAOV)
# Il s'agit d'une ANOVA à un facteur à 3 niveaux, qui vise à comparer les moyennes
# de poids selon que les échantillons fassent partie du contrôle, du traitement 1 ou
# du traitement 2
# HO: les moyennes des poids du controle et des deux traitements sont égales;
# H1: au moins une des moyennes es différente des autres
# On obtient une valeur de p = 0.01591. Il y a donc une probabilité de 0.01591
# d'obtenir une valeur de F supérieure ou égale à 4.8461 si H0 était vrais. On peut 
# donc rejeter H0 au seuil alpha de 5%.

#5)	La fonction residuals(myAOV) vous renvoie les résidus de cette analyse. A l'aide 
# des fonctions hist(), qqnorm(), et shapiro.test(), vérifiez la normalité des résidus 
# de l'ANOVA.
##################################################################################
hist(residuals(myAOV))
qqnorm(residuals(myAOV))
qqline(residuals(myAOV))
shapiro.test(residuals(myAOV))
# Les quantiles des résidus ne sont pas parfaitement alignés sur la droite 
# de correspondance avec les quantiles d'une distribution normale. On a donc recours
# au test de Shapiro, dont H0: la variable suit une loi normale. La valeur de p du test
# étant égale à 0.4379, on ne rejette pas H0 au seuil alpha de 5%. Les conditions d'application
# de l'ANOVA sont donc respectées du point de vue de la normalité des résidus.  


# 6)	La fonction bartlett.test(weight ~ group, data = PlantGrowth), va nous permettre de 
# vérifier l'homogénéité des variances. Quelles sont les hypothèses H0 et H1 de ce test ? 
# Dans ce cas ci, les variances peuvent-elles être considérées comme égales ?
##################################################################################
bartlett.test(weight ~ group, data = PlantGrowth)
# H0: les variances des trois groupes sont égales
# H1: au moins une des variance différe des deux autres
# Oui, car la valeur de p > 0.05 nous indique que l'on ne rejette pas H0 au seuil
# alpha de 5%. Les conditions d'application de l'ANOVA sont donc respectées du point 
# de vue de l'homoscédasticité (homogénéité des variances). 

# 7)	Chargez le jeu de données InsectSprays et en utilisant les mêmes codes que dans 
# l'exemple précédent, testez l'effet des insecticides sur les nombres d'insectes observés. 
# Vérifiez la normalité des résidus et l'homoscédasticité. Avant même de procéder au test 
# de Bartlett, les variances semblent-elles égales ?
##################################################################################
data(InsectSprays)
boxplot(count ~ spray, InsectSprays)
# On voit déjà sur le boxplot que certains niveaux de la variable spray ont 
# des variabilités très différentes (indiquées par l'espace interquartile). Par eexemple,
# les niveaux C, D et E, ont apparement des variabilités beaucoup plus faibles que les 
# niveaux A, B et F
myAOV = aov(count ~ spray, InsectSprays)
summary(myAOV)
# L'analyse des variance montre un effet significatif du type de spray sur les 
# moyennes de nombres d'insectes.
hist(residuals(myAOV))
shapiro.test(residuals(myAOV))
# La valeur de p du test de Shapiro nous permet de rejetter H0 au seuil alpha de 5%, 
# les résidus ne suivent donc pas une loi normale.
bartlett.test(count ~ spray, InsectSprays)
# Le test de Bartlett nous permet également de rejetter H0; les variance des différents 
# niveaux ne sont donc pas égales.


#8)	Essayez de tester l'effet d'une transformation des variables (transformation racine,
# et log), ceci améliore-t-il la normalité des résidus ? Et l'homoscédasticité ?
##################################################################################
# Transformation racine
InsectSprays$Sqrt = sqrt(InsectSprays$count)
boxplot(Sqrt ~ spray, InsectSprays)
myAOV = aov(Sqrt ~ spray, InsectSprays)
summary(myAOV)
hist(residuals(myAOV))
shapiro.test(residuals(myAOV))
bartlett.test(Sqrt ~ spray, InsectSprays)
# Transformation Log
InsectSprays$Log = log10(InsectSprays$count + 1)
boxplot(Log ~ spray, InsectSprays)
myAOV = aov(Log ~ spray, InsectSprays)
summary(myAOV)
hist(residuals(myAOV))
shapiro.test(residuals(myAOV))
bartlett.test(Log ~ spray, InsectSprays)
# Oui, les deux types de transformation on permit de normaliser les résidus de l'ANOVA;
# et d'améliorer l'homoscédasticité des résidus, puisque les valeurs de p des deux tests
# ne permettent pas de rejetter H0 pour les deux tests (Shapiro et Bartlett).

# 9.  Chargez le package MASS en tapant :
##################################################################################
library(MASS)
# 10.	Chargez à présent le jeu de données " cabbages ". Quelle-est l'expérience réalisée 
# ici ? Décrivez ce jeu de données (statistiques et/ou graphes descriptifs). Sur cette base, 
# pensez-vous qu'il y ait un effet du cultivar et de la date sur le poids des choux et sur 
# leur contenance en vitamines C ? Avant de procéder aux analyses, pensez-vous qu'il y ait 
# une interaction entre la date et le cultivar dans leur effet sur les poids de choux, et 
# sur le taux de vitamines C ? Pourquoi ?
##################################################################################
data(cabbages)
# Il s'agit d'une expérience dans laquelle deux variables quantitatives ont été mesurées
# sur des choux (le poids et le taux de vitamine C), en fonction de deux types de cultivars
# (variable qualitative 1) et de dates (variable qualitative 2).

# A) Analyse des poids
boxplot(HeadWt ~ Cult, cabbages)
# Les choux du cultivar c39 semblent avoir un poids plus élevé que ceux du cultivar c52
# mais comme il y a recouvrement entre les boîtes de dispersion, il va falloir recourir
# au test statistique pour vérifier si cette différence est significative
boxplot(HeadWt ~ Date, cabbages)
# La date de plantation n'a pas un effet clair sur le poids. Les boites de dispersion 
# se recouvrent, il est difficile de se prononcer sans un recours au test
boxplot(HeadWt ~ Date + Cult, cabbages)
# Il semble il y avoir un effet d'interaction entre le cultivar et la date
# en effet, la série des trois dates du cultivar c39 ne montrent pas une tendance
# similaire à la série des trois dates du cultivar c52, pour lequel la date d20 donne clairement
# un poids plus important des choux.

# A) Analyse des taux de vitamine C
boxplot(VitC ~ Cult, cabbages)
# Le cultivar c52 semble avoir le taux de vitamines C le plus élevé. A vérifier par les tests.
boxplot(VitC ~ Date, cabbages)
# La date de plantation n'a pas un effet clair sur le taux de vitamines C
# Les boites de dispersion se recouvrent, il est difficile de se prononcer sans un recours au test
boxplot(VitC ~ Date + Cult, cabbages)
# Les boites de dispersion en fonction des deux facteurs montrent qu'il semble ily avoir à la fois
# un effet cultivar (la serie des trois dates du c39 semblent avoir des taux plus faible que la 
# série des trois dates du c52), et un effet date (pour les deux cultivars, la troisième date 
# semblent avoir le taux de vitamines C le plus élevé)

# 11.	Faites une ANOVA à deux facteurs (modèle complet avec terme d'interaction) pour comparer 
# les moyennes de poids (variable HeadWt) en fonction du cultivar et de la date. Que pouvez-vous
# constater sur base des résultats ? 
##################################################################################
myAOV = aov(HeadWt ~ Date + Cult + Date:Cult, cabbages)
summary(myAOV)
# Ici, on a testé simultanément l'effet date, cultivar et l'interaction entre ces deux facteurs
# sur le poids des choux. On constate un effet date significatif (on peut donc rejeter H0: les moyennes 
# des trois dates sont les mêmes), un effet cultivar significatif (on rejette H0: les moyennes des deux cultivars
# sont égales), et un effet d'interaction (on rejette H0: il n'y a pas d'interaction entre les facteurs), ce qui
# veut dire qu'il existe certaines dates pour lesquelles l'effet cultivar est différent)

# 12.	Sur base des ce qui a été vu à la séance précédente de travaux pratiques, vérifiez 
# les conditions d'application de l'ANOVA
##################################################################################
shapiro.test(residuals(myAOV))
# La valeur de p >= au seuil alpha de 0.05, on ne rejette donc pas H0: la distribution des résidus ne 
# diffère pas de celle d'une loi normale
bartlett.test(HeadWt ~ Cult, cabbages)
# La valeur de p >= au seuil alpha de 0.05, on ne rejette donc pas H0: les variance des différents cultivars 
# ne sont pas différentes
bartlett.test(HeadWt ~ Date, cabbages)
# La valeur de p >= au seuil alpha de 0.05, on ne rejette donc pas H0: les variance des différentes dates 
# ne sont pas différentes

# 13.	A l'aide de la fonction TukeyHSD, réalisez les tests de comparaison multiple sur cette analyse de 
# variance. Comment interprétez-vous ces résultats ?
TukeyHSD(myAOV)
# Au niveaux des dates: on ne trouve pas de différence significative entre les moyennes des dates d20 et d16, 
# les différence entre les autres dates sont toutes deux significatives.
# Au niveau des cultivars, on observe bien un différence significative entre les poids moyens des deux cultivars.
# Au niveaux des combinaisons des facteurs, les combinaisons suivantes présentent une différence significative 
# entre les moyennes des poids au seuil alpha de 5%:
# d16:c52-d16:c39
# d21:c52-d16:c39
# d21:c52-d20:c39
# d21:c52-d21:c39
# d21:c52-d20:c52
# Toutes les autres combinaisons ne présentent pas de différence de moyenne significative

# 14.	Répétez l'analyse (points 3 à 5), mais en étudiant cette fois la contenance en vitamines C (VitC). 
# Les résultats sont-ils comparables ? 
##################################################################################
myAOV = aov(VitC ~ Date + Cult + Date:Cult, cabbages)
summary(myAOV)
shapiro.test(residuals(myAOV))
bartlett.test(VitC ~ Cult, cabbages)
bartlett.test(VitC ~ Date, cabbages)
TukeyHSD(myAOV)
# Non, dans ce cas ci, seuls les effets Cultivar et Dates sont significatifs, et le terme d'interaction
# ne l'est pas, puisque la valeur de p associée à la statistique F est supérieure au seuil alpha de 5%.
# L'analyse des résidus nous montre que les conditions d'application de l'ANOVA sont remplies.
# Les test post-hoc nous montrent que
# Au niveaux des dates: on ne trouve pas de différence significative entre les moyennes des dates d20 et d16, 
# les différence entre les autres dates sont toutes deux significatives.
# Au niveau des cultivars, on observe bien un différence significative entre les taux moyens de vitamine C des deux cultivars.
# Au niveaux des combinaisons des facteurs, les combinaisons suivantes présentent une différence significative 
# entre les moyennes des taux en vitamines C au seuil alpha de 5%:
# d16:c52-d16:c39
# d21:c52-d16:c39
# d16:c52-d20:c39
# d20:c52-d20:c39
# d21:c52-d20:c39
# d21:c52-d21:c39
# d21:c52-d16:c52
# d21:c52-d20:c52
# Toutes les autres combinaisons ne présentent pas de différence de moyenne significative

# 15.	Quel cultivar et quelle date de plantation recommanderiez-vous en fonction de ces analyses ?
##################################################################################
# La combinaison d20.c52 semble la meilleure puisqu'elle présente un poids moyen
# élevé tout en ayant également un taux important en vitamines C. 







