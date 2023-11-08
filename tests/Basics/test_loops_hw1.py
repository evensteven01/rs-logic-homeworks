from unittest import mock
import pytest
from pytest_mock.plugin import MockerFixture

from src.Basics.loops_hw1 import *

@pytest.mark.parametrize(
	"numbers,exp_max",
	[
		(None,None),
		([],None),
		([2],2),
		([2,0,1], 2),
		([2,1,2,0], 2),
		([-10,-3,-5], -3),
	]
)
def test_get_maximum(numbers: list[float], exp_max: float) -> None:
	# Arrange

	# Act
	act_max = get_maximum(numbers)

	# Assert
	assert exp_max == act_max

@pytest.mark.parametrize(
	"numbers,exp_min",
	[
		(None,None),
		([],None),
		([2],2),
		([2,0,1], 0),
		([2,1,2,0], 0),
		([-10,-3,-5], -10),
	]
)
def test_get_minimum(numbers: list[float], exp_min: float) -> None:
	# Arrange

	# Act
	act_min = get_minimum(numbers)

	# Assert
	assert exp_min == act_min

@pytest.mark.parametrize(
	"numbers,exp_avg",
	[
		(None,None),
		([],None),
		([2],2),
		([2,0,1], 1),
		([2,1,2,0], 1.25),
		([-10,-3,-5], -6),
	]
)
def test_get_average(numbers: list[float], exp_avg: float) -> None:
	# Arrange

	# Act
	act_avg = get_average(numbers)

	# Assert
	assert pytest.approx(exp_avg, .1) == act_avg

@pytest.mark.parametrize(
	"numbers,closest_to,exp_closest",
	[
		(None,None, None),
		(None,1, None),
		([],1,None),
		([2],1,2),
		([2,0,1],.1,0),
		([2,1,2,0],1.51,2),
		([-10,-3,-5],0,-3),
	]
)
def test_get_closest(numbers: list[float], closest_to: float, exp_closest: float) -> None:
	# Arrange

	# Act
	act_closest = get_closest(numbers, closest_to)

	# Assert
	assert exp_closest == act_closest

@pytest.mark.parametrize(
	"numbers,num,exp_numbers",
	[
		(None,None, None),
		(None,1, None),
		([],1,[]),
		([2],1,[3]),
		([2,0,1],.1,[2.1,.1,1.1]),
		([2,1,2,0],-1,[1,0,1,-1]),
	]
)
def test_add_x(numbers: list[float], num: float, exp_numbers: list[float]) -> None:
	# Arrange

	# Act
	act_numbers = add_x(numbers, num)

	# Assert

	assert any([
		(exp_numbers is None and act_numbers is None),
		(
			exp_numbers is not None and act_numbers is not None and
			len(exp_numbers) == len(act_numbers) and
            all([pair[0]==pair[1] for pair in zip(exp_numbers, act_numbers)])
        )
    ])
	                            
@pytest.mark.parametrize(
	"numbers,num,exp_numbers",
	[
		(None,None, None),
		(None,1, None),
		([],1,[]),
		([2],1,[1]),
		([2,0,1],.1,[1.9,-.9,.9]),
		([2,1,2,0],-1,[3,2,3,1]),
	]
)
def test_sub_x(numbers: list[float], num: float, exp_numbers: list[float]) -> None:
	# Arrange

	# Act
	act_numbers = sub_x(numbers, num)

	# Assert

	assert any([
		(exp_numbers is None and act_numbers is None),
		(
			exp_numbers is not None and act_numbers is not None and
			len(exp_numbers) == len(act_numbers) and
            all([pair[0]==pair[1] for pair in zip(exp_numbers, act_numbers)])
        )
    ])
	
