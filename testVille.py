#!usr/bin/env python

from ville import cVille
from carte import cCarte

iut = cVille(48.787858,2.328314,"IUT_cachan")
orly = cVille(48.720572,2.36488014,"orly")
AndrosTown = cVille(24.706531,-77.769922,"Andros_Town")
Kingston = cVille(17.987035,-76.836693,"Kingston")
VillefrancheDeRouerge = cVille(44.352343,2.037834,"Villefranche_de_Rouerge")

print "La distance IUT - orly est de:", str(iut.better_distance(orly))
print "La distance IUT - AndrosTown est de:", str(iut.better_distance(AndrosTown))
print "La distance IUT - Kingston est de:", str(iut.better_distance(Kingston))
print "La distance IUT - Villefranche de Rouerge est de:", str(iut.better_distance(VillefrancheDeRouerge))

carte = cCarte()

carte.ajouter_ville(iut)
carte.ajouter_ville(orly)
carte.ajouter_ville(AndrosTown)
carte.ajouter_ville(VillefrancheDeRouerge)

print "La carte contient :", carte.recup_liste_noms_villes()
