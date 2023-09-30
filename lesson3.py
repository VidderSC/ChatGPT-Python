# Lesson 3: Control Flow and Loops

# 3.1 If Statements
# Write an if statement to check if a variable x is greater than 10.
# If it is, print “x is greater than 10.”
x: int = 12

if x > 10:
    print("X is greater than 10")

# 3.2 For Loops
# Create a list of numbers from 1 to 5.
# Use a for loop to print each number in the list.

numbers: list = range(1, 6)
for number in numbers:
    print(number)

# 3.3 While Loops
# Write a while loop that counts from 1 to 3 and prints each number.

x = 1
while x < 4:
    print(x)
    x += 1

# 3.4 Exercise
# Create a function that takes an integer n as input and prints all
# even numbers from 1 to n. Use typed variables and return types.

def print_even_numbers(n: int) -> None:
    """Will print only the even numbers on the range 1 to n"""
    for num in range(1,n):
        if num%2 == 0:
            print (num)

print_even_numbers(10)
