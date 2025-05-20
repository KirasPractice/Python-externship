# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Invalid input! Please enter a valid number.")

# print("Welcome to the Error-Free Calculator!")
# while True:
#     print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
#     choice = input("> ")
#     if choice == "5":
#         print("Goodbye!")
#         break
#     if choice not in ("1", "2", "3", "4"):
#         print("Invalid choice! Please select 1-5.")
#         continue

#     num1 = get_number("Enter the first number: ")
#     num2 = get_number("Enter the second number: ")

#     try:
#         if choice == "1":
#             result = num1 + num2
#         elif choice == "2":
#             result = num1 - num2
#         elif choice == "3":
#             result = num1 * num2
#         else:
#             result = num1 / num2
#     except ZeroDivisionError:
#         print("Oops! Division by zero is not allowed.")
#     else:
#         ops = {"1": "+", "2": "-", "3": "*", "4": "/"}
#         print(f"{num1} {ops[choice]} {num2} = {result}")
#     finally:
#         print("Operation complete.")
