import random

number_to_guess = random.randint(1,100)

user_guess = int(input("Guess a number (1-100): "))

while user_guess != number_to_guess:
    if user_guess > number_to_guess:
        print("Too high! Try again!")
        break;
    elif user_guess < number_to_guess:
        print("Too low! Try again!")
    else:
        print("Congraualtions! You guessed it!")
print(user_guess)