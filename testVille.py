#!usr/bin/env python
"""
Script de test des different objet actuellement implementes
"""

from ville import cVille #import de l'objet decrivant les villes
from carte import cCarte #import de l'objet decrivant la liste de toute les villes
from Algo_gen import cDarwin
from population import cPopulation

"""
Creation des != villes
"""
iut = cVille(48.787858,2.328314,"IUT_cachan")
orly = cVille(48.720572,2.36488014,"Orly")
AndrosTown = cVille(24.706531,-77.769922,"Andros_Town")
Kingston = cVille(17.987035,-76.836693,"Kingston")
VillefrancheDeRouerge = cVille(44.352343,2.037834,"Villefranche_de_Rouerge")

"""
Affichage de leur distance par rapport a l'IUT (test calcul distance)
"""
print "La distance IUT - orly est de:", str(iut.distance_precise(orly))
print "La distance IUT - AndrosTown est de:", str(iut.distance_precise(AndrosTown))
print "La distance IUT - Kingston est de:", str(iut.distance_precise(Kingston))
print "La distance IUT - Villefranche de Rouerge est de:", str(iut.distance_precise(VillefrancheDeRouerge))

carte = cCarte() #creation de l'instance qui regroupe toutes les villes

"""
Ajout des villes dans la carte
"""
carte.ajouter_ville(iut)
carte.ajouter_ville(orly)
carte.ajouter_ville(AndrosTown)
carte.ajouter_ville(Kingston)
carte.ajouter_ville(VillefrancheDeRouerge)

print "La carte contient :", carte.recup_liste_noms_villes() #On affiche le contenue de la carte

echantillon = cPopulation(carte,50)
echantillon.generer()

print "Meilleur distance initiale :", str(echantillon.obtenir_meilleur_chemin().distance())

"""
algo = cDarwin(carte)

for i in range(0,100):
	echantillon = algo.nouvelle_population(echantillon)

print "Meilleur distance finale :", str(echantillon.obtenir_meilleur_chemin().distance())"""
