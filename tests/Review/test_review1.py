from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from unittest.mock import call

from src.Review.review1 import *

@pytest.mark.parametrize(
    "liters, price, exp_result",
    [
        (1.2, 5.4, 6.48),
        (2, 2.25, 4.40),
        (10, 2.3, 20.5), # 2.05
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
    "start, end, exp_result",
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
    "mpg, exp_result",
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
    "lp100, exp_result",
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
    "val1, val2, operator, exp_result",
    [
        (50, 12, "+", 5024),
        (7, 5, "-", 70),
        (13, 20, "*", 26400),
        (10, 10, "/", 101),
    ]
)
def test_sticky_calculator(val1, val2, operator, exp_result):
    # Arrange
    # Act
    act_result = sticky_calculator(operator, val1, val2)
    # Assert
    assert exp_result == act_result


@pytest.mark.parametrize(
    "estimates, exp_result",
    [
        ([(1, 2), (3, 4)], (4, 5, 6)),
        ([(2, 5), (10, 100), (4, 7)], (16, 64, 112)),
        ([(7, 13)], (7, 10, 13)),
    ]
)
def test_global_estimate(estimates, exp_result):
    # Arrange
    # Act
    act_result = global_estimate(estimates)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "args, exp_result",
    [
        ([], 0),
        ([3, 4, 5], 26),
        ([1, 4, -5, 5], 14),
    ]
)
def test_add(args, exp_result):
    # Arrange
    # Act
    act_result = add(args)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "start, end, step, exp_result",
    [
        (10, 20, 10, [10, 20]),
        (10, 20, 1, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
        (10, 20, 5, [10, 15, 20]),
        (10, 20, 7, [10, 17]),
        (20, 10, 3, []),
        (10, 20, 5, [10, 15, 20]),
    ]
)
def test_generate(start, end, step, exp_result):
    # Arrange
    # Act
    act_result = generate(start,end,step)
    # Assert
    assert exp_result == act_result

@pytest.mark.parametrize(
    "lon, exp_result",
    [
        ([1, 2, 4, 5],[3]),
        ([0, 2, 3, 5, 6, 8],[1, 4, 7]),
        ([-3, -2, 1, 5],[-1, 0, 2, 3, 4]),
    ]
)
def test_find_missing(lon, exp_result):
    # Arrange
    # Act
    act_result = find_missing(lon)
    # Assert
    assert exp_result == act_result

def test_correct_tail():
    # Arrange
    # Assert
    assert correct_tail("Fox", "x") ==  True
    assert correct_tail("Rhino", "o") == True
    assert correct_tail("Meerkat", "t") == True
    assert correct_tail("Emu", "t") == False

def test_string_repeat():
    # Assert
    assert string_repeat(3, "Fox") ==  "FoxFoxFox"
    assert string_repeat(4, "a") ==  "aaaa" 

def test_sum_no_highest_lowest():
    # Assert
    assert sum_no_highest_lowest([1,2,3,4,5]) == 9
    assert sum_no_highest_lowest([10, 34, 75, 100, 24, 734]) == 233
    assert sum_no_highest_lowest([]) == 0
    assert sum_no_highest_lowest([-2, -5, 5, 7]) == 3

def test_paper_rock_scissors():
    # Assert
    assert paper_rock_scissors("scissors", "paper") == "Player 1 won!"
    assert paper_rock_scissors("scissors", "rock") == "Player 2 won!"
    assert paper_rock_scissors("paper", "paper") == "Draw!"
    
def test_calculate_tip():
    # Assert
    assert calculate_tip(30, "poor") ==  2
    assert calculate_tip(20, "Excellent") ==  4
    assert calculate_tip(20, "hi") ==  "Rating not recognized"
    assert calculate_tip(107.65, "GReat") ==  17
    assert calculate_tip(20, "great!") ==  "Rating not recognized"

def test_shorten_to_date():
    # Assert
    assert shorten_to_date("Monday February 2, 8pm") == "Monday February 2"
    assert shorten_to_date("Tuesday May 29, 8pm") == "Tuesday May 29"
    assert shorten_to_date("Wed September 1, 3am") == "Wed September 1"
    assert shorten_to_date("Friday May 2, 9am") == "Friday May 2"
    assert shorten_to_date("Tuesday January 29, 10pm") == "Tuesday January 29"

def test_double_array():
    assert double_array([]) == []
    assert double_array([0, 1, 2]) == [0, 2, 4]
    assert double_array([-4, 1, 8, 1000, 34, 73, -1231, 54, 6, 6, 1]) == [-8, 2, 16, 2000, 68, 146, -2462, 108, 12, 12, 2]

def test_sum_2d_list():
    assert sum_2d_list([[1,2,3], [5,6]]) == 17
    assert sum_2d_list([]) == 0
    assert sum_2d_list([[]]) == 0
    assert sum_2d_list([[], [1]]) == 1
    assert sum_2d_list([[1,2,3], [5,6], [100, -200]]) == -83


def test_sums_of_lists():
    assert sums_of_lists([[1,2,3], [5,6]]) == [6,11]
    assert sums_of_lists([]) == []
    assert sums_of_lists([[0]]) == [0]
    assert sums_of_lists([[0], [1]]) == [0, 1]
    assert sums_of_lists([[1,2,3], [5,6], [100, -200]]) == [6, 11, -100]

def test_powers_of_2():
    assert powers_of_2(0) == [1]
    assert powers_of_2(1) == [1, 2]
    assert powers_of_2(2) == [1, 2, 4]
    assert powers_of_2(5) == [1, 2, 4, 8, 16, 32]

def test_count_pos_sum_neg():
    assert count_pos_sum_neg([]) == []
    assert count_pos_sum_neg([0, 0]) == [0, 0]
    assert count_pos_sum_neg([-3, -2, 4, 6, 0, -5, 12]) == [3, -10]
    assert count_pos_sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]

def test_is_all_caps():
    assert is_all_caps("c") == False
    assert is_all_caps("C") == True
    assert is_all_caps("hello I AM DONALD") == False
    assert is_all_caps("HELLO I AM DONALD") == True
    assert is_all_caps("ACSKLDFJSgSKLDFJSKLDFJ") == False
    assert is_all_caps("ACSKLDFJSGSKLDFJSKLDFJ") == True
