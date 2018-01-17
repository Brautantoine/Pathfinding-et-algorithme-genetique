#!usr/bin/env python

import math

class cVille():
	def __init__(self, longitude, latitude, nom):
		self.longitude=longitude
		self.latitude=latitude
		self.nom=nom

	def distance(self,ville):
		dX=((self.longitude-ville.longitude)*40000*math.cos(self.latitude+ville.latitude)*math.pi/360)/360
		dY=((self.latitude-ville.latitude)*40000)/360
		return math.sqrt(dX**2+dY**2)

	def longitude(self):
		return self.longitude

	def latitude(self):
		return self.latitude
