from random import randint
import sys
from typing import Union, Optional

from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from unittest.mock import call

from src.Logic.functions import *
from src.Logic import functions


@pytest.mark.parametrize(
    "arg1,arg2,exp_result",
    [
        (3,2,3),
        (-5,-2,-2),
        ("1","2","2"),
        ("10","2","2"),
        ("Bob","car","car"),
    ]
)
def test_return_greater(arg1, arg2, exp_result):
    # Arrage & Act
    result = return_greater(arg1,arg2)
    # Assert
    assert exp_result == result

@pytest.mark.parametrize(
    "arg1,arg2,exp_result",
    [
        ("123","224","1222"),
        ("Bobby","car","Boca"),
        ("nickel","cern","nice"),
        ("Pickle","n","Pin"),
        ("","Hi","Hi"),
        ("","",""),
    ]
)
def test_combine_first_two(arg1: str, arg2: str, exp_result: str, mocker: MockerFixture):
    # Arrange
    curr_mod = sys.modules[__name__]
    spy_get_first_two_letters = mocker.spy(functions, "_get_first_two_letters")

    # Act
    result = functions.combine_first_two(arg1, arg2)
    # Assert
    assert result == exp_result
    assert spy_get_first_two_letters.call_args_list == [
        call(arg1),
        call(arg2),
    ]

@pytest.mark.parametrize(
    "arg1,arg2,arg3",                                                              
    [
        ("123","224","456"),
        ("Bobby","car","Boca"),
        ("nickel","cern","nice"),
        ("Pickle","n","Pin"),
        ("","Hi","Hi"),
        ("a","",""),
    ]
)
def test_positional_args(arg1: str, arg2: str, arg3: str, mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.functions._cregister")

    # Act
    positional_args(arg1, arg2, arg3)

    # Assert
    register.assert_has_calls([
        call(arg1, arg2, arg3),
        call(arg3, arg2, arg1),
    ])


@pytest.mark.parametrize(
    "lon,exp_result",
    [
        ([],0),
        ([7],7),
        ([2,4],6),
        ([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],45),
    ]
)
def test_sum_numbers(lon: list, exp_result, mocker: MockerFixture):
    # Arrange & # Act
    result = sum_numbers(lon)
    # Assert
    assert exp_result == result


@pytest.mark.parametrize(
    "string, integer, flt, boolean, lst",
    [
        ("bob", 2, 4.6, True, [1,2]),
        ("Jean", -5, 6, False, ["a", "b"]),
        ("", 0, .1, False, []),
    ]
)
def test_try_kwargs(string: str, integer: int, flt: float, boolean: bool, lst: list, mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.functions._cregister")

    # Act
    try_kwargs(string, integer, flt, boolean, lst)

    # Assert
    register.assert_has_calls([
        call(string=string, integer=integer, flt=flt, boolean=boolean, lst=lst),
        call(lst=lst, boolean=boolean, flt=flt, integer=integer, string=string),
        call(string=string, lst=lst, integer=integer, boolean=boolean, flt=flt),
    ])


@pytest.mark.parametrize(
    "arg_names,arg_values,exp_result",
    [
        (["ardvark", "bark", "angel"], [3, 6, 8], 11),
        (["ben", "bark", "angel"], [3, 6, 8], 8),
        (["ben", "bark", "zoo"], [3, 6, 8], 0),
        ([], [], 0),
        (["a", "ab", "abc", "d", "asf", "z", "ate"], [2,5,7,8,1,3,11], 26),
    ],
)
def test_sum_if_param_name_starts_with_a(arg_names: list[str],arg_values: list[int],exp_result) -> None:
    # Arrange
    kwargs = {arg_names[i]: arg_values[i] for i in range(len(arg_names))}

    # Act
    result = sum_if_param_name_starts_with_a(**kwargs)

    # Assert
    assert exp_result == result
