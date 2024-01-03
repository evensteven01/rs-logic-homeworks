import math

from decimal import *

def fuel_cost(liters: float, pricePerLiter: float):

    discount = int(liters / 2) * 0.05

    if discount > .25:
        discount = .25

    discountPerLiter = (pricePerLiter - discount)

    if discountPerLiter < 0:
        discountPerLiter = 0

    totalCost = (liters * discountPerLiter)

    return round(totalCost, 2)

def ints_between(start: int, end: int):

    array = []

    for st in start:
        for ed in end:
            if st <= ed:
                combine_int = st + ed
                array.extend(combine_int)
    return array

def mpg2lp100km(mpg: float):
    
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
    
    if operator == "*":
        return (val1 * val2)

    elif operator == "/":
        return (val1 * val2)
 
    elif operator == "+":
        return (val1 + val2)  

    elif operator == "-":
        return (val1 - val2)

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