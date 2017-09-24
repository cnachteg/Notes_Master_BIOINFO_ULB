##################################################################################
## Travaux pratiques: 9ème séance: statistiques non paramétriques
##################################################################################

# 1) Etude de groupes sanguins aux USA. Les distributions de groupes sanguins sont-elles 
# identiques dans les trois états étudiés ? 
##################################################################################
# Nous allons faire un test de Chi2
# Cet exercice est plus facile a effectuer dans un tableur
# Voici cependant une solution...

# Stockons d'abord les données dans une matrice
myMObs = matrix(c(122,117,19,244,1781, 1351, 289, 3301,353, 269, 60, 713), 4,3)
# On doit maintenant calculer les fréquences attendues
myMAtt = myMObs
for (i in 1:3){
for (j in 1:4){
myMAtt[j,i] = sum(myMObs[j,])*sum(myMObs[,i])/sum(myMObs)
}
} 
# Maitenant on calcule le Chi-2
myChi = sum(((myMObs-myMAtt)^2)/myMAtt)
myddl = (3-1)*(4-1)
pchisq(myChi, myddl, lower.tail = F)

# On obtient une valeur de p de 0.536, on ne rejette donc pas H0 et on peut considérer
# que la distribution des groupes sanguins est homogène aux USA.

# Une autre possibilité encore, utiliser la fonction chisq.test de R;
chisq.test(myMObs)



# 2) Etudiez cette question à l'aide d'un test de Wilcoxon-Mann-Whitney (apparié 
# ou non-apparié ? Pourquoi ?). Vous pouvez ici utiliser soit la technique vue au 
# cours et calculer vos percentiles avec la fonction pwilcox(), soit utiliser la 
# fonction wilcox.test().
##################################################################################
tol = c(3.420,2.314,1.911,2.464,2.781,2.803)
tem = c(1.820,1.843,1.397,1.803,2.539,1.990)

wilcox.test(c(3.420,2.314,1.911,2.464,2.781,2.803),c(1.820,1.843,1.397,1.803,2.539,1.990))

# L'analyse montre qu'on peut rejetter H0 à un seuil alpha de 5%, car on obtient un 
# une statistique W = 32 associée à une valeur de p de 0.0259. On peut donc conclure
# que les deux populations n'ont pas le même taux de dopamine. On a utilisé un test 
# non apparié car les mesures on été effectuées sur des individus différents.

# Etude d'un coupe-faim (mCPP) : diminution de poids de sujets après 2 semaines avec 
# mCPP et avec un placébo (expérience menée en double aveugle). Etudiez cette question à 
# l'aide d'un test de Wilcoxon-Mann-Whitney (apparié ou non-apparié ? Pourquoi ?). 
##################################################################################
wilcox.test(c(0.0,-1.1,-1.6,-0.3,-1.1,-0.9,-0.5,0.7,-1.2),c(-1.1,0.5,0.5,0.0,-0.5,1.3,-1.4,0.0,-0.8), paired = T)
# On a utilisé un test apparié puisque les observations on été effectuées sur les mêmes
# individus. Ici en revanche, on ne peut pas rejetter H0, puisque la probabilité associée 
# à la statistique V est supérieure au seuil alpha de 5%. Il n'y a donc pas de différence
# de perte de poids entre les populations ayant reçu un coupe faim et celles ayant reçu un
# placebo.

