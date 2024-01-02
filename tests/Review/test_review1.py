from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from unittest.mock import call

from src.Review.review1 import *

@pytest.mark.parametrize(
    "liters,price,exp_result",
    [
        (1.2, 5.4, 6.48),
        (2, 2.25, 4.40),
        (10, 2.3, 2.05), # 2.05
        (15.7, 7.34, 111.31), # 15.7 * (7.34-.25) = 
        (0, 5.4, 0),
        (100, 0, 0),                                                                                                                                                         
        (100, 0, 0),
    ]
)
def test_fuel_cost(liters: float, price: float, exp_result: float, mocker: MockerFixture):
    # Arrange
    # Act
    act_result = fuel_cost(liters, price)

    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "start,end,exp_result",
    [
        (1, 5, [1,2,3,4,5]),
        (-1, 0, [-1,0]),
        (-2, 3, [-2,-1,0,1,2,3]),
        (0, 0, [0]),
        (2, 1, []),
    ]
)
def test_ints_between(start: int, end: int, exp_result):
    # Arrange
    # Act
    act_result = ints_between(start,end)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "mpg,exp_result",
    [
        (42, 5.60),
        (10, 23.52),
        (1, 235.21),
    ]
)
def test_mpg2lp100km(mpg: float, exp_result: float):
    # Arrange
    # Act
    act_result = mpg2lp100km(mpg)
    # Assert
    assert pytest.approx(act_result, .01) == exp_result

@pytest.mark.parametrize(
    "lp100,exp_result",
    [
        (9, 26.13),
    ]
)
def test_lp100km2mpg(lp100: float, exp_result: float):
    # Arrange
    # Act
    act_result = lp100km2mpg(lp100)
    # Assert
    assert pytest.approx(act_result, .01) == exp_result


@pytest.mark.parametrize(
    "val1,val2,operator,exp_result",
    [
        (50, 12, "+",5024),
        (7, 5, "-",70),
        (13, 20, "*",26400),
        (10, 10, "/",101),
    ]
)
def test_sticky_calculator(val1, val2, operator, exp_result):
    # Arrange
    # Act
    act_result = sticky_calculator(operator, val1, val2)
    # Assert
    assert exp_result == act_result


@pytest.mark.parametrize(
    "estimates,exp_result",
    [
        ([(1,2), (3,4)], (4,5,6)),
        ([(2,5), (10,100), (4,7)], (16,64,112)),
        ([(7,13)], (7,10,13)),
    ]
)
def test_global_estimate(estimates, exp_result):
    # Arrange
    # Act
    act_result = global_estimate(*estimates)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "args,exp_result",
    [
        ([], 0),
        ([3,4,5], 26),
        ([1,4,-5,5], 14),
    ]
)
def test_add(args, exp_result):
    # Arrange
    # Act
    act_result = add(*args)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "start,end,step,exp_result",
    [
        (10,20,10, [10,20]),
        (10,20,1, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        (10,20,5, [10,15,20]),
        (10,20,7, [10,17]),
        (20,10,0, []),
        (10,20,-5, []),
    ]
)
def test_generate(start, end, step, exp_result):
    # Arrange
    # Act
    act_result = generate(start,end,step)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "lon,exp_result",
    [
        ([1,2,4,5],[3]),
        ([0,2,3,5,6,8],[1,4,7]),
        ([-3,-2,1,5],[-1,0,2,3,4]),
    ]
)
def test_find_missing(lon, exp_result):
    # Arrange
    # Act
    act_result = find_missing(lon)
    # Assert
    assert exp_result == act_result