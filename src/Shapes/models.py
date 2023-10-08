# This module designs and create all kinds of shape objects with areas and/or perimeters
# import math
import math

# create shape class
class Shape:
	def area(self) -> float:
		raise NotImplementedError()

# create Trianle class
class Triangle(Shape):
	"""docstring for Triangle"""
	# constructor of triangle
	def __init__(self, side1: float, side2: float, side3: float):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def area(self):
		# area for triangle
		# Triangle's area formula
		# semi perimeter
		s_p = (self.side1 + self.side2 + self.side3)/2
		return math.sqrt(s_p*(s_p-self.side1)*(s_p-self.side2)*(s_p-self.side3))
	# string object of traingle
	def __str__(self):
		return f"trinagle's side1: {self.side1}, side2: {self.side2}, side3: {self.side3}"

# create Square class
class Square(Shape):
	"""docstring for Square"""
	# constructor of square
	def __init__(self, side: float):
		self.side = side

	# area for square
	def area(self):
		# since, in squares, all sides are the same
		# so we'll to use math.pow function in 
		# which is built-in function as equalvent to exponent
		# this is square's area formula
		sqrtArea = math.pow(self.side, 2)
		return sqrtArea
	# string object of square
	def __str__(self):
		return f"square's side: {self.side}"
	# perimeter of square
	def perimeter():
		squrePerimeter = sum(self.side)
		return squrePerimeter

# create Rectangle class
class Rectangle(Shape):
	"""docstring for Rectangle"""
	# constructor of rectangle
	def __init__(self, width: float, height: float):
		self.width = width
		self.height = height

	# area for rectangle
	def area(self):
		# this is Rectangle's area formula with width and height
		rectArea = (self.width * self.height)
		return rectArea
	# string object of rectangle
	def __str__(self):
		return f"rectangle's width: {self.width}, height: {self.height}"

# create Circle class		
class Circle(Shape):
	"""docstring for Circle"""
	# constructor of circle
	def __init__(self, radius: float):
		self.radius = radius

	# area for circle
	def area(self):
		# this is circle's area formular with 3.14 represents pie
		circleRadious = (self.radius ** 2) * 3.14
		return circleRadious
	# perimeter of circle
	def perimeter(self):
		circlePerimeter = (2 * self.radius) * 3.14
		return circlePerimeter
	# string object of circle
	def __str__(self):
		return f"circle's radius: {self.radius}"
		
