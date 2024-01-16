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

    for num in args:
        if num not in args:
            return 0

        totalSum += int(num)

    return totalSum
 
def generate(start: int, end: int, step: int):

    generateArray = []

    for index, num in range(start, end, step):

        From, To, Step = index[0], index[1], index[2]

        while From < To:

            generateArray.append(num)
            
            if Step > To:
                generateArray.pop(num)

            if From > To:
                generateArray.append(reverse(num))

            Step += 1

    return generateArray

def find_missing(numbers):

    max = numbers[0]

    for i in numbers:
        if i > max:
            max = i

    min = numbers[0]

    for j in numbers:
        if j < min:
            min = j

    missing = max + 1

    missingNumbers = []

    for _ in numbers:
        max = max - 1

        if max not in numbers:
            missingNumbers.append(max)

    return missingNumbers
