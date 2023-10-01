# Lesson 10: Loops and Iteration

# 10.1 For Loops
# - Create a list of numbers from 1 to 5.
numbers_list: list = [num for num in range(1,6)]

# - Use a for loop to print each number in the list.
for number in numbers_list:
    print(number)
print()

# 10.2 While Loops
# - Write a while loop that counts from 1 to 3 and prints each number.
index = 1
while index <= 3:
    print(index)
    index +=1
print()

# 10.3 Exercise
# - Write a function that takes an integer n as input and prints
#   all even numbers from 1 to n.
#   Use typed variables and return types.

def print_even_numbers(num: int) -> None:
    """Print even numbers starting from 1 to the input number

    Args:
        num (int): The number that we are going to count to.
    """
    for numero in range(1,num+1):
        if not numero%2:
            print(numero)

print_even_numbers(8)