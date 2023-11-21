from src.Logic.variables import *

def main():
    automate = input("Do you want to input(i), or hardcode(h)?:_")

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
            print()
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 5:
            print()
        case 6:
            print()
        case 7:
            print()
        case 8:
            print()
        case 9:
            print()
        case 10:
            print()
        case _:
            print("None these functions will ever called")
