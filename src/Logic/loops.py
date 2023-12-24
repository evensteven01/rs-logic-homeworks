from src.Logic.utils import _register

def iter_list(anyList: list[Any]):
    
    for al in anyList:
        _register(al)

def even_iter_list(anyList: list[Any]):
    
    count = 0

    for item in anyList:
        if item % 2 == 0:
            _register(item)
        count += 1

def input_until():

    while True:
        userInput = input("To break out the loop, enter X or type Exit:_")

        if userInput == "X" or userInput == "Exit":
            _register(userInput)
            break

def iter_dict_keys(dictKeys: dict[Any, Any]):
    
    for k, val in dictKeys:
        _register(k.keys())

def iter_dict_values(dictValues: dict[Any, Any]):
    
    for keys, val in dictValues:
        _register(val.values())

def iter_empty_dict_keys(emptyDict: dict[Any, Any]):
    
    for k, val in emptyDict:
        if val.values() is None:
           _register(k.keys())

def iter_dict_except(variableDict: dict[Any, Any], one: Any):
    
    for itemDict in variableDict:
        if itemDict.keys() != one and itemDict.values() != one:
            _register(itemDict.items())
