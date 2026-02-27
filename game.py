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

    