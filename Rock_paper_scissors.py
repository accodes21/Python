import random

choices = ["rock","paper","scissors"]
comp_choice = random.choice(choices)

print("Welcome to Rock Paper Scissors Game!")
user_choice = input("Enter your Choice \n(rock,paper,scissors): ")

print("Your Choice:"+user_choice+" \nComputer Choice:"+comp_choice)


if user_choice == comp_choice:
    print("Its a tie")
if user_choice == "rock":
    if comp_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
    
elif user_choice =="paper":
        if comp_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

elif user_choice =="scissors":
    if comp_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        