from src.Basics.utils import get_random_nums

"""
	Loops Homework 1
""" 

def get_maximum(listOfNumbers: list[float]):
	# Assume first number in list is laragest
	# initally and assign it to variable 'maximum'
	maximum = None
	# now traverse through the list and compare
	# each number with 'maximum' value'
	# whichever is largest assign that value to 'maximum'

	if listOfNumbers is None:
		return maximum

	for item in listOfNumbers:
		if maximum is None:
			maximum = item

		if item > maximum:
			maximum = item
	
	# after complete traversing the list
	# return the 'maximum'
	return maximum

def get_minimum(listOfNumbers: list[float]):
	minimum = None

	if listOfNumbers is None:
		return minimum

	for item in listOfNumbers:
		if minimum is None:
			minimum = item

		if item < minimum:
			minimum = item    


	return minimum

def get_average(listOfNumbers: list[float]):
	sumOfList = None

	if listOfNumbers is None:
		return sumOfList

	sumOfList = 0

	for item in listOfNumbers:
		sumOfList += item

	if len(listOfNumbers) == 0:
		return None
	else:
		average = (sumOfList / len(listOfNumbers))
	
	return average

def get_closest(listOfNumbers: list[float], num: float):
	# initialize a variable closestNum to the first element of the sorted list
	# use for loop to iterate over the list
	# in loop, check if it is closer to num than the varable 'closestNum', then update varable 'closestNum' to be that element
	# check if an element is greater than num, then should terminate the loop
	# finally return varable 'closestNum'
	closestNum = None

	if listOfNumbers is None or num is None:
		return closestNum

	for n in listOfNumbers:
		if (closestNum is None):
			closestNum = n

		elif abs(n - num) < abs(closestNum - num):
			closestNum = n

	return closestNum

def add_x(listOfNumbers: list[float], num: float):
	newNum = None

	if listOfNumbers is None:
		return newNum

	for i, n in enumerate(listOfNumbers):
		listOfNumbers[i] += num

	newNum = listOfNumbers

	return newNum

def sub_x(listOfNumbers: list[float], num: float):
	
	newNum = None

	if listOfNumbers is None:
		return newNum

	for i, n in enumerate(listOfNumbers):
		listOfNumbers[i] -= num

	newNum = listOfNumbers

	return newNum
