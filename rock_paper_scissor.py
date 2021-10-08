import random

print("You will get 5 chances")
score_user = 0
score_comp = 0
for i in range(1,6):
    print("Attempt",i)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print("Same Choice.. No Points for this")
    elif user_action == "rock":
        if computer_action == "scissors":
            score_user += 1
        else:
            score_comp += 1
    elif user_action == "paper":
        if computer_action == "rock":
            score_user += 1
        else:
            score_comp += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            score_user += 1
        else:
            score_comp += 1

print("Your Score", score_user)
print("Computer Score", score_comp)
if score_comp > score_user:
    print("You Lost")
elif score_comp < score_user:
    print("You Won")
else:
    print("Its a Tie")