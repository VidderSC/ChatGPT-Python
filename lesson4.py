# Lesson 4: Functions and Modules

# 4.1 Functions with Parameters

# Create a function that calculates and returns the area of a rectangle.
# The function should take two parameters, length and width, and return the area as a float.

from geometry import area_rectangle

# 4.2 Modules
# Create a separate Python file/module named geometry.py.
# Move the rectangle area calculation function from the previous
# exercise into this module.
# Import the geometry module into your current code and
# use the function to calculate the area of a rectangle.

print(area_rectangle(10, 2))

# 4.3 Exercise
# Create a function that checks if a given string is a palindrome
# (reads the same forwards and backward).
# The function should take a string as input and return a boolean value
# (True if it’s a palindrome, False otherwise).

def is_palindrome(word: str) -> bool:
    """Checks if the word is a palindrome

    Args:
        word (str)

    Returns:
        bool
    """
    word_reversed: str = ""
    for letter in word.lower():
        word_reversed = letter + word_reversed
    if word.lower() == word_reversed:
        return True
    return False

print(is_palindrome("Anna"))
