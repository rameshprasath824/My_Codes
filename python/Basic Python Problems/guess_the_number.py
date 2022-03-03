# importing random module to make interpreter to choose once random  number
import random

# taking range as input
range = int(input('enter upto which range you wanna play: '))

# calling the below method to make intrepreter to choose one random number on its own
number = random.randint(0, range)

# restricting users from guessing numbers beyond the range
if range >= number:
    guess = 0
    chances = 0
    x = 0

    # looping until guessing correct number and restricting user for 3 chances only
    while guess != number and chances != 3:
        print(f'chances = {chances}')
        guess = int(input(f"Enter your first guess between 1 and {range}: "))
        if guess < number:
            print('Oops,you missed.number is too low')
            chances += 1
        if guess > number:
            print('Oops,you missed. the number is too high')
            chances += 1
        if guess == number:
            print('Hurreeey!! your guess is correct')
            chances += 1
            x += 1

    # print below statement only if user missed to guess the correct number
    if x == 0:
        print("you missed all three chances, sorry. better luck next time ")
