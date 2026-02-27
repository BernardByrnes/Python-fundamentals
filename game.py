import random
import time

def print_slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def number_game():
    print_slow("Welcome to the Number Guessing Game!")
    print_slow("I'm thinking of a number between 1 and 50.")
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < 1 or guess > 50:
                print("Stay within 1 and 50!")
                continue
            if guess == secret_number:
                print_slow(f"Correct! You guessed it in {attempts} tries.")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

    