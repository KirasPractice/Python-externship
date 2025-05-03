import random

number_to_guess = random.randint(1,100)

user_guess = int(input("Guess a number (1-100): "))

while user_guess != number_to_guess:
    if user_guess > number_to_guess:
        print(f"{user_guess} Too high! Try again!")
        
    elif user_guess < number_to_guess:
        print(f"{user_guess} Too low! Try again!")
     
    user_guess = int(input("Guess again: "))
print(f"{user_guess} Congradulations! You guessedd it!")