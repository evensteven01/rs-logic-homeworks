from src.Basics.loops_hw1 import *
from src.Basics.utils import get_random_nums

def main():
	automate = input("Do you want to input(i), or hardcode(h)?:_")

	if automate.lower() == "h":
		userInput = [
			[0, -5.5, 0.1, 4, 4.3, 0.9],
			[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
			[0.5, 0.4, 0.3, 0.2],
			[0, 1, 2, 3, 4, 5, 6, 7],
			[2.5, 3.5, 4.5, 5.5, 6.5],
			[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10],
			[-0.1, -0.2, -0.3, -0.4],
			[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5],
			[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
			[1.0, 3.5, 6.0, 8.5],
			[5.5, 8.0, 10.5, 13.0],
			[1.0, 3.5, 6.0, 8.5],
			[27.5, 22.0, 16.5, 11.0, 5.5],
			[2.5, 5.0, 7.5, 10.0, 12.5],
			[2.5, 4.5, 6.5, 8.5, 10.5],
			[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
			[-0.1, -0.2, -0.3, -0.4],
			[0.5, 0.4, 0.3, 0.2],
			[0, 1, 2, 3, 4, 5, 6, 7],
			[2.5, 3.5, 4.5, 5.5, 6.5],
		]

		number = 0, -5.5, 0.1, 4, 4.3, 0.9,
			1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5,
			0.5, 0.4, 0.3, 0.2,
			0, 1, 2, 3, 4, 5, 6, 7,
			2.5, 3.5, 4.5, 5.5, 6.5,
			1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
			-0.1, -0.2, -0.3, -0.4,
			0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5,
			0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
			1.0, 3.5, 6.0, 8.5,
			5.5, 8.0, 10.5, 13.0,
			1.0, 3.5, 6.0, 8.5,
			27.5, 22.0, 16.5, 11.0, 5.5,
			2.5, 5.0, 7.5, 10.0, 12.5,
			2.5, 4.5, 6.5, 8.5, 10.5,
			1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5,
			-0.1, -0.2, -0.3, -0.4,
			0.5, 0.4, 0.3, 0.2,
			0, 1, 2, 3, 4, 5, 6, 7,
			2.5, 3.5, 4.5, 5.5, 6.5,

	else:
		userInput = list(float(input("Please enter a list of numbers?:_")))
		number = float(input("Please enter a number?:_"))

	"""
		basics functions calls
	"""

	match automate:
		case 1:
			print("The maximum number is: ", get_maximum(userInput), "\n")
		case 2:
			print("The minimum number is: ", get_minimum(userInput), "\n")
		case 3:
			print("The average number is: ", get_average(userInput), "\n")
		case 4:
			print("The closest number is: ", get_closest(userInput, number), "\n")
		case 5:
			print("The list of numbers in addition are: ", add_x(userInput, number), "\n")
		case 6:
			print("The list of numbers in subtraction are: ", sub_x(userInput, number), "\n")
		case _:
			print("None of these functions are called on\n")