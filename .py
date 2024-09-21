import random
from random import choices

choice = ["Rock", "Paper", "Scissors"]

#User inputs

user = input("Input Either Rock, Paper, or Scissors: ")

#comtuer chooses random string from list
import random
computer = random.choice(choice)

#The choices are printed in terminal
print(f"user entered:{user}")
print(f"computer entered:{computer}")

#if statement deciding who wins
if user == computer:
    print("Tie")
elif (user == "Rock" and computer == "Scissors") or (computer == "Paper" and user == "Scissors") or (user == "Paper" and computer == "Rock"):
    print("User wins :)")
elif (computer == "Rock" and user == "Scissors") or (user == "Paper" and computer == "Scissors") or (computer == "Paper" and user == "Rock"):
    print("You suck pal :(")

