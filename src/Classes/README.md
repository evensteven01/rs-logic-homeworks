# HW 6
This homework will start to incorporate Classes. The goal will be to continue to build on the logic we've practiced, while working on classes.

## Playing with cubes I
Create a class called Cube. The constructor should not initialize any items. Add a method, a getter getSide(), that returns the value of a field side on the object. Also a setter setSide(int num) method for this property. Actually, getter and setter methods are not the common way to write this code in python. In the next kata of this series, we will refactor the code and make it a bit more professional...

Notes:

There's no need to check for negative values!
initialise the side to 0.

## Playing with Cubes II

You already implemented a Cube class, but now we need your help again! I'm talking about constructors. Lets add a constructor that accepts side integer!

Also we got a problem with negative values. Correct the code so negative values will be switched to positive ones!

The constructor taking no arguments should assign 0 to Cube's Side property.

## Playing with Cubes III
Add a method called getArea that calculates the area of the cube. The area of a cube is 6a^2, where a is the length of the side.

## Cubes and spheres
We need to support more shapes now.

Create a base class called Shape that both Cube and Sphere can extend. The base class should just have the getArea function. The common pattern in base classes is to provide the getArea function in the base class, but that raises an exception. Any concrete classes extending the base class must implement this function; if it does not, then the base classes' version of it will run and raise an exception.

The sphere should accept a radius in the constructor. If the radius is negative, make it positive. No need to add setters/getters.
