from typing import Any

from .models import Person

def is_1(data: int) -> bool:

    if data == 1:
        return True
    else:
        return False

def adds_to_10(num1: int, num2: int) -> bool:

    if num1 + num2 == 10:
        return True
    else:
        return False

def is_even(num: int) -> bool:

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    if num % 2 == 0:
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

def do_multiple_if(num1: float, num2: float, do_multiply: bool) -> bool:

    if do_multiply:
        result = num1 * num2
        return result

    if not do_multiply:
        return num1

def string_even_length(length: str) -> bool:
    
    if len(length) % 2 == 0:
        return True
    else:
        return False

def check_type(data: Any) -> str:

    if type(data) == bool:
        return "boolean"

    if type(data) == str:
        return "string"

    if type(data) == float or type(data) == int or type(data) == complex or type(data) == any:
        return "number"
    else:
        return "other"

def correct_math(num1: float, num2: float, answer: float, operation: str):
    
    if operation == "*":
        if (num1 * num2) == answer:
            return True
        else:
            return False

    elif operation == "/":
        if (num1 / num2) == answer:
            return True
        else:
            return False

    elif operation == "+":
        if (num1 + num2) == answer:
            return True
        else:
            return False

    elif operation == "-":
        if (num1 - num2) == answer:
           return True
        else:
            return False
    else:
        raise NotImplementedError

def contains_word(sentence: str, needle: str):

    if needle in sentence:
        return True
    else:
        return False                                                                                                                                                                                               

def has_duplicates(list_of_things: list[Any]):

    if len(list_of_things) != len(set(list_of_things)):
        return True
    else:
        return False

def any_family(persons: list[Person]):

    lastNames = [p.last_name for p in persons]
    
    if len(lastNames) == len(set(lastNames)):
        return False
    else:
        return True