# Lesson 8: Conditional Statements and Boolean Logic

# 8.1 Conditional Statements
# - Create a variable `number_x` and set it to 5.
number_x: int = 5

# - Write an if statement to check if `number_x` is greater than 10.
#   If it is, print "Number_x is greater than 10." Otherwise, 
#   print "Number_x is not greater than 10."
if number_x > 10:
    print(f"{number_x} is greater than 10.")
else:
    print(f"{number_x} is not greater than 10.")

print()

# 8.2 Boolean Logic
# - Create two variables, `is_a_true` and `is_b_false`, and 
#   set them to True and False, respectively.
is_a_true: bool = True
is_a_false: bool = False

# - Write an if statement to check if both `is_a_true` and
#   `is_b_false` are True.
#   If they are, print "Both `is_a_true` and `is_b_false` are True."
#   Otherwise, print "At least one of them is False."
if is_a_true and is_a_false:
    print("Both 'is_a_true' and 'is_b_false' are True.")
else:
    print("At least one of them is False.")

print()


# 8.3 Exercise
# - Write a function that takes an integer as input and returns True 
#   if the integer is even, and False if it's odd.
#   Use typed variables and return types.

def is_even(number: int) -> bool:
    """Check if the provided number(int) is even

    Args:
        number (int): The number to check if it is even

    Returns:
        bool: True or False depending on the number
    """
    return not number%2

print(is_even(2))
print(is_even(3))
