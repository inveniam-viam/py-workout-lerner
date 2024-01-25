# Exercise 1 - Guessing Numbers


import random   # to generate the random number between 0 to 100


def guessing_game() -> None:

    answer = random.randint(0, 100)
    attempts = 0

    while guess := input("Enter a number between 0 and 100: "):

        attempts += 1

        if int(guess) > answer:

            print("Too high")
        
        elif int(guess) < answer:

            print("Too low")
        
        else:

            print("Just about right")
            break

        if attempts == 3:

            print("You're out of guesses, goodbye!")
            break

if __name__ == "__main__":

    guessing_game()
