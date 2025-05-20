# ask 1 - Understanding Python Exceptions


number = input("Enter a number: ")
try:
    number = float(number)
    print("100 divided by", number, "is", 100 / number)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")
print("Done.")


# 
# Task 2 - Types of Exceptions
my_list = [1, 2, 3]
my_dict = {'a': 1}

try:
    print(my_list[5])
except IndexError:
    print("IndexError occurred! List index out of range.")

try:
    print(my_dict['b'])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    print('hello' + 5)
except TypeError:
    print("TypeError occurred! Unsupported operand types for +.")

# Task 3 - Using try...except...else...finally
x = input("Enter the first number: ")
y = input("Enter the second number: ")
try:
    x = float(x)
    y = float(y)
    result = x / y
except Exception:
    print("Error: invalid input or division by zero.")
else:
    print("The result is", result)
finally:
    print("This block always executes.")