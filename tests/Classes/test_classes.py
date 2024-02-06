from faker import Faker
import pytest
from pytest_mock.plugin import MockerFixture
from unittest.mock import call

from src.Classes.classes1 import *

def test_create_cube1():
    # Arrange
    # Assert
    cube1 = Cube()
    assert cube1.side == 0

    assert cube1.getSide() == 0
    cube1.setSide(2)
    assert cube1.getSide() == 2

    cube2 = Cube()
    cube2.setSide(3)
    assert cube2.getSide() == 3
    assert cube1.getSide() == 2
    assert cube1 != cube2

def test_create_cube2():
    # Arrange
    # Assert
    cube1 = Cube(4)
    assert cube1.side == 4

    assert cube1.getSide() == 4
    cube1.setSide(2)
    assert cube1.getSide() == 2

    cube2 = Cube(-7)
    assert cube2.getSide() == 7

def test_cube_area():
    # Arrange
    # Assert
    cube1 = Cube(4)
    assert cube1.side == 4
    assert cube1.getArea() == 96


def test_cubes_spheres():
    cube1 = Cube(4)
    assert isinstance(cube1, Shape)

    sphere1 = Sphere(5)
    assert isinstance(sphere1, Shape)
    assert sphere1.radius == 5
    assert pytest.approx(sphere1.getArea(), .01) == 314.15926536  
