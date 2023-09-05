# this is the main module where to execute the program

from models import Shape, Triangle, Square, Rectangle, Circle
import shapes_hw1

if __name__ == '__main__':

	trinage = Triangle(1.5, 1.2, 1.3)
	square = Square(2.4)
	rectangle = Rectangle(4.2, 3.1)
	circle = Circle(15.6)

	print("The largest area of these shapes are: ", largestArea([trinage, square, rectangle, circle]))
	print("The smallest area of these shapes are: ", smallesArea([trinage, square, rectangle, circle]))