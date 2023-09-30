# Lesson 3: Control Flow and Loops

# 3.1 If Statements
# Check if a variable is greater than 10.
# Print a message if it is.

def check_and_print_greater_than_10(value: int) -> None:
    """
    Check if a number is greater than 10 and print a message.

    Parameters:
    value (int): The number to check.

    Returns:
    None
    """
    if value > 10:
        print(f"{value} is greater than 10")

numero: int = 12
check_and_print_greater_than_10(numero)

# 3.2 For Loops
# Create a list of numbers from 1 to 5.
# Use a for loop to print each number in the list.

def print_numbers_in_list(numbers: list) -> None:
    """
    Print each number in a list.

    Parameters:
    numbers (list): The list of numbers to print.

    Returns:
    None
    """
    for num in numbers:
        print(num)

numbers_list: list = list(range(1, 6))
print_numbers_in_list(numbers_list)

# 3.3 While Loops
# Count from 1 to 3 and print each number.

def count_and_print_numbers(number: int) -> None:
    """
    Count from 1 to a given number and print each number.

    Parameters:
    number (int): The number to count up to.

    Returns:
    None
    """
    start_number: int = 1
    while start_number <= number:
        print(start_number)
        start_number += 1

count_and_print_numbers(3)

# 3.4 Exercise
# Create a function that prints all even numbers from 1 to n.

def print_even_numbers(number: int) -> None:
    """
    Print even numbers from 1 to a given number.

    Parameters:
    number (int): The number to print even numbers up to.

    Returns:
    None
    """
    for num in range(1, number + 1):
        if num % 2 == 0:
            print(num)

print_even_numbers(10)
