def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_positive_integer(prompt):
    while True:
        value = input(prompt)
        if not value.isdigit() or int(value) < 1:
            print("  ✗ Please enter a positive whole number.")
        else:
            return int(value)

def main_menu():
    while True:
        print("\nWelcome to the Recursion Demo! Choose an option:")
        print("  1. Calculate Factorial")
        print("  2. Find Fibonacci Number")
        print("  3. Exit")
        choice = input("> ").strip()

        if choice == "1":
            n = get_positive_integer("Enter a number for factorial: ")
            result = factorial(n)
            print(f"✓ {n}! = {result}")
        elif choice == "2":
            n = get_positive_integer("Enter Fibonacci position: ")
            result = fibonacci(n)
            print(f"✓ Fibonacci({n}) = {result}")
        elif choice == "3":
            print("Goodbye! Thanks for exploring recursion.")
            break
        else:
            print("  ✗ Invalid choice — please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
