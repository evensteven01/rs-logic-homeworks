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
        pass
    else:
        pass

def _get_first_two_letters(arg1: str, arg2: str):
    
    for i in arg1:
        for j in arg2:
            return i + j

def combine_first_two(arg1: str, arg2: str):
    return _get_first_two_letters(arg1, arg2)

def positional_args(arg1: str, arg2: str, arg3: str):

    string1 = arg1
    string2 = arg2
    string3 = arg3

    _register(string1, string2, string3)
    _register(string3, string2, string1)

def sum_numbers():
    pass


def try_kwargs(string: str, integer: int, flt: float, boolean: bool, lst: list):

    str_arg = string
    int_arg = integer
    float_arg = flt
    bool_arg = boolean
    list_arg = lst

    _register(str_arg, int_arg, float_arg, bool_arg, list_arg)
    _register(list_arg, bool_arg, float_arg, int_arg, str_arg)
    _register(str_arg, list_arg, int_arg, bool_arg, float_arg)

def sum_if_param_name_starts_with_a():
    
    if :
        pass
