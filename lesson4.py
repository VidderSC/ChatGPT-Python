# Lesson 4: Functions and Modules

# 4.1 Functions with Parameters

# Create a function that calculates and returns the area of a rectangle.
# The function should take two parameters, length and width, and return the area as a float.

def area_rectangle(length: int, width: int) -> float:
    """Calculates the area of a rectangle.
    - Parameters:
    length and width are (int)
    - Returns:
    (float)"""
    return float(length * width)

# 4.2 Modules
# Create a separate Python file/module named geometry.py.
# Move the rectangle area calculation function from the previous
# exercise into this module.
# Import the geometry module into your current code and
# use the function to calculate the area of a rectangle.

# 4.3 Exercise
# Create a function that checks if a given string is a palindrome
# (reads the same forwards and backward).
# The function should take a string as input and return a boolean value
# (True if it’s a palindrome, False otherwise).
