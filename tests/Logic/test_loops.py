from typing import Any

from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from unittest.mock import call

from src.Logic.loops import *

@pytest.mark.parametrize(
    "loi",                                                              
    [
        (["123","224","456"]),
        (["Bobby","car","Boca"]),
        ([1,2,3]),
        ([]),
    ]
)
def test_iter_list(loi: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(item) for item in loi]

    # Act
    iter_list(loi)

    # Assert
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "loi,exp_calls",                                                              
    [
        (["123","224","456"],["123","456"]),
        (["Bobby","car","Boca","Truck"],["Bobby","Boca"]),
        ([1,2],[1]),
        ([],[]),
    ]
)
def test_even_iter_list(loi: list[Any], exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(item) for item in exp_calls]

    # Act
    even_iter_list(loi)

    # Assert
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "user_input, exp_calls",
    [
        (["hi", "bye", "x"], ["hi", "bye"]),
        (["exit"], []),
        (["Exit", "exit"], ["Exit"]),
    ]
)
def test_input_until(user_input: list[Any], exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    register = mocker.patch("src.Logic.loops.input", side_effect=user_input)
    exp_calls = [call(item) for item in exp_calls]

    # Act
    input_until()

    # Asset
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "dct,exp_calls",                                                              
    [
        ({"a": 1, "b": 2, "c": 3},["a","b","c"]),
        ({1: "One", 2: "Two", 3: "Three"},[1,2,3]),
        ({"one": 1, 2: "Two"},["one", 2]),
        ({},[]),
    ]
)
def test_iter_dict_keys(dct: dict[Any,Any], exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(item) for item in exp_calls]

    # Act
    iter_dict_keys(dct)

    # Assert
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "dct,exp_calls",                                                              
    [
        ({"a": 1, "b": 2, "c": 3},[1,2,3]),
        ({1: "One", 2: "Two", 3: "Three"},["One", "Two", "Three"]),
        ({"one": 1, 2: "Two"},[1, "Two"]),
        ({},[]),
    ]
)
def test_iter_dict_values(dct: dict[Any,Any], exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(item) for item in exp_calls]

    # Act
    iter_dict_values(dct)

    # Assert
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "dct,exp_calls",                                                              
    [
        ({"a": 1, "b": 2, "c": 3},[]),
        ({1: "One", 2: "Two", 3: None},[3]),
        ({"one": 1, 2: "Two", 3: None, "Four": None, "5": 5},[3, "Four"]),
        ({},[]),
    ]
)
def test_iter_empty_dict_keys(dct: dict[Any,Any], exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(item) for item in exp_calls]

    # Act
    iter_empty_dict_keys(dct)

    # Assert
    register.assert_has_calls(exp_calls)

@pytest.mark.parametrize(
    "dct,no,exp_calls",                                                              
    [
        ({"a": 1, "b": 2, "c": 3}, "d",[("a", 1), ("b",2), ("c",3)]),
        ({"a": 1, "b": 2, "c": 3}, "a",[("b",2), ("c",3)]),
        ({1: "One", 2: "Two", 3: None}, None,[(1, "One"), (2, "Two")]),
        ({"one": 1, 2: "Two", 3: "one", "Four": None, "5": 5},"one", [(2, "Two"), ("Four", None), ("5", 5)]),
        ({},1,[]),
    ]
)
def test_iter_dict_except(dct: dict[Any,Any], no: Any, exp_calls: list[Any], mocker: MockerFixture):
    # Arrange
    register = mocker.patch("src.Logic.utils._cregister")
    exp_calls = [call(*item) for item in exp_calls]

    # Act
    iter_dict_except(dct,no)

    # Assert
    register.assert_has_calls(exp_calls)
