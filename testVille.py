#!usr/bin/env python
"""
Script de test des different objet actuellement implementes
"""

from ville import cVille #import de l'objet decrivant les villes
from carte import cCarte #import de l'objet decrivant la liste de toute les villes
from Algo_gen import cDarwin
from core import cCore
from population import cPopulation
import sys #Module pour la gestion d'argument

"""   #Affichage de l'argument 
try :
	print sys.argv[1]
	print type(sys.argv[1])
except IndexError:
	print "Aucun argument donnee"
"""

carte = cCarte() #creation de l'instance qui regroupe toutes les villes
carte.importer_csv("villes.csv") #chargement des coordonnées GPS du csv

try: #On vient tester la validite de l'argument lors de la création de la pop
	if not sys.argv[1].isdigit():
		raise ValueError
	echantillon = cPopulation(carte,int(sys.argv[1]))
except IndexError: #Si aucun argument n'est passe on previens l'utilisateur
	print "Aucune argument donnee, population par defaut = 100"
	echantillon = cPopulation(carte,100)
except ValueError: #Si l'argument n'est pas un nombre ou une valeur acceptable
	print "Argument non valide, population par defaut = 100"
	echantillon = cPopulation(carte,100)

echantillon.generer() #On remplit aleatoirement la population 0

#On affiche le meilleur trajet
print "Meilleure distance initiale :", str(echantillon.obtenir_meilleur_chemin().distance()) , str(echantillon.obtenir_meilleur_chemin())

algo = cDarwin(carte) #On cree l'instance de notre algo genetique

c = cCore(echantillon,algo) #On cree notre instance de gestion globale
c.determiner_minimum_locale() #On lance le calcul du meilleur trajet
