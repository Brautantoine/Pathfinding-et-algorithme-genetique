#!usr/bin/env python

from carte import cCarte
from population import cPopulation
from chemin import cChemin
import random

class cDarwin():
	def __init__(self,carte,tournoi = 4,taux=0.05,mutation=False,elitisme=True):
		self.carte = carte
		self.mutation_active = mutation
		self.taux_mutation = taux
		self.elitisme_active = elitisme
		self.taille_tournoi = tournoi

	def tournoi(self,population):
		tournoi=cPopulation(self.carte,self.taille_tournoi)
		for i in range(0,self.taille_tournoi):
			numero_vainqueur = int(random.random() * population.obtenir_taille())
			tournoi.definir_chemin(i,population.obtenir_chemin(numero_vainqueur))
		#print tournoi.obtenir_meilleur_chemin()
		return tournoi.obtenir_meilleur_chemin()

	def brassage(self,parent1,parent2):
		enfant = cChemin(self.carte)
		position_depart = int(random.random() * len(parent1))
		position_stop = int(random.random() * len(parent1))

		for i in range(0,len(enfant)):
			if position_depart < position_stop and i > position_depart and i < position_stop:
				enfant.definir_ville(i,parent1.obtenir_ville(i))
			elif position_depart > position_stop:
				if not (i < position_depart and i > position_stop):
					enfant.definir_ville(i,parent1.obtenir_ville(i))
		#print "moitie enfant:",enfant 

		for i in range(0,len(parent2)):
			if not enfant.contient_ville(parent2.obtenir_ville(i)):
				#k = 0
				#while not enfant.obtenir_ville(k):
				#	if enfant.obtenir_ville(k)==None:
				#		enfant.definir_ville(k,parent2.obtenir_ville(i))
				#	else:
				#		k+=1
				for k in range(0,len(enfant)):
					if enfant.obtenir_ville(k)==None:
						enfant.definir_ville(k,parent2.obtenir_ville(i))
						break		
		return enfant

	def nouvelle_population(self,population):
		npopu = cPopulation(self.carte,population.obtenir_taille())
		decalage_elitisme = 0
		if self.elitisme_active:
			npopu.definir_chemin(0,population.obtenir_meilleur_chemin())
			decalage_elistisme = 1

		for i in range(decalage_elitisme, npopu.obtenir_taille()):
			parent1 = self.tournoi(population)
			#print parent1
			parent2 = self.tournoi(population)
			#print parent2
			enfant = self.brassage(parent1,parent2)
			#print "enfant :", enfant
			npopu.definir_chemin(i,enfant)

		#faire muter

		return npopu
