import random
user_action = input("Enter a choice (Rock, Paper, Scissors): ").capitalize().strip()
possible_actions = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_actions)

print(f"You chose {user_action}, computer chose {computer_action}")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It is a tie!")

elif user_action == "Rock":
    if computer_action == "Scissors":
        print("Rock smashes scissors. You win!")
    else:
        print("Paper covers Rock. You lose!")

elif user_action == "Paper":
    if computer_action == "Rock":
        print("Paper covers Rock. You win!")
    else: 
        print("Scissors cuts Paper. You lose!")

elif user_action == "Scissors":
    if computer_action == "Paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock smashes Scissors. You lose!")
