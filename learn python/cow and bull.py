import random
print('COW AND BULL GUESSING GAME')
cow = 0
bull = 0
guess = str(random.randint(10,100))
print('guess the number it contains 2 digits!')
chances = 7
while chances > 0:
    player = input('enter your 2 digit number: ')
    if guess == player:
        print('You guessed it right!')
        print('You Won')
        break
    else:
        if guess[1] == player[1]:
            bull += 1
        if guess[0] == player[0]:
            bull += 1
        if guess[0] ==  player[1]:
            cow += 1
        if guess[1]== player[0]:
            cow += 1
        print('Bulls: ',bull)
        print('Cows: ',cow)
        chances -= 1
        if chances < 1:
            print('YOU LOST!')
            print('the correct number is',guess)
            break

