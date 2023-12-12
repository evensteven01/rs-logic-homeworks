import copy

from PyDictionary import PyDictionary

def _register(*args, **kwargs):
    """ This is just for me to use in unit testing """

    # Because objects are passed by reference, need to clone
    # To know what value of a variable was at time of calling
    # since it may be updated later in code
    narg = []
    for arg in args:
        narg.append(copy.deepcopy(arg))

    nkwargs = {}
    for k, v in kwargs.items():
        nkwargs[k] = copy.deepcopy(v)
    
    _cregister(*narg, **nkwargs)

def example(*args, **kwargs):
    _register(1)

def _cregister(*args, **kwargs):
    pass

def return_greater(arg1, arg2):

    obj1 = arg1
    obj2 = arg2

    greater = lambda obj1, obj2: obj1 if obj1 > obj2 else obj2

    if isinstance(obj1, str) == str and isinstance(obj2, str) == str:
        return greater
    
    elif isinstance(obj1, int) == int and isinstance(obj2, int) == int:
        return

def _get_first_two_letters(arg1: str, arg2: str):
    
    for i in arg1:
        for j in arg2:
            return i + j

def combine_first_two(arg1: str, arg2: str):

    strObj1 = arg1
    strObj2 = arg2

    return _get_first_two_letters(strObj1, strObj2)

def positional_args(arg1: str, arg2: str, arg3: str):

    string1 = arg1
    string2 = arg2
    string3 = arg3

    _register(f'{string1} {string2} {string3}')
    _register(f'{string3} {string2} {string1}')

def sum_numbers(**kwargs):
    
    numbers = None

    if numbers is None and **kwargs is None:
        return numbers

    numbers = **kwargs

    result = sum(numbers)

    return result


def try_kwargs(string: str, integer: int, flt: float, boolean: bool, lst: list):

    str_arg = string
    int_arg = integer
    float_arg = flt
    bool_arg = boolean
    list_arg = lst

    _register(f'{str_arg} {int_arg} {float_arg} {bool_arg} {list_arg}')
    _register(f'{list_arg} {bool_arg} {float_arg} {int_arg} {str_arg}')
    _register(f'{str_arg} {list_arg} {int_arg} {bool_arg} {float_arg}')

def sum_if_param_name_starts_with_a(arg_names: list[str], arg_values: list[int]):

    param_names = PyDictionary()

    names = arg_names
    values = arg_values

    for val in values:
        if names[0] == "a":
            values += val