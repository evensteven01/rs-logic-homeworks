 import math

 from decimal import *

def fuel_cost(liters: float, pricePerLiter: float):

    distance = float(input("how much is the distance?:_"))

    for fl in liters:
        for ppl in pricePerLiter:
            totalCost = (distance / fl) * ppl

    return totalCost

def ints_between(start: int, end: int):

    array = []

    for st in range(start):
        for ed in range(end):
            if st <= len(st) and ed >= len(ed):
                combine_int = st + ed
                array.extend(combine_int)
    return array

def mpg21p100km(mpg: float):
    
    mile = 1.609344

    gallon = 3.785411784

    kms_per_mpg = (100 / mpg)

    kms_per_gallon = (kms_per_mpg * gallon)

    miles_per_gallon = (kms_per_gallon / mile)

    return miles_per_gallon

def lp100km2mpg(lp100: float):
    
    mile = 1.609344

    gallon = 3.785411784

    gallon_per_100miles = (100 / lp100)

    gallon_per_100kms = (gallon_per_100miles / mile)

    liters_per_100kms = (gallon_per_100kms * gallon)

    return liters_per_100kms


def sticky_calculator(operator: str, val1: int, val2: int):

    val1 = int(input("Please enter your first number:_"))

    val2 = int(input("Please enter your second number:_"))

    operator = input("Please enter arithmetic operators such as (+, _ , *, /):_")
    
    if operator == "+":
        return result = (val1 * val2)

    elif operator == "/"
        return result = (val1 * val2)
 
    elif operator == "+":
        return result = (val1 + val2)

    elif operator == "-":
        return result = (val1 - val2)

def global_estimate(estimates):
    pass

def add(*args):
    return sum(args)

def generate(start, end, step):

    From = []
    To = []

    for number in range(start, end, step):
        pass

def find_missing():  
    pass