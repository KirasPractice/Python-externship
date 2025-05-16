
# Task 1 - Writing Functions

def greet_user(name):
    print(f"Hello {name}")


# def add_numbers(num1, num2):
#     return num1 + num2

# greet_user("ally")
# total = add_numbers(4,3)
# print(f"The sum of 4 and 3 is {total}.") 


# Create a function describe_pet that accepts two parameters:

# pet_name (string)
# animal_type (string, default value is "dog").
# The function should print a description of the pet.

def describe_pet(pet_name ="lala",animal_type ='dog'):
    print(f"I have a {animal_type} named {pet_name} ")
describe_pet()
# Example Output:


# Task 3 - Functions with Variable Arguments
# Write a function make_sandwich that accepts a variable number of arguments for sandwich ingredients and prints them as a list.
# def make_sandwich(*ingredients):
#     print("Making a sandwich with the following ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# make_sandwich("Lettuce", "Tomato", "Cheese")
# # Example Output:


# Task 4 - Understanding Recursion
# Write a recursive function factorial to calculate the factorial of a number.
# Then, write another recursive function fibonacci to calculate the nth number in the Fibonacci sequence.
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# def fibonacci(n):
#     if n <= 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(f"Factorial of 5 is {factorial(5)}.")
