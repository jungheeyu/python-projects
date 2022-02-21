#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

target_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt = 10 if difficulty == 'easy' else 5
guessed_number = 0
while guessed_number != target_number and attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number > target_number:
        print("Too high. \nGuess again.")
    elif guessed_number < target_number:
        print("Too low. \nGuess again.")
    else:
        print(f"You got it! The answer was {target_number}.")
        break
    attempt -= 1
if attempt == 0:
    print("You've run out of guesses, you lose.")


