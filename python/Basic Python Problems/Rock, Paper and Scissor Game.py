import random

def play():
    # Taking input from user
    user_choice = input("Start Playing, Choose one 'r for rock, 'p' for paper and 's' for scissor\n")

    computer_choice = random.choice(['r', 'p', 's'])

    if computer_choice == 'r':
        computer_var = "rock"
    elif computer_choice == 'p':
        computer_var = "paper"
    else:
        computer_var = "scissor"

    if user_choice == computer_choice:
        print(f"It's a tie because computer choice is {computer_var}")

    if win_scenarios(user_choice, computer_choice):
        print(f"You won ! because computer choice is {computer_var}")

    if win_scenarios(computer_choice, user_choice):
        print(f"You lost ! because computer choice is {computer_var}")

    Continue = input("You wanna play again ?\n")

    if Continue == 'Y' or Continue == 'y':
        play()
    else:
        print("Bye, have a nice day !")

def win_scenarios(user_choice, computer_choice):
    # winning scenarios are r > s, p > r, s > p
    if (user_choice == 'r'and computer_choice == 's')or(user_choice == 'p' and computer_choice == 'r')\
        or (user_choice == 's' and computer_choice == 'p'):
        return True

play()