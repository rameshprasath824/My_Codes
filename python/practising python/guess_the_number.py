number = 4
range = 15


if range >= number:
     guess = 0
     chances = 1
   while guess != number:
     if 3 != chances and guess != number:
        guess = int(input(f"Enter your first guess between 1 and {range}: "))
        if guess < number:
            print('Oops,you missed.number is too low')
            chances+=1
        if guess > number:
            print('Oops,you missed. the number is too high')
            chances+=1
        if guess == number:
            print('Hurreeey!! your guess is correct')
