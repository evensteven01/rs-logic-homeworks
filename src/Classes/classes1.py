import math
from math import pi

class Shape:
	"""docstring for Shape"""
	def getArea(self):
		raise NotImplementedError()
		
class Cube(Shape):
	"""docstring for Cube"""
	def __init__(self, side: int = 0):
		self.side = abs(side)

	def getSide(self):
		return self.side

	def setSide(self, num: int):
		self.side = abs(num)

	def getArea(self):
		ar =  6 * (self.side * self.side)
		return ar

class Sphere(Shape):
	"""docstring for Sphere"""
	def __init__(self, r):
		self.radius = r

	def getArea(self):
		ar = 4 * pi * self.radius ** 2
		return ar