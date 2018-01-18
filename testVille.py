#!usr/bin/env python
"""
Script de test des different objet actuellement implementes
"""

from ville import cVille #import de l'objet decrivant les villes
from carte import cCarte #import de l'objet decrivant la liste de toute les villes
from Algo_gen import cDarwin
from core import cCore
from population import cPopulation

"""
Creation des != villes
"""
iut = cVille(48.787858,2.328314,"IUT_cachan")
orly = cVille(48.720572,2.36488014,"Orly")
AndrosTown = cVille(24.706531,-77.769922,"Andros_Town")
Kingston = cVille(17.987035,-76.836693,"Kingston")
VillefrancheDeRouerge = cVille(44.352343,2.037834,"Villefranche_de_Rouerge")
Mascat = cVille(23.587565,58.412176,"Mascat")
Naruto = cVille(34.182665,134.550965,"Naruto")
Kellog = cVille(62.476744,86.295110,"Kellog")

"""
Affichage de leur distance par rapport a l'IUT (test calcul distance)
"""
"""
print "La distance IUT - orly est de:", str(iut.distance_precise(orly))
print "La distance IUT - AndrosTown est de:", str(iut.distance_precise(AndrosTown))
print "La distance IUT - Kingston est de:", str(iut.distance_precise(Kingston))
print "La distance IUT - Villefranche de Rouerge est de:", str(iut.distance_precise(VillefrancheDeRouerge))
"""

carte = cCarte() #creation de l'instance qui regroupe toutes les villes

"""
Ajout des villes dans la carte
"""
carte.ajouter_ville(iut)
carte.ajouter_ville(orly)
carte.ajouter_ville(AndrosTown)
carte.ajouter_ville(Kingston)
carte.ajouter_ville(VillefrancheDeRouerge)
carte.ajouter_ville(Mascat)#ici
carte.ajouter_ville(Naruto)
carte.ajouter_ville(Kellog)

#print "La carte contient :", carte.recup_liste_noms_villes() #On affiche le contenue de la carte

echantillon = cPopulation(carte,500)
echantillon.generer()

print "Meilleur distance initiale :", str(echantillon.obtenir_meilleur_chemin().distance()) , str(echantillon.obtenir_meilleur_chemin())

algo = cDarwin(carte)
"""
core = 0
num_generations = 0
while core<15:
	dernier_meilleur = echantillon.obtenir_meilleur_chemin().distance()
	echantillon = algo.nouvelle_population(echantillon)
	if dernier_meilleur == echantillon.obtenir_meilleur_chemin().distance():
		core += 1
	else:
		core = 0
	num_generations += 1
"""
#print "\nMeilleur distance finale :", str(echantillon.obtenir_meilleur_chemin().distance()) , str(echantillon.obtenir_meilleur_chemin()) , "\na la generation numero :" , str(num_generations)

c = cCore(echantillon,algo)
c.determiner_minimum_locale()
