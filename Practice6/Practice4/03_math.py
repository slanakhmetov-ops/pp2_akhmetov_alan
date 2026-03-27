#1 Write a Python program to convert degree to radian
import math
degree = float(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", round(radian, 6))

#2 Write a Python program to calculate the area of a trapezoid.
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
trapezoid_area = (a + b) / 2 * h
print("Expected Output:", trapezoid_area)

#3 Write a Python program to calculate the area of regular polygon.
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
polygon_area = (n * s * s) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", int(polygon_area))

#4 Write a Python program to calculate the area of a parallelogram.
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
parallelogram_area = base * height
print("Expected Output:", parallelogram_area)