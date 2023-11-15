import copy

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

def _cregister(*args, **kwargs):
    pass

def example():
    """ Just an example of how to call _catcher """
    _register(1)

def create_vars(num: int, text: str):
    _register(2, "")

def create_list():
    pass

def modify_list():
    pass

def add_item_to_list():
    pass

def create_str_dict():
    pass

def create_int_dict():
    pass

def create_mix_dict():
    pass

def update_dict():
    pass

def remove_item_dict():
    pass

def build_dict():
    pass
