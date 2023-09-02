import math

class Shape:(self)
	def area(self) -> float:
		raise NotImplementedError()

class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def area(self):
		# Triangle's area formula
		# semi perimeter
		s_p = (self.side1 + self.side2 + self.side3)/2
		return math.sqrt(s_p*(s_p-self.side1)*(s_p-self.side2)*(s_p-self.side3))

class Square(Shape):
	"""docstring for Square"""
	def __init__(self, side):
		self.side = side

	def area(self):
		# since, in squares, all sides are the same
		# so we'll to use math.pow function in 
		# which is built-in function as equalvent to exponent
		# this is square's area formula
		sqrtArea = math.pow(self.side, 2)
		return sqrtArea

	def perimeter():
		squrePerimeter = sum(self.side)
		return squrePerimeter

class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		# this is Rectangle's area formula with width and height
		rectArea = (self.width * self.height)
		return rectArea
		
class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		# this is circle's area formular with 3.14 represents pie
		circleRadious = (self.radius ** 2) * 3.14
		return circleRadious

	def perimeter(self):
		circlePerimeter = (2 * self.radius) * 3.14
		return circlePerimeter
		