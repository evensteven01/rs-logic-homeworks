from random import randint
from typing import Union

from faker import Faker
import pytest

from src.Logic.boolean_logic import *


@pytest.mark.parametrize(
    "data,exp_result",
    [
        (3, False),
        (-1, False),
        ("1", False),
        ("Lmnop", False),
        (1, True),
    ]
)
def test_is_1(data, exp_result):
    # Arrange
    # Act
    result = is_1(data)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "num_1,num_2,exp_result",
    [
        (3,6,False),
        (-1,9,False),
        (-1,-9,False),
        (9,.9,False),
        (2,8,True),
        (1,9,True),
        (7,3,True),
        (100,-90,True),
    ]
)
def test_adds_to_10(num_1, num_2, exp_result):
    # Arrange
    # Act
    result = adds_to_10(num_1, num_2)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "data,exp_result",
    [
        (3, False),
        (-1, False),
        ("2", False),
        (2.1, False),
        (2, True),
        (180, True),
    ]
)
def test_is_even(data, exp_result):
    # Arrange
    # Act
    result = is_even(data)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "data,exp_result",
    [
        (3, True),
        (-1, True),
        ("2", False),
        (0, True),
        (7.8, True),
        (True, False),
    ]
)
def test_is_number(data, exp_result):
    # Arrange
    # Act
    result = is_number(data)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "data,exp_result",
    [
        (3, False),
        (-1, False),
        ("2", True),
        ("Hello", True),
        (["String"], False),
        ("", True),
        (True, False),
    ]
)
def test_is_string(data, exp_result):
    # Arrange
    # Act
    result = is_string(data)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "num_1,num_2,do_mult,exp_result",
    [
        (3,2,True,6),
        (3,2.4,True,7.2),
        (3.1,2.4,False,3.1),
        (1,7,False,1),
    ]
)
def test_do_multiple_if(num_1,num_2,do_mult,exp_result):
    # Arrange
    # Act
    result = do_multiple_if(num_1,num_2,do_mult)

    # Assert
    assert pytest.approx(exp_result, .1) == result

@pytest.mark.parametrize(
    "data,exp_result",
    [
        ("True",True),
        ("False", False),
        ("This is a sentence. And another", False),
        ("This is a sentence. And another.", True),
    ]
)
def test_string_even_length(data,exp_result):
    # Arrange
    # Act
    result = string_even_length(data)

    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "data,exp_result",
    [
        ("True","string"),
        ("2", "string"),
        (1, "number"),
        (3.4, "number"),
        (-99, "number"),
        (True, "boolean"),
        (False, "boolean"),
        ([], "other"),
        ([1], "other"),
        (["string"], "other"),
        ([True], "other"),
        (Exception, "other"),
    ]
)
def test_check_type(data,exp_result):
    # Arrange
    # Act
    result = check_type(data)

    # Assert
    assert exp_result == result


@pytest.mark.parametrize(
    "num1,num2,answer,operation,correct_answer,error_exp",
    [
        (1,2,3,"+",True, False),
        (1,2,4,"+",False, False),
        (2,3,-1,"-",True, False),
        (2,3,-1,"-",True, False),
        (2,-3,5,"-",True, False),
        (2,-3,-6,"*",True, False),
        (2,0,0,"*",True, False),
        (2,1,2,"/",True, False),
        (2.2,1.1,2,"/",True, False),
        (2.2,2,1,"/",False, False),
        (2.2,2,1,"^",False, True),
    ]
)
def test_correct_math(num1: float, num2: float, answer: float, operation: str, correct_answer: bool, error_exp: bool):
    # Arrange
    # Act & Assert
    if error_exp:
        with pytest.raises(NotImplementedError) as exc:
            result = correct_math(num1, num2, answer, operation)
    else:
        result = correct_math(num1, num2, answer, operation)
        assert correct_answer == result

@pytest.mark.parametrize(
    "sentence,needle,exp_answer",
    [
        ("This is a sentence","is",True),
        ("This is a sentence","be",False),
        ("This is a sentence","s a",True),
        ("This is a sentence","This",True),
        ("This is a sentence","is a",True),
        ("This is a sentence","iS",False),
    ]
)
def test_contains_word(sentence: str, needle: str, exp_answer):
    # Arrange
    # Act
    answer = contains_word(sentence, needle)
    # Assert
    assert exp_answer == answer


@pytest.mark.parametrize(
    "list_of_things,exp_result",
    [
        (["1", 1, 2, 3],False),
        (["This", "This", "yes"],True),
        (["This", "this", "no"],True),
        ([2, 2.1, 3],False),
        ([2.0, 2, 4],True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.3, 8.9, 9, 10],True),
        ([True, False],False),
        ([],False),
    ]
)
def test_has_duplicates(list_of_things: list[Any], exp_result: bool):
    # Arrange
    # Act
    result = has_duplicates(list_of_things)
    # Assert
    assert exp_result == result


@pytest.mark.parametrize(
    "has_duplicate",
    [
        (True,),
        (False,),
    ]
)
def test_has_duplicates_huge(has_duplicate: bool):
    # Arrange
    ct = 50000
    huge_list = [{randint() for i in range(ct)}]
    if has_duplicate:
        rand_index = randint(1,ct-1)
        huge_list[rand_index] = huge_list[rand_index-1]
    
    # Act
    result = has_duplicates(huge_list)
    # Assert
    assert has_duplicate == result

@pytest.mark.parametrize(
    "last_name_list,exp_result",
    [
        (["Fordham", "Greiger", "Lanzer"], False),
        (["Rodman", "Thompson", "Rodman"], True),
        (["Fordham", "Ford", "Nelson"], False),
        (["Fordham", "Ford", "Nelson", "Einstein", "Basten", "Dresdo", "Franks", "Frenchmen", "Smith", "Ironman"], False),
        (["Fordham", "Ford", "Nelson", "Einstein", "Basten", "Dresdo", "Franks", "Frenchmen", "Smith", "Ironman", "Basten", "Kurkowski"], True),
    ]
)
def test_any_family(last_name_list, exp_result: bool, faker: Faker):
    # Arrange
    person_list = [Person(faker.first_name(), l_name) for l_name in last_name_list]

    # Act
    result = any_family(person_list)

    # Assert
    assert exp_result == result
