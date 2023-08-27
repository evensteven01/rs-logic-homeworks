"""
	Create a square type with an area function. It should extend Shape.
	Create a rectangle type with an area function. It should extend Shape.
	Create a circle type with an area function. It should extend Shape.

	Create a function that takes a list of shapes, and returns the shape with the largest area.
		If tie, return any of the tied.

	Create a function that takes a list of shapes, and returns the shape with the smallest area.
		If tie, return any of the tied.
"""


import math

class Shape:
	def area() -> float:
		raise NotImplementedError()

class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def area():
		# semi perimeter
		s_p = (self.side1 + self.side2 + self.side3)/2
		return math.sqrt(s_p*(s_p-self.side1)*(s_p-self.side2)*(s_p-self.side3))


