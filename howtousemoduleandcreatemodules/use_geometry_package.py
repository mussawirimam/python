# file03 use_geometry_package.py
# this file will use the geometry directory
# in this file we are adding the arguments for the parameters we have set in the shapes.py file
from geometry.shapes import circle_area, rectangle_area, triangle_area

radius = 5
length = 4
width = 6
base = 3
height = 8

print(f"Area of circle with radius {radius}: {circle_area(radius):.2f}")
print(f"Area of rectangle with length {length} and width {width}: {rectangle_area(length, width)}")
print(f"Area of triangle with base {base} and height {height}: {triangle_area(base, height)}")
