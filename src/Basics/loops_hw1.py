from src.Basics.utils import get_random_nums

"""
	Loops Homework 1
""" 

def get_maximum(listOfNumbers: list[float]):
	try:
		# Assume first number in list is laragest
		# initally and assign it to variable 'maximum'
		maximum = listOfNumbers[0]
		# now traverse through the list and compare
		# each number with 'maximum' value'
		# whichever is largest assign that value to 'maximum'
		for item in listOfNumbers:
			try:
				if item > maximum:
					maximum = item
				print(maximum)
			except IndexError as e:
				print("Error:", e)
				print("Index", item, "is out of range")
	except Exception as e:
		print("An error has occurred: ", e)
	
	# after complete traversing the list
	# return the 'maximum'
	return maximum

def get_minimum(listOfNumbers: list[float]):
	try:
		minimum = listOfNumbers[0]

		for item in listOfNumbers:
			try:
				if item < minimum:
					minimum = item
				print(minimum)
			except IndexError as e:
				print("Error:", e)
				print("Index", item, "is out of range")
	except Exception as e:
		print("An error has occurred: ", e)
	return minimum

def get_average(listOfNumbers: list[float]):
	try:
		sumOfList = 0
		average = 0
		for i in range(len(listOfNumbers)):
			sumOfList += listOfNumbers[i]
			try:
				if sumOfList == 0:
					average = 0
				else:
					average = (sumOfList / len(listOfNumbers))
				print("The average is: ", average)
			except IndexError as e:
				print("Error: ", e)
				print("Index", i, "is out of range")
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
		listOfNumbers.sort()
		closestNum = listOfNumbers[0]
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