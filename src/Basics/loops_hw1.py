from src.Basics.utils import get_random_nums

"""
	Loops Homework 1
""" 

def get_maximum(listOfNumbers: list[float]):
	maximum = None

	for value in listOfNumbers:
		if maximum is None:
			maximum = value
		elif maximum < value:
			maximum = value
	return maximum

def get_minimum(listOfNumbers: list[float]):
	minimum = None

	for value in listOfNumbers:
		if minimum is None:
			minimum = value
		elif minimum > value:
			minimum = value
	return minimum

def get_average(listOfNumbers: list[float]):
	sumOfList = 0
	for i in range(len(listOfNumbers)):
		sumOfList += listOfNumbers[i]

		if sumOfList == 0:
			average = 0
		else:
			average = (sumOfList / len(listOfNumbers))
	return average

def get_closest(listOfNumbers: list[float], num: float):
	# sorting the list of nukbers in ascending order
	# imitialize a varaible closest_num to the first element of the sorted list
	# use for loop to iterate over the sorted list
	# in loop, check if it is closer to num than the varable 'closest_num', then update varable 'closest_num' to be that element
	# check if an element is greater than num, then should terminate the loop
	# finally return varable 'closest_num'
	listOfNumbers.sort()
	closest_num = listOfNumbers[0]
	for n in listOfNumbers:
		if abs(n - num) < abs(closest_num - num):
			closest_num = n
		if n > num:
			break
	return closest_num

def add_x(listOfNumbers: list[float], num: float):
	numbers = []

	if numbers is None or listOfNumbers is None or num is None:
		return numbers

	num = [n for n in listOfNumbers]

	numbers.append(num)

	return numbers

def sub_x(listOfNumbers: list[float], num: float):
	numbers = []

	if numbers is None or listOfNumbers is None or num is None:
		return numbers

	num = [n for n in listOfNumbers]

	numbers.append(num)

	return numbers