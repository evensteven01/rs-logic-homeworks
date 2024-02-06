from src.Basics.loops_hw1 import *

def main():
    
    automate = input("Do you want to input(i), or hardcode(h)?:_")

    function = int(input("What function(s) do you want? Please select these options (1 for max, 2 for min, 3 for average, 4 for closest, 5 for list of numbers being added, for 6 for list of numbers being subtract):_"))

    if automate.lower() == "h":
        userInput = [0.5, -1.0, 1.5, 2, -2.5, 3.0, -3.5, 4, 4.5, -5.0, 5.5, 6, 6.5, 7.0, -7, 8.0, -8, 9.0, 9.5]

        number = 9.5

    else:
        userInput = list(float(input("Please enter a list of numbers?:_")))
        number = float(input("Please enter a number?:_"))

    """
        basics functions calls
    """

    match function:
        case 1:
            print("The maximum number is: ", get_maximum(userInput), "\n")
        case 2:
            print("The minimum number is: ", get_minimum(userInput), "\n")
        case 3:
            print("The average number is: ", get_average(userInput), "\n")
        case 4:
            print("The closest number is: ", get_closest(userInput, number), "\n")
        case 5:
            print("The list of numbers in addition are: ", add_x(userInput, number), "\n")
        case 6:
            print("The list of numbers in subtraction are: ", sub_x(userInput, number), "\n")
        case _:
            print("None of these functions are called on\n")