import random

number_to_guess = random.randint(1,100)
user_attempts = 0

user_guess = int(input("Guess a number (1-100): "))
user_attempts += 1

while user_guess != number_to_guess and user_attempts < 10:
    if user_guess > number_to_guess:
        print(f"{user_guess} Too high! Try again!")
        
    elif user_guess < number_to_guess:
        print(f"{user_guess} Too low! Try again!")
     
    user_guess = int(input("Guess again: "))
    user_attempts += 1

if user_guess == number_to_guess:   
    print(f"{user_guess} Congradulations! You guessedd it in {user_attempts} tries")
else:
    print(f"You ran out of tries, the number was {number_to_guess}")