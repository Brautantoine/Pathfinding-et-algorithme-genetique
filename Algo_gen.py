#!usr/bin/env python

from carte import cCarte
from population import cPopulation
from chemin import cChemin
import random

""" Class gerant l'algorithme genetique, il permet de calculer une nouvelle population à partir d'une population de base"""
class cDarwin():
	def __init__(self,carte,tournoi = 10,taux=0.05,mutation=False,elitisme=True):
		self.carte = carte
		self.mutation_active = mutation #Utilise t'on la mutation ?
		self.taux_mutation = taux
		self.elitisme_active = elitisme #utilise t'on l'elitisme ?
		self.taille_tournoi = tournoi
	"""Selectionne un individu dans la population"""
	def tournoi(self,population): 
		tournoi=cPopulation(self.carte,self.taille_tournoi) #on cree une liste vide de chemin
		for i in range(0,self.taille_tournoi): #en fonction de notre taille de poule
			numero_vainqueur = int(random.random() * population.obtenir_taille()) # on tire un vainqueur
			tournoi.definir_chemin(i,population.obtenir_chemin(numero_vainqueur)) #et on le stock dans la liste de chemin
		return tournoi.obtenir_meilleur_chemin() #On renvoie alors le meilleur des vainqueur
	
	"""On cree un nouvelle individu à partir de 2 parent, le brassage ce fait avec un 2-point aleatoire"""
	def brassage(self,parent1,parent2): 
		enfant = cChemin(self.carte)#On instancie un enfant
		position_depart = int(random.random() * len(parent1))#on choisie un premier point aleatoire
		position_stop = int(random.random() * len(parent1))#on choisie un deuxieme point aleatoire
		
		#On vient remplir l'enfant avec les points aleatoire du parent 1
		for i in range(0,len(enfant)):
			if position_depart < position_stop and i > position_depart and i < position_stop: 
				enfant.definir_ville(i,parent1.obtenir_ville(i)) #Si start<stop on remplit l'enfant avec les villes du parent 1 comprise entre start et stop
			elif position_depart > position_stop: #Si stop<start on remplit l'enfant avec les villes du parent 1 qui ne sont pas comprise entre start et stop
				if not (i < position_depart and i > position_stop):
					enfant.definir_ville(i,parent1.obtenir_ville(i))

		for i in range(0,len(parent2)): #On vient ensuite complete l'enfant avec le parent 2
			if not enfant.contient_ville(parent2.obtenir_ville(i)):#On verifie que l'enfant ne contient pas déjà la ville du parent 2
				#k = 0  #Version de remplissage sans break (augmente la compllexite)
				#while not enfant.obtenir_ville(k):
				#	if enfant.obtenir_ville(k)==None:
				#		enfant.definir_ville(k,parent2.obtenir_ville(i))
				#	else:
				#		k+=1
				for k in range(0,len(enfant)): #On cherche la premiere place libre de l'enfant
					if enfant.obtenir_ville(k)==None:
						enfant.definir_ville(k,parent2.obtenir_ville(i)) #des qu'une place est libre on la remplit
						break		
		return enfant #On retourne l'enfant ainsi cree

	"""Gere le mechanisme d'evolution de la population"""
	def nouvelle_population(self,population):
		npopu = cPopulation(self.carte,population.obtenir_taille()) #instancie une nouvelle population (population de rang gen+1)
		decalage_elitisme = 0 #variables local pour le decalage du a l'elitisme

		if self.elitisme_active: #Si l'elitisme est active
			npopu.definir_chemin(0,population.obtenir_meilleur_chemin()) #On stock le meilleur chemin de la population de depart
			decalage_elistisme = 1 #On indique que la premiere place de la  liste est prise

		for i in range(decalage_elitisme, npopu.obtenir_taille()): #On remplit la nouvelle population
			parent1 = self.tournoi(population) #On tire un parent 1
			parent2 = self.tournoi(population) #on tire un parent 2
			enfant = self.brassage(parent1,parent2) #on cree le nouvelle individu
			npopu.definir_chemin(i,enfant) #on stocke le nouvelle individu dans la nouvelle population

	""" La mutation se passe ici ... <- à faire """

		return npopu #On retourne la nouvelle population
