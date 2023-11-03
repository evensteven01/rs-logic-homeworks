from src.Basics.utils import get_random_nums

"""
	Loops Homework 1
""" 

def get_maximum(listOfNumbers: list[float]):
	try:
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

	except Exception as e:
		print("An error has occurred: ", e)
	
	# after complete traversing the list
	# return the 'maximum'
	return maximum

def get_minimum(listOfNumbers: list[float]):
	try:
		minimum = None

		if listOfNumbers is None:
			return minimum

		for item in listOfNumbers:
			if minimum is None:
				minimum = item

			if item < minimum:
				minimum = item    

	except Exception as e:
		print("An error has occurred: ", e)

	return minimum

def get_average(listOfNumbers: list[float]):
	try:
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

	except Exception as e:
		print("An error has occurred: ", e)
	
	return average

def get_closest(listOfNumbers: list[float], num: float):
	# sorting the list of numbers in ascending order
	# initialize a varaible closestNum to the first element of the sorted list
	# use for loop to iterate over the sorted list
	# in loop, check if it is closer to num than the varable 'closestNum', then update varable 'closestNum' to be that element
	# check if an element is greater than num, then should terminate the loop
	# finally return varable 'closestNum'
	try:
		closestNum = None

		if listOfNumbers is None or num is None:
			return closestNum

		listOfNumbers.sort()

		for n in listOfNumbers:
			try:
				if abs(n - num) < abs(closestNum - num):
					closestNum = n
				if n > num:
					break
			except IndexError as e:
				print("Error: ", e)
				print("Index", n, "is out of range")
	except Exception as e:
		print("An error has occurred: ", e)

	return closestNum

def add_x(listOfNumbers: list[float], num: float):
	numbers = None

	newNum = []

	if listOfNumbers is None or num is None:
		return numbers

	num = [n for n in listOfNumbers]

	random = [i for i in range(get_random_nums())]

	newNum[random] += len(num)

	return newNum

def sub_x(listOfNumbers: list[float], num: float):
	numbers = None

	newNum = []

	if listOfNumbers is None or num is None:
		return numbers

	num = [n for n in listOfNumbers]

	random = [i for i in range(get_random_nums())]

	newNum[random] -= len(num)

	return newNum