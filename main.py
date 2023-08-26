""" Number Guessing game

Task:
Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

The minimum number of guesses depends upon range.
"""

from random import randint
import math

A = int(input("Enter the first number of range: "))
B = int(input("Enter the last number of range: "))

guessed_num = randint(A, B)
tries = round(math.log(B - A + 1, 2))
print("\n\tYou've only ",
      tries,
      " chances to guess the integer!\n")

count = 0

while count < tries:
    count += 1
    user_num = int(input("Guess the number: "))

    if user_num > guessed_num:
        print("Try Again! You guessed too high")
    elif user_num < guessed_num:
        print("Try Again! You guessed too less")
    elif user_num == guessed_num:
        print(f"Congratulations you did it in {count} try")
        break

if count > tries: print("Better luck next time! Number is %d" % guessed_num)