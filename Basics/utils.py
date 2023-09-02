import random

# Helper Functions
def get_random_nums(number_of_randoms: int=10, min: int=0, max: int=1000):
	ran = random.Random()
	for i in range(number_of_randoms):
		yield ran.randint(min, max)