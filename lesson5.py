# Lesson 5: Lists and List Comprehensions

# 5.1 Lists
# - Create a list of your favorite fruits.
favorite_fruits: list = [
    "Strawberry", "Watermelon", "Kiwi", "Dragonfruit", "Banana"]

# - Print out the first and last items in the list.
print(favorite_fruits[0])
print(favorite_fruits[-1])
print()

# 5.2 List Comprehensions
# - Create a list of numbers from 1 to 10 using a list comprehension.
numbers_list: list = [number for number in range(1,11)]
print(numbers_list)
print()

# - Create a new list that contains only the even numbers from the
# previous list, also using a list comprehension.

even_numbers_list: list = [num for num in numbers_list if num%2 == 0]
print(even_numbers_list)
print()

# 5.3 Exercise
# - Write a function that takes a list of numbers and returns a new
# list containing only the numbers that are divisible by 3.
# Use typed variables and return types.

def divisible_by_three(lista: list) -> list:
    """Function that takes a list of numbers and returns a list
    containing only the numbers that are divisible by 3.

    Args:
        lista (list): Must contain only numbers (int)

    Returns:
        list: list with numbers (int) divisible by 3
    """
    return [numero for numero in lista if numero%3 == 0]

print(divisible_by_three(numbers_list))