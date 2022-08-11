import random

print('GUESS THE THE GAME!')
computer = random.randint(1, 100)
num_attempts = 0
while True:

    try:
        user = int(input('Enter a number between 1 - 100: \n'))
        if computer == user:
            num_attempts += 1
            print(f' you guessed the correct number after {num_attempts} attempts!')
            break

        elif user < computer:
            print('number is too low.')
            num_attempts += 1
        else:
            print('number is too high.')
            num_attempts += 1
    except:
        print('choose a number between 1-100')
