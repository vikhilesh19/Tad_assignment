#Rock Paper Scissors  

import random
choice = ["rock", "paper", "scissors"]
while 1:
    user = input("Choose rock, paper, or scissors or exit: ").lower()
    if user == "exit":
        break
    elif user not in choice :
        print("Enter a vaild choice")
        continue
    computer = random.choice(choice)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")