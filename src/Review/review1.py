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

    arrayInt = []

    for value in range(start, end + 1):
        arrayInt.append(value)

    return arrayInt

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


def sticky_calculator(operator: str, val1, val2):

    result = str(val1) + str(val2)
    
    if operator == "*":
        return (int(result) * val2)

    elif operator == "/":
        return (int(result) / val2)
 
    elif operator == "+":
        return (int(result) + val2)  

    elif operator == "-":
        return (int(result) - val2)

def global_estimate(estimates):

    globalBestCase, globalAvgCase, globalWorstCase = 0, 0, 0

    for fEstimate in estimates:

        fBestCase = fEstimate[0]
        fworstCase = fEstimate[1]
        fAverageCase = (fBestCase + fworstCase) / 2

        globalBestCase += fBestCase
        globalWorstCase += fworstCase
        globalAvgCase += fAverageCase

    totalGlobalEstimation = (globalBestCase, globalAvgCase, globalWorstCase)
        
    return totalGlobalEstimation

def add(args):

    totalSum = 0

    count = 1

    for index, num in enumerate(args):

        calcSum = (num * count)

        count += 1

        totalSum += int(calcSum)

    return totalSum
 
def generate(start: int, end: int, step: int):

    generateArray = []

    for num in range(start, end + 1, step):
        generateArray.append(num)

    if start > end:
        generateArray.reverse()

    return generateArray 

def find_missing(numbers):

    # numbers = [-1,1,2,3,7,8,10] -> [0,4,5,6,9] 

    # use list comprehension to loop over paramters
    # use zip method to pairs the corresponging elements or items from the list
    # use slicing[] as starting from element at certain index
    # then use for loop in a range where the first variable get added by 1 and then second variable
    # theh check if the second variable is substracted by first variable and then greater than 1

    return [missingArr for row, col in zip(numbers, numbers[1:])
        for missingArr in range(row + 1, col) if col - row > 1]


def correct_tail(body, tail):
     sub = body.substr(len(body)-len(tail.length))
    if sub = tai:
        return True
    else:
        return False