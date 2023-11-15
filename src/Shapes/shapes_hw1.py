# this module will find largest and smallest area of each shapes and compare them which has largest or smallest area
# import shape from models
from src.Shapes.models import Shape

# this function is to find the largest area from whichever the shape has
def largestArea(listOfShapes: list[Shape])-> Shape:
    biggest = None
    for shp in listOfShapes:
        if biggest is None:
            biggest = shp
        elif biggest.area() < shp.area():
            biggest = shp
    return biggest

# this function is to find the smallest area from whichever the shape has
def smallestArea(listOfShapes: list[Shape])-> Shape:
    smallest = None
    for shp in listOfShapes:
        if smallest is None:
            smallest = shp
        elif smallest.area() > shp.area():
            smallest = shp
    return smallest