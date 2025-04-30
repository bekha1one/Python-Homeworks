1. Square Calculations
# Given a side of square, find its perimeter and area
side = float(input("Enter the side length of the square: "))
perimeter = 4 * side
area = side ** 2
print(f"Perimeter: {perimeter}, Area: {area}")

2. Circle Circumference
# Given diameter of circle, find its length (circumference)
import math
diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"Circumference: {circumference}")

3. Mean of Two Numbers
# Given two numbers a and b, find their mean
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
mean = (a + b) / 2
print(f"Mean of {a} and {b} is {mean}")

4. Operations on Two Numbers
# Given two numbers a and b, find their sum, product and square of each number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_result = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2

print(f"Sum: {sum_result}")
print(f"Product: {product}")
print(f"Square of {a}: {square_a}")
print(f"Square of {b}: {square_b}")
