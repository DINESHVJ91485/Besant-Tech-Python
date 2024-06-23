import random

#Prining Title
print("Rock, Paper, Scissors Game!!!")

#Getting User's Input
user=input("Enter 'Rock', 'Paper' or 'Scissor': ")
print("User's Choice",user)

#Getting Computer's Input
computer=random.choice(['Rock', 'Paper', 'Scissor'])
print("Computer's Choice",computer)

if user == computer:
    print("It's a tie!")
elif user== "Rock":
    if computer == "Scissor":
        print("User Won!", user, "Smashes", computer)
    else:
        print("Computer Won!", computer, "Covers", user)
elif user == "Scissor":
    if computer == "Paper":
        print("User Won!", user, "Cuts", computer)
    else:
        print("Computer Won!", computer, "Smashes", user)
elif user == "Paper":
    if computer == "Rock":
        print("User Won!", user, "Covers", computer)
    else:
        print("Computer Won!", computer, "Cut", user)
