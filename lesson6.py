# Lesson 6: Strings and String Manipulation

# 6.1 String Basics
# - Create a string variable containing your full name.

full_name = "Pepito Perez"

# - Print out the length of your name (number of characters).

print(len(full_name))

# - Print out your name in uppercase.
print(full_name.upper())

# 6.2 String Slicing
# - Extract your first name from your full name using string slicing.

print(full_name[:6])

# - Print out your last name using string slicing.
print(full_name[7:])

# - Print out your name in reverse.
print(full_name[::-1])
print()

# 6.3 Exercise
# - Write a function that takes a string as input and returns the same 
# string with all spaces removed.
# Use typed variables and return types.

def remove_spaces(string: str) -> str:
    """Remove the caracter space from a given string.

    Args:
        string (str): The input string from where spaces will be removed.

    Returns:
        str: A new string with spaces removed.
    """
    no_spaces: str = ""
    for letter in string:
        if letter != " ":
            no_spaces += letter
    return no_spaces

# Example usage:
result = remove_spaces("Hello World")
print(result)
