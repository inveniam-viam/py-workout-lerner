# Exercise 1 
# Number Guessing Game 

import random

def guessing_game():

    chosen_number: int = random.randint(0, 100)

    while True:

        user_guess:int = int(input("Guess what number has been chosen: "))

        if user_guess == chosen_number:

            print("Just right")
            break
        
        elif user_guess > chosen_number:

            print("Too high")
        
        elif user_guess < chosen_number:

            print("Too low")
        
        else:

            print("Invalid input")


if __name__ == "__main__":

    guessing_game()



