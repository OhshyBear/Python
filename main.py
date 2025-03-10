from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = int(input('guess a number from 1 to 10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('You are a Genius! You WIN!')
                break
        else:
            print('That is not the magic number, Try again!')
            continue
    except ValueError:
        print('Enter a number or you will never win')
        continue
