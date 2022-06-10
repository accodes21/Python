import random
your_score = 0
comp_score = 0
while True:

    choices = ["rock","paper","scissors"]
    comp_choice = random.choice(choices)

    print("Welcome to Rock Paper Scissors Game!")
    user_choice = input("Enter your Choice \n(rock,paper,scissors): ")

    # your_score = 0
    # comp_score = 0

    print("Your Choice:"+user_choice+" \nComputer Choice:"+comp_choice)


    if user_choice == comp_choice:
        print("**Its a tie**")

    if user_choice == "rock":   
        if comp_choice == "scissors":
            print("**Rock smashes scissors! You win!**")
            your_score+=1
        else:
            print("**Paper covers rock! You lose.**")
            comp_score+=1
    
    elif user_choice =="paper":
        if comp_choice == "rock":
            print("**Paper covers rock! You win!**")
            your_score+=1
        else:
            print("**Scissors cuts paper! You lose.**")
            comp_score+=1

    elif user_choice =="scissors":
        if comp_choice == "paper":
            print("**Scissors cuts paper! You win!**")
            your_score+=1
        else:
            print("**Rock smashes scissors! You lose.**")
            comp_score+=1
    print("Your Score: "+str(your_score)+" Comp Score: "+str(comp_score))
    x = input("Do you want to play again? (y/n): ")
    if x!= "y":
        print("Thank You!")
        break