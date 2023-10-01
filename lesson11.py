# Lesson 11: Functions and Function Parameters

# 11.1 Function Basics
# - Create a function that takes two integers as input and returns their sum.

def add_two_numbers(num1: int, num2: int) -> int:
    """Add the two provided numbers

    Args:
        num1 (int), num2 (int)

    Returns:
        int: The sum of the two numbers
    """
    return num1+num2

# - Test your function with different integer inputs.

print(add_two_numbers(2,2))
print(add_two_numbers(3,4))
print()

# 11.2 Function with Default Parameters
# - Modify your previous function to have a default parameter, like `b=0`.
# - This parameter should be added to the second integer before
#   calculating the sum.

def add_two_numbers_b(num1: int, num2: int = 0) -> int:
    """Add the two provided numbers

    Args:
        num1 (int), 
        num2 (int) by default is 0 unless provided otherwise

    Returns:
        int: The sum of the two numbers
    """
    return num1+num2


# - Test your function with and without providing the default parameter.
print(add_two_numbers_b(2))
print(add_two_numbers_b(3,4))
print()

# 11.3 Exercise
# - Write a function that takes a list of numbers and returns
#   the product of all the numbers in the list.

numbers_list: list = [num for num in range (1,6)]

def multiply_numbers_in_list(numbers: list) -> int:
    total: int = 1
    for number in numbers:
        total = total * number
    return total

print(multiply_numbers_in_list(numbers_list))