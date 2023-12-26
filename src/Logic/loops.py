from src.Logic.utils import _register

def iter_list(anyList: list[any]):
    
    for al in anyList:
        _register(al)

def even_iter_list(anyList: list[any]):
    
    count = 0

    for item in anyList:
        if int(item) % 2 == 0:
            _register(item)
        count += 1

def input_until():

    while True:
        userInput = input("To break out the loop, enter X or type Exit:_")

        if userInput == "X" or userInput == "Exit":
            _register(userInput)
            break

def iter_dict_keys(dictKeys: dict[any, any]):
    
    getKeys = [ele for key in dictKeys for ele in key]

    _register(getKeys)

def iter_dict_values(dictValues: dict[any, any]):
    
    for key, tupleValues in dictValues.items():
        for value in tupleValues:
            _register(value)

def iter_empty_dict_keys(emptyDict: dict[any, any]):
    
    for key, tupleValues in emptyDict.items():
        for value in tupleValues:
            if value is None:
               _register(key)

def iter_dict_except(variableDict: dict[any, any], one: any):
    
    for itemDict in variableDict.items():
        if itemDict.keys() != one and itemDict.values() != one:
            _register(itemDict.items())
