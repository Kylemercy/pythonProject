import random

print('COW AND BULL GUESSING GAME')
cow = 0
bull = 0
secret_number = str(random.randint(1000, 9999))
print('guess the number it contains 4 digits!')
chances = 7


def get_cow_bull(number, user_guess):
    bulls_cows = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            bulls_cows[0] += 1
        elif user_guess[i] in number:
            bulls_cows[1] += 1
    return bulls_cows


while chances > 0:
    player = input('enter your 4 digit number: ')
    if player == secret_number:
        print('You guessed it right!')
        print('You Won')
        break
    else:
        bull_cows = get_cow_bull(secret_number, player)
        print('Bulls', bull_cows[0])
        print('Cows', bull_cows[1])
        chances -= 1
        if chances < 1:
            print('YOU LOST!')
            print('the correct number is', secret_number)
            break
