#     project    __ROCK - PAPER - SCISSORS__


import random



print("____HELLO____ \n you are playng ROCK - PAPER - SCISSORS \n good luck")
retry = True
win = 0
lose = 0
tie = 0

while retry == True:
    choice_of_user = input("Make your choice --  (r)ock  or  (p)aper  or  (s)cissors: ")


    random_number = random.randint(1,3)
    computer_choice = ""

    if random_number == 1:
        computer_choice = "ROCK"
    elif random_number == 2:
        computer_choice = "PAPER"
    elif random_number == 3:
        computer_choice = "SCISSORS"


    if choice_of_user == "r":
        print(f"ROCK - versus - {computer_choice}")
    elif choice_of_user == "p":
        print(f"PAPER - versus - {computer_choice}")
    elif choice_of_user == "s":
        print(f"SCISSORS - versus - {computer_choice}")



    if choice_of_user == "r" and computer_choice == "ROCK":
        print("tie")
        tie += 1
    elif choice_of_user == "p" and computer_choice == "PAPER":
        print("tie")
        tie += 1
    elif choice_of_user == "s" and computer_choice == "SCISSORS":
        print("tie")
        tie += 1
    elif choice_of_user == "r" and computer_choice == "PAPER":
        print("you lose")
        lose += 1
    elif choice_of_user == "r" and computer_choice == "SCISSORS":
        print("you win")
        win += 1
    elif choice_of_user == "p" and computer_choice == "ROCK":
        print("you win")
        win += 1
    elif choice_of_user == "p" and computer_choice == "SCISSORS":
        print("you lose")
        lose += 1
    elif choice_of_user == "s" and computer_choice == "ROCK":
        print("you lose")
        lose += 1
    elif choice_of_user == "s" and computer_choice == "PAPER":
        print("you win")
        win += 1
    else:
        print("something went wrong")

    print(f"win = {win} : lose = {lose} : tie = {tie}")



    retry = input("Wish you re-try -- (y/n): ")
    if retry == "y":
        retry = True
    else:
        False



print(f"final result \n win = {win} : lose = {lose} : tie = {tie}")


if win > lose:
    print("You are very lucky")
elif lose > win:
    print("If you are not lucky today, do not give up")
elif win == lose:
    print("Draw")

