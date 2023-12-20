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

    greater = lambda a1, a2: a1 if a1 > a2 else a2

    if isinstance(arg1, str) and isinstance(arg2, str):
        return greater(arg1, arg2)
    
    elif isinstance(arg1, int) and isinstance(arg2, int):
        return greater(arg1, arg2)

def _get_first_two_letters(arg1: str):

    if arg1 is None:
        return None

    if arg1 == "":
        return ""

    if len(arg1) == 1:
        return arg1

    return arg1[0] + arg1[1]

def combine_first_two(arg1: str, arg2: str):

    strObj1 = _get_first_two_letters(arg1)
    strObj2 = _get_first_two_letters(arg2)

    return strObj1 + strObj2

def positional_args(arg1: str, arg2: str, arg3: str):

    _register(arg1, arg2, arg3)
    _register(arg3, arg2, arg1)

def sum_numbers(numbers):
    
    total = 0

    for i in numbers:
        total += int(i)

    return total

def try_kwargs(string: str, integer: int, flt: float, boolean: bool, lst: list):

    _register(string = string, integer = integer, flt = flt, boolean = boolean, lst = lst)
    _register(lst = lst, boolean = boolean, flt = flt, integer = integer, string = string)
    _register(string = string, lst = lst, integer = integer, boolean = boolean, flt = flt)

# sum_if_param_name_starts_with_a() -> 0
# sum_if_param_name_starts_with_a(a=3, abby=5, craig=6) -> 8
# sum_if_param_name_starts_with_a(bobby=6, johnny=10, greg=True) -> 0
def sum_if_param_name_starts_with_a(**kwargs):

    total = 0

    for key, value in kwargs.items():
        if key[0] == "a":
            total += value

    return total