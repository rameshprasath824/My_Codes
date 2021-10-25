import random

number = random.randint(0,3)
range = 3


if range >= number:
 guess = 0
 chances = 0
 x = 0
 while guess != number and chances != 3:
     print(f'chances = {chances}')
     guess = int(input(f"Enter your first guess between 1 and {range}: "))
     if guess < number:
       print('Oops,you missed.number is too low')
       chances+=1
     if guess > number:
       print('Oops,you missed. the number is too high')
       chances+=1
     if guess == number:
       print('Hurreeey!! your guess is correct')
       chances+=1
       x+=1

 if x == 0:
  print("you missed all three chances, sorry. better luck next time ")
