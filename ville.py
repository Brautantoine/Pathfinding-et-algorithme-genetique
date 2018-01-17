#!usr/bin/env python

import math

class cVille():
	def __init__(self, latitude, longitude, nom):
		self.longitude=longitude
		self.latitude=latitude
		self.nom=nom

	def distance(self,ville):
		dX=((self.longitude-ville.longitude)*40000*math.cos(self.latitude+ville.latitude)*math.pi/360)/360
		dY=((self.latitude-ville.latitude)*40000)/360
		return math.sqrt(dX**2+dY**2)

	def better_distance(self,ville): #d'apres la formule de haversine
		rayon =  6378.137 #rayon de la Terre
		dLatitude = ville.latitude * math.pi / 180 - self.latitude * math.pi / 180
		dLongitude = ville.longitude * math.pi / 180 - self.longitude * math.pi / 180
		a = math.sin(dLatitude/2) * math.sin(dLatitude/2) + math.cos(self.latitude * math.pi / 180) * math.cos(ville.latitude * math.pi / 180) * math.sin(dLongitude/2) * math.sin(dLongitude/2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		distance = rayon * c
		return distance

	def longitude(self):
		return self.longitude

	def latitude(self):
		return self.latitude

	def nom(self):
		return self.nom
