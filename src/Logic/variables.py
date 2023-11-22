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

def create_vars():

    number = 7
    text = "name"

    _register(number, text)

def create_list():
    number = [1, 2, 3]

    _register(number)

def modify_list():
   number = [1, 2, 3] # [2,3,4]

   _register(number)

   for i, v in enumerate(number):
        number[i] += 1

   _register(number)

def add_item_to_list():
    text = ["fname", "lname"]

    _register(text)

    text.append("mname")

    _register(text)

def create_str_dict():
    stringDict = {"fname": "Bob", "lname": "Davis"}

    _register(stringDict)

    stringDict["mname"] = ".L"

    _register(stringDict)

def create_int_dict():
    numDict = {0: 3, 1: 7}

    _register(numDict)

    numDict[2] = 10

    _register(numDict)

def create_mixed_dict():
    mixedDict = {"fname": 1, 0: "Davis"}

    _register(mixedDict)

    mixedDict[4.0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    _register(mixedDict)

def update_dict():
    updateDict = {"fname": "Billy", "lname": 7, 0: "Davis", 4: 100, 5.4: 7.9, "fun": 7.6, 5.9: "strict", 10: -5.6}

    _register(updateDict)

    updateDict.update({"fun": -5.4})

    _register(updateDict)

def remove_item_dict():
    anyDict = {0: 4, "string": "Wilfred"}

    _register(anyDict)

    del anyDict["string"]

    _register(anyDict)

def build_dict():
    stringList = ["name", "place", "thing"]
    intList = [1, 2, 3]

    _register(stringList, intList)

    buildDict = {stringList[i]: intList[i] for i in range(len(stringList))}

    _register(buildDict)