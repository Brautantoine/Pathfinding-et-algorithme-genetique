#!usr/bin/env python

class cCore():
	
	def __init__(self,echantillon,algo):
		self.core = 0
		self.num_generations = 0
		self.algo = algo
		self.echantillon = echantillon
		 

	def determiner_minimum_locale(self):
		while self.core<15:
			dernier_meilleur = self.echantillon.obtenir_meilleur_chemin().distance()
			self.echantillon = self.algo.nouvelle_population(self.echantillon)
			if dernier_meilleur == self.echantillon.obtenir_meilleur_chemin().distance():
				self.core += 1
			else:
				self.core = 0
			self.num_generations += 1

		print "\nMeilleur distance finale :", str(self.echantillon.obtenir_meilleur_chemin().distance()) , str(self.echantillon.obtenir_meilleur_chemin()) , "\na la generation numero :" , str(self.num_generations)
