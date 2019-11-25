#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program guesses the number

import random


def main():
    # random number
    number = random.randint(0, 9)

    # input
    guess = int(input("Guess the number between 0 and 9: "))

    # process
    if guess == number:
        # output
        print()
        print("Correct!")

    # process
    else:
        # output
        print()
        print("Sorry. nice try!")
        print("My number was", number)


if __name__ == "__main__":
    main()
