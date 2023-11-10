from src.Basics.loops_hw1 import *
from src.Basics.utils import get_random_nums

def main():
	automate = input("Do you want to input(i), or hardcode(h)?:_")

	if automate.lower() == "h":
		userInput = [0, -5.5, 0.1, 4, 4.3, 0.9]
	else:
		userInput = list(input("Please enter a list of numbers?:_"))

	"""
		basics functions calls
	"""
	print("The maximum number is: ", get_maximum(), "\n")
	print("The minimum number is: ", get_minimum(), "\n")
	print("The average number is: ", get_average(), "\n")
	print("The closest number is: ", get_closest(), "\n")
	print("The list of numbers in addition are: ", add_x(), "\n")
	print("The list of numbers in subtraction are: ", sub_x(), "\n")