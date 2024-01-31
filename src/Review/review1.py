import math

from decimal import *

import re

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
    # then check if the second variable is substracted by first variable and then greater than 1

    return [missingArr for row, col in zip(numbers, numbers[1:])
        for missingArr in range(row + 1, col) if col - row > 1]

def correct_tail(body: str, tail: str):

    # create stored variable called sub
    # firstly, let's do length of body by using len function
    # subtracted by 1
    # the colon operator does slice a part of from a sequence object
    # such as list, tuple or string
    # also the colon indicates that start of new block of code 
    # and signals the python that following indented lines should be executed as part that block
    # then just have the length of body
    # all of these are in subscript
    # the check if stored variable 'sub' is equal to tail
    # if it does equal or at least match the corrected tail
    # it should return true
    # otherwise it returns false

    sub = body[len(body) - 1 : len(body)]

    if sub == tail:
        return True
    else:
        return False

def string_repeat(n: int, s: str):
    
    repeatStr = ""

    for _ in range(n):
        repeatStr += s

    return repeatStr

def sum_no_highest_lowest(arr):
    
    # objectively is to calculate the sum of list of integers
    # by having a minus the minimum and maximum
    # Then check if the array is either empty, none, or 
    # if only one element exist
    # Then it should returns 0

    if arr is None or len(arr) <= 1:
        return 0
    else:
        return sum(sorted(arr)[1:-1])

def paper_rock_scissors(input1: str, input2: str):

    PLAYER1 = "Player 1 won!"
    PLAYER2 = "Player 2 won!"
    DRAW = "Draw!"

    if input1 == "rock" and input2 == "scissors":
        return PLAYER1
    elif input1 == "rock" and input2 == "paper":
        return PLAYER2
    elif input1 == "rock" and input2 == "rock":
        return DRAW
    elif input1 == "paper" and input2 == "scissors":
        return PLAYER2
    elif input1 == "paper" and input2 == "rock":
        return PLAYER1
    elif input1 == "paper" and input2 == "paper":
        return DRAW
    elif input1 == "scissors" and input2 == "rock":
        return PLAYER2
    elif input1 == "scissors" and input2 == "paper":
        return PLAYER1
    elif input1 == "scissors" and input2 == "scissors":
        return DRAW

def calculate_tip(cost: float, rating: str):
    # Return the tip amount that the customer will leave
    # tip = tip_percentage * cost
    # tip = .18 * 20 = 3.60

    # How much the bill is
    bill = cost

    # how much the tip was
    if rating.lower() == "terrible":
        tip = math.ceil(0 * bill)
        return tip
    elif rating.lower() == "poor":
        tip = math.ceil(.05 * bill)
        return tip
    elif rating.lower() == "good":
        tip = math.ceil(.1 * bill)
        return tip
    elif rating.lower() == "great":
        tip = math.ceil(.15 * bill)
        return tip
    elif rating.lower() == "excellent":
        tip = math.ceil(.2 * bill)
        return tip
    else:
        return "Rating not recognized"

def shorten_to_date(longDate: str):
    
    # lets use split on comma
    # let use subscript at index 0
    # so the outcome should be shortned string

    return longDate.split(',')[0]

def double_array(arr):
    
    # lets use list comprehension
    # have list comprehension to iterate over paramter
    # then have iterator times 2 
    # then have whole code block into bracket 
    # finally returns whole thing in one line

    return [num * 2 for num in arr]

def sum_2d_list(arr: int):

    # create stored variable and set to 0
    # use for loop to iterate over the parameter
    # then increment the stored variable by having iterator in the sum function
    # note- the sum function its purpose is to add all the elements in an iterable like (list or tuples) and it returns the total
    # finally returns the outcome or result
    
    totalSum = 0

    for row in arr:
        totalSum += sum(row)

    return totalSum

def sums_of_lists(numbers):

    return sum([sum(num) for num in numbers])

def powers_of_2(n: int):

    # create stored variable and set as empty array
    # use for loop to iterate over parameter in range function and added by 1
    # in body statement, append the expression: iterator to the power of 2 into the array
    # finally returns the array
    
    out = []

    for num in range(n+1):
        out.append(2**num)

    return out

def count_pos_sum_neg(arr: int):

    # lets use list comprehension to iterate over parameter
    # then check if list comprehension's iterator is greater than 0
    # then put the first list comprehension code block in length function
    # then lets use another list comprehension to iterate over the same parameter
    # but this time check if list comprehension's iterator is less than 0
    # then put second list comprehension code block into sum function
    # then put this whole code block with two list comprehensions into brackets
    # finally, outside of the bracket, check if length of array is not equal to 0
    # otherwise, its empty array

    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []

def is_all_caps(randomCharacters: str):

    # import re- regular expression
    # then use if-else-if statements
    # use of uppercase function to compare the parameter
    # then use match function which takes two arguments and then check if its not equal to null
    # finally returns boolans

    if randomCharacters.upper() == randomCharacters:
        return True

    elif re.match('a-z', randomCharacters) != None:
        return False

    else:
        return False
