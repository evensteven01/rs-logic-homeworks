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

    print("\t\tWelcome to the tip calculator!")

    # How much the bill is
    bill = cost

    # how much the tip was
    tips = [0, 5, 10, 15, 20]

    for tp in tips:
        print(f"If you would like to leave a {tp}%, the amount will be ${bill * tp / 100}.")

    # to calculate the bill
    # will use PANDAS
    final_amount = bill * (1 + (tp / 100))

    if tp == 20:
        print(f"each person should pay:${final_amount:.2f}")
        return rating

    elif tp == 15:
        print(f"each person should pay:${final_amount:.2f}")
        return rating

    elif tp == 10:
        print(f"each person should pay:${final_amount:.2f}")
        return rating

    elif tp == 5:
        print(f"each person should pay:${final_amount:.2f}")
        return rating

    elif tp == 0:
        print(f"each person should pay:${final_amount:.2f}")
        return rating
    else: 
        return rating

def shorten_to_date(longDate: str):
    
    # lets use split on comma
    # let use subscript at index 0
    # so the outcome should be shortned string

    return longDate.split(',')[0]