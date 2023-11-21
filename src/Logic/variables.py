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
    _register(1, "programming")

def create_list(*num: list[int, int, int]):
    _register([1, 2, 3])

def modify_list(*num: list[int, int, int]):
    _register([1, 2, 3])

def add_item_to_list(*stringList: list[str, str]):
    _register(["name", "thing"])

def create_str_dict(**strinDict1: dict[str, str], **stringDict2: dict[str, str]):
    _register(strinDict1["fname": "Fred"], stringDict2["lname": "Jones"])

def create_int_dict(**intDict1: dict[int, int], **intDict2: dict[int, int]):
    _register(intDict1[0: 3], intDict2[0: 7])

def create_mix_dict(**mixedDict1: dict[str, int], **mixedDict2: dict[int, str]):
    _register(mixedDict1["name": 6], mixedDict2[0]: "Davis")

def update_dict():
    pass

def remove_item_dict():
    pass

def build_dict(*uniqueString: list[str, str, str], *uniqueInt: list[int, int, int]):
    _register(["fname", "lname", "mname"], [1, 2, 3])
 