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
