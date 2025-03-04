# file03 use_geometry_package.py

from geometry.shapes import circle_area, rectangle_area, triangle_area

radius = 5
length = 4
width = 6
base = 3
height = 8

print(f"Area of circle with radius {radius}: {circle_area(radius):.2f}")
print(f"Area of rectangle with length {length} and width {width}: {rectangle_area(length, width)}")
print(f"Area of triangle with base {base} and height {height}: {triangle_area(base, height)}")
