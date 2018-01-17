from chemin import cChemin

class cPopulation():
	def __init__(self, carte, taille):
		self.carte = carte
		self.taille = taille
		self.chemins = [None]*taille
	
	def generer(self):
		for i in range(0, self.taille):
			chemin = cChemin(self.carte)
			chemin.melanger()
			self.chemins[i]=chemin
	
	def taille(self):
		return len(self.chemins)
	
	def definir_chemin(self, index, chemin):
		self.chemins[index] = chemin
	
	def obtenir_chemin(self, index):
		return self.chemins[index]
	
	def obtenir_meilleur_chemin(self):
		meilleur_chemin = self.chemins[0];
		
		for i in range(0, self.taille):
			if meilleur_chemin.efficacite() <= self.chemins[i].efficacite():
				meilleur_chemin = self.chemins[i]
			#print self.chemins[i].efficacite()
			return meilleur_chemin
			
	def __repr__(self):
		return str(self.chemins)
