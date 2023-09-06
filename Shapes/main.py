# this is the main module where to execute the program

from models import Shape, Triangle, Square, Rectangle, Circle
from shapes_hw1 import largestArea, smallestArea

if __name__ == '__main__':

	trinagle_side1 = float(input("Please enter for side1 of trinagle:_"))
	trinage_side2 = float(input("Please enter for side2 of trinagle:_"))
	trinage_side3 = float(input("Please enter for side3 of trinagle:_"))

	sqrt_side = float(input("Please enter for side of square:_"))

	rect_length = float(input("PLease enter for length of rectangle:_"))
	rect_width = float(input("Please enter for width of rectangle:_"))

	circle_radius = float(input("Please enter for radius of circle:_"))

	trinage = Triangle(trinagle_side1, trinage_side2, trinage_side3)
	square = Square(sqrt_side)
	rectangle = Rectangle(rect_length, rect_width)
	circle = Circle(circle_radius)

	print("The largest area of these shapes are: ", largestArea([trinage, square, rectangle, circle]))
	print("The smallest area of these shapes are: ", smallestArea([trinage, square, rectangle, circle]))