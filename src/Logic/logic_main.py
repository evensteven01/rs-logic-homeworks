from src.Logic.variables import *
from src.Logic.boolean_logic import *

def main():
    automate = input("Do you want to hardcode(h)?:_")

    if automate.lower() == "h":
        stringUser = '''
            "What function(s) do you want?\n
            Please select these options:
            (1 for create_vars, 
            2 for create_list, 
            3 for modify_list, 
            4 for add_item_to_list, 
            5 for create_str_dict, 
            6 for create_int_dict,
            7 for create_mixed_dict,
            8 for update_dict,
            9 for remove_item_dict,
            10 for build_dict)_"
        '''

    function = int(input(stringUser))

    """
        Logic's functions calls
    """

    match function:
        case 1:
            print("The integer and string are: ", create_vars())
        case 2:
            print("The list of integers are: ", create_list())
        case 3:
            print("The modified list of integers are: ", modify_list())
        case 4:
            print("This list looks like after added item is inserted: ", add_item_to_list())
        case 5:
            print("The string dictionary looks like: ", create_str_dict())
        case 6:
            print("The integer dictionary looks like: ", create_int_dict())
        case 7:
            print("The mixed dictionary looks like: ", create_mixed_dict())
        case 8:
            print("The update dictionary looks like: ", update_dict())
        case 9:
            print("This dictionary looks like after a certain item has been removed: ", remove_item_dict())
        case 10:
            print("This dictionary looks like: ", build_dict())
        case _:
            print("None these functions will ever called")


    if automate.lower() == "h":

        userInput = any(input("Enter any value?:_"))
        
        stringUser2 = '''
            "What function(s) do you want?\n
            Please select these options:
            (1 for is_1, 
            2 for adds_to_10, 
            3 for is_even, 
            4 for is_number, 
            5 for is_string, 
            6 for do_multiple_if,
            7 for string_even_length,
            8 for check_type)_"
        '''

    boolean_function = int(input(stringUser2))

    """
        Logic's boolean functions calls
    """

    match boolean_function:
        case 1:
            print("The result of this function is: ", is_1(userInput))
        case 2:
            print("The result of this function is: ", adds_to_10(userInput, userInput))
        case 3: 
            print("The result of this function is: ", is_even(userInput))
        case 4:
            print("The result of this function is: ", is_number(userInput))
        case 5:
            print("The result of this function is: ", is_string(userInput))
        case 6:
            print("The result of this function is: ", do_multiple_if(userInput, userInput, userInput))
        case 7:
            print("The result of this function is: ", string_even_length(userInput))
        case 8:
            print("The result of this function is: ", check_type(userInput))
        case _:
            print("None these functions will ever called")
