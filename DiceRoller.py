import sys
import random

ans = True

while ans:
    question = input("You want to roll the die? y or n: ")

    answers = random.randint(1, 6)

    if question == 'n':
        sys(quit())


    elif answers == 1:
        print('You got 1!')

    elif answers == 2:
        print('You got 2!')

    elif answers == 3:
        print('You got 3!')

    elif answers == 4:
        print('You got 4!')

    elif answers == 5:
        print('You got 5!')

    elif answers == 6:
        print('You got 6!')

