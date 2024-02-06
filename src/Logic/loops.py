from src.Logic.utils import _register

def iter_list(anyList: list[any]):
    
    for al in anyList:
        _register(al)

def even_iter_list(anyList: list[any]):

    for ele, val in enumerate(anyList):
        if ele % 2 == 0:
            _register(val)

def input_until():

    userInput = ""

    while userInput != "x" or userInput != "exit":
        userInput = input("To break the loop, enter x or type exit:_")

        if userInput == "x" or userInput == "exit":
            break
            
        _register(userInput)

def iter_dict_keys(dictKeys: dict[any, any]):
    
    for key, tupleValues in dictKeys.items():
        _register(key)

def iter_dict_values(dictValues: dict[any, any]):
    
    for key, value in dictValues.items():
        _register(value)

def iter_empty_dict_keys(emptyDict: dict[any, any]):
    
    for key, value in emptyDict.items():
        if value is None:
           _register(key)

def iter_dict_except(variableDict: dict[any, any], one: any):
    
    for key, value in variableDict.items():
        if key != one and value != one:
            _register(key, value)
