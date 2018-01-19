#!usr/bin/env python

import csv
from ville import cVille

class cCarte(): #contient la liste de toutes les instances cVille du parcours
	def __init__(self): #initialisation vide
		self.villes=[]

	def ajouter_ville(self,ville): #Enrichi la liste avec une nouvelle ville
		self.villes.append(ville)

	def nb_villes(self): #retourne le nombre de ville contenue dans la liste
		return len(self.villes)

	def recup_liste_noms_villes(self): #cree et retourne une liste de tous les noms des villes
		temp = []
		for i in range(0,len(self.villes)):
			temp.append(self.villes[i].nom)
		return temp
	
	def importer_csv(self, filename):
		with open(filename, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in reader:
				ville = cVille(float(row[1]), float(row[2]), str(row[0]).strip())
				self.ajouter_ville(ville)
		