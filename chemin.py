from ville import cVille

import random

class cChemin():
	def __init__(self, carte): #il melange tout seul les villes qui lui sont donne dans la carte
		self.carte = carte;
		self.chemin = list(carte.villes) #copie des villes dans les chemins
	
	def __len__(self):
		return len(self.chemin)
	
	def melanger(self):
		random.shuffle(self.chemin)
	
	def efficacite(self):
		return 1.0/self.distance()
	
	def distance(self):
		distance = 0
		for index in range(0, len(self.chemin)-1):
			villeOrigine = self.chemin[index]
			villeDestination = self.chemin[index+1]
			distance += villeOrigine.distance_precise(villeDestination)
			
		return distance
	
	def definir_ville(self, index, ville):
		self.chemin[index] = ville
		
	def obtenir_ville(self, index):
		return self.chemin[index]
	
	def contient_ville(self, ville):
		return ville in self.chemin
	
	def __repr__(self):
		resultat = ""
		
		for chemin in self.chemin:
			resultat += str(chemin) + "->"
		
		return resultat
