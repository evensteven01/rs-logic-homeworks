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

class Square(Shape):
	"""docstring for Square"""
	def __init__(self, side):
		self.side = side

	def area():
		sqrtArea = (self.side * self.side)
		return sqrtArea

	def perimeter():
		return sum(self.side)

class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def area(self):
		rectArea = (self.side1 * self.side2)
		return rectArea
		
class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return (self.radius ** 2) * 3.14

	def perimeter(self):
		return (2 * self.radius) * 3.14
		