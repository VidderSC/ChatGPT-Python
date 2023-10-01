# Lesson 7: Lists and List Manipulation

# 7.1 List Basics
# - Create a list of your favorite colors.
my_colors: list = [
    "Purple",
    "Green", 
    "Blue",
    "Black"]

# - Print out the number of colors in the list.
print(len(my_colors))

# - Print out the first and last colors in the list.
print(my_colors[0])
print(my_colors[-1])

# 7.2 List Manipulation
# - Add a new color to your list of favorite colors.
my_colors.append("Pink")
print(my_colors)

# - Remove one of the colors from the list.
my_colors.remove("Green")
print(my_colors)

# - Sort the list of colors in alphabetical order.
my_colors.sort()
print(my_colors)
print()

# 7.3 Exercise
# - Write a function that takes a list of numbers and returns
# the sum of all the numbers in the list.
# Use typed variables and return types.

def sum_all_numbers(numbers: list) -> int:
    """Sum all numbers in a provided list

    Args:
        numbers (list): List of numbers to add

    Returns:
        int: Total of the sum
    """
    total: int = 0
    for num in numbers:
        total += num
    return total

numbers_list: list = [number for number in range(1,11)]
print(sum_all_numbers(numbers_list))