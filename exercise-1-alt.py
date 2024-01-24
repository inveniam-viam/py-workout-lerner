# Exercise 1 solved with a Walrus
import random


def guessing_game() -> None:

    chosen_number: int = random.randint(0, 100)

    while s := int(input("Guess what number was chosen: ")):

        if s > chosen_number:

            print("Too high")
        elif s < chosen_number:

            print("Too low")

        elif s == chosen_number:

            print("Just right")
            break


if __name__ == "__main__":

    guessing_game()
