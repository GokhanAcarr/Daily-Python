import random


users_choice = input("You can choose Rock, Paper or Scissors!")
computers_choice = random.choice(["Rock", "Paper", "Scissors"])

print(computers_choice)

if users_choice == computers_choice:
    print("It's a tie!")
if users_choice == "Rock" and computers_choice == "Paper":
    print("You lose!")
if users_choice == "Rock" and computers_choice == "Scissors":
    print("You Win!")
if users_choice == "Paper" and computers_choice == "Rock":
    print("You Win!")
if users_choice == "Paper" and computers_choice == "Scissors":
    print("You lose!")
if users_choice == "Scissors" and computers_choice == "Rock":
    print("You lose!")
if users_choice == "Scissors" and computers_choice == "Paper":
    print("You Win!")