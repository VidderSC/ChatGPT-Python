# Lesson 9: Dictionaries and Dictionary Manipulation

# 9.1 Dictionary Basics
# Create a dictionary to represent a person, including their 
# name, age, and city.
person_dictionary: dict = {
    "name":"Pepito",
    "age":43,
    "city":"World",
    }

# Print out the person's name.
print(person_dictionary["name"])

# 9.2 Dictionary Manipulation
# Add a new key-value pair to the person dictionary to
# represent their occupation.
person_dictionary["occupation"] = "Future Python developer"

# Update the age of the person in the dictionary.
person_dictionary["age"] = 21

# Print out the updated dictionary.
print(person_dictionary)

# 9.3 Exercise
# Write a function that takes a dictionary representing a person
# as input and returns their age.

def what_is_the_age(person: dict) -> int:
    """Takes a dictionary of a person and returns their age

    Args:
        person (dict): Dictionary from where we are returning the age

    Returns:
        int: The age of the person
    """
    if "age" in person:
        return person["age"]
    return 0

print(what_is_the_age(person_dictionary))