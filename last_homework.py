import random

while True:
    user_choice = input("Your choice (rock paper scissors lizard spock)? \n")
    computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    if user_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
        print(f"Player:{user_choice} \nComputer:{computer_choice}")
    else:
        print(f"Invalid input'{user_choice}'")
        continue
    if user_choice == computer_choice:
        print("no winner")
    elif user_choice == "rock":
        if computer_choice != 'lizard' and 'scissors':
            print("Computer WIN!")
        else:
            print("Player WIN!")
    elif user_choice == "paper":
        if computer_choice == "rock" and 'spock':
            print("Player WIN!")
        else:
            print("Computer WIN!")
    elif user_choice == "scissors":
        if computer_choice == "paper" and 'lizard':
            print("Player WIN!")
        else:
            print("Computer WIN!")
    elif user_choice == "lizard":
        if computer_choice == "paper" and "spock":
            print("Player WIN!")
        else:
            print("Computer WIN!")
    elif user_choice == "spock":
        if computer_choice == "scissors" and "rock":
            print("Player WIN!")
        else:
            print("Computer WIN!")

    repeat = input('Repeat(Y/N)?')
    if repeat == 'Y':
        continue
    elif repeat == "N":
        break
    else:
        print(f'Invalid choice: {repeat} \n Repeat(Y/N)?')
        continue
