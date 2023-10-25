from src.Basics.utils import get_random_nums

"""
	Loops Homework 1
""" 

def get_maximum(listOfNumbers: list[float]):
	maximumNumber = None

	for value in listOfNumbers:
		if maximumNumber is None:
			maximumNumber = value
		elif maximumNumber < value:
			maximumNumber = value
	return maximumNumber

def get_minimum(listOfNumbers: list[float]):
	minimumNumber = None

	for value in listOfNumbers:
		if minimumNumber is None:
			minimumNumber = value
		elif minimumNumber > value:
			minimumNumber = value
	return minimumNumber

def get_average(listOfNumbers: list[float]):
	pass

def get_closest(listOfNumbers: list[float], num: float):
	pass

def add_x(listOfNumbers: list[float], num: float):
	pass

def sub_x(listOfNumbers: list[float], num: float):
	pass