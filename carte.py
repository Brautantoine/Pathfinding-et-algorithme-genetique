#!usr/bin/env python

from ville import cVille

class cCarte():
	def __init__(self):
		self.villes=[]

	def ajouter_ville(self,ville):
		self.villes.append(ville)
	def nb_villes(self):
		return len(self.villes)

	def recup_liste_noms_villes(self):
		temp = []
		for i in range(0,len(self.villes)):
			temp.append(self.villes[i].nom)
		return temp
