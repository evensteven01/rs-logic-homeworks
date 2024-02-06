import math
from math import pi

class Shape:
	"""docstring for Shape"""
	def getArea(self):
		raise NotImplementedError()
		
class Cube(object):
	"""docstring for Cube"""
	def __init__(self):
		side = 0

	def getSide(self):
		return self.side

	def setSide(self, num: int):
		self.side = num

	def getArea(self):
		
		ar =  6 * (self.side * self.side)
		return ar

class Sphere(object):
	"""docstring for Sphere"""
	def __init__(self, r):
		self.radius = r

	def area(self):
		ar = 4 * pi * self.radius ** 2