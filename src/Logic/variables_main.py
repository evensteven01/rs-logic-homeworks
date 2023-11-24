from src.Logic.variables import *

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
