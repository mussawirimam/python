# file02 geometry/shapes.py

import math

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width): # we are setting the parameter in the function called rectangle_area
    return length * width # this is the argument that where we can do the computation (basically used as the phantom variable when we call this function)

def triangle_area(base, height):
    return 0.5 * base * height
