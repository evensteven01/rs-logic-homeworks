from src.Logic.variables import *
from src.Logic.boolean_logic import *

def main():
    
    """
        Logic's functions calls
    """
    create_vars()
    create_list()
    modify_list()
    add_item_to_list()
    create_str_dict()
    create_int_dict()
    create_mixed_dict()
    update_dict()
    remove_item_dict()
    build_dict()

    """
        Logic's boolean functions calls
    """

    automate = input("Enter your input(i)?:_")
                    
    if automate.lower() == "i":
        
        stringUser = '''
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

        userInput = any(input("Enter any value?:_"))
        userInput2 = any(input("Enter any value?:_"))
        useraAnyInput  = any(input("Enter any value?:_"))
        userAny2Input = any(input("Enter any?:_"))
        userFloat1Input = float(input("Enter float1?:_"))
        userFloat2Input = float(input("Enter float2?:_"))
        userBooleanInput = bool(input("Enter boolean?:_"))
        userStrInput = input("Enter string?:_")
        userAny3Input = any(input("Enter any?:_"))

    boolean_function = int(input(stringUser))

    match boolean_function:
        case 1:
            print("The result of this function is: ", is_1(userInput))
        case 2:
            print("The result of this function is: ", adds_to_10(userInput, userInput2))
        case 3: 
            print("The result of this function is: ", is_even(userInput))
        case 4:
            print("The result of this function is: ", is_number(userAnyInput))
        case 5:
            print("The result of this function is: ", is_string(userAny2Input))
        case 6:
            print("The result of this function is: ", do_multiple_if(userFloat1Input, userFloat2Input, userBooleanInput))
        case 7:
            print("The result of this function is: ", string_even_length(userStrInput))
        case 8:
            print("The result of this function is: ", check_type(userAny3Input))
        case _:
            print("None these functions will ever called")
