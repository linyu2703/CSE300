import random

options = ["rock", "paper", "scissor"]

user_input = input("Choose rock, paper, or scissor: ")
computer_input = random.choice(options)

print("You chose: ", user_input)
print("Computer chose: ", computer_input)

if user_input == computer_input:
    print("Tie")
elif user_input == "rock" and computer_input == "scissor":
    print("You win")
elif user_input == "paper" and computer_input == "rock":
    print("You win")
elif user_input == "scissor" and computer_input == "paper":
    print("You win")
else:
    print("Computer wins")
