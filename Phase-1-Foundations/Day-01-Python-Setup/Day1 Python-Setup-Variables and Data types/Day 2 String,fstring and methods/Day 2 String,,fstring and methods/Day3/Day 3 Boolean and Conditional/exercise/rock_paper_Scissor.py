"""
Exercise 3 — Rock, Paper, Scissors vs the Computer (STUDENT STUB).

Rules: rock beats scissors, scissors beats paper, paper beats rock.

"""

import random

OPTIONS = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    computer = random.choice(OPTIONS)

    user = input("Enter from the option = [rock, paper, scissors]: ")
    user = user.lower()

    if user == "rock" and computer == "scissors":
        print("User wins")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("User wins")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("User wins")
        user_score += 1

    elif user == computer:
        print("Match Draw")

    else:
        print("Computer wins")
        computer_score += 1

    print(f"User selection was {user} and Computer selection was {computer}")
    print("User:", user_score, "Computer:", computer_score)

    if input("Play again? (yes/no): ").lower() == "no":
        break

print("Final Score")
print("User:", user_score)
print("Computer:", computer_score)