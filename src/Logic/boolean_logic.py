from typing import Any

def is_1(data: int) -> bool:

    data = None

    if data is None:
        return False

    for i in range(int(data)):
        if i == 1:
            return True
        else:
            return False
    print(i)

def adds_to_10(num1: int, num2: int) -> bool:

    for i in range(int(num1)):
        for j in range(int(num2)):

            result = i + j

            if ((result) == 10):
                return True
            else:
                return False
            print(result)

def is_even(num: int) -> bool:

    if (int(num) % 2 == 0):
        return True
    else:
        return False

def is_number(number: any) -> bool:
    if type(number) == int or type(number) == float or type(number) == complex:
        return True
    else:
        return False

def is_string(strNumber: any) -> bool:
    if type(strNumber) == str:
        return True
    else:
        return False

def do_multiple_if(num1: float, num2: float, num3: bool) -> bool:
    num3 = True

    if num3 is True:
        result = num1 * num2
        return result
        print(result)

    if num3 is False:
        return num1
        print(num1)

def string_even_length(length: str) -> bool:
    
    if len(length) % 2 == 0:
        return True
    else:
        return False

def check_type(data: Any) -> str:

    if type(data) == str:
        return True
    else:
        return False
    print(type(data))

    if type(data) == float or type(data) == int or type(data) == complex or type(data) == any:
        return True
    else:
        return False
    print(type(data))

    if type(data) == bool:
        return True
    else:
        return False
    print(type(data))
