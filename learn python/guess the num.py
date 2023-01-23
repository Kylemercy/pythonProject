print('WELCOME TO NUMBER GUESSING GAME')
import random

comp = random.randint(1, 100)
print("i'm thinking of a number between 1-100.")
user = input('Choose difficulty.type easy,or hard : ')


def guess():
    easy_num_guess = 10
    Hard_num_guess = 5
    
    while Hard_num_guess > 0:
        if user == 'hard':
            print(f'You have {Hard_num_guess} attempts to make a guess')
            make_guess = int(input('Make a Guess: '))
            if make_guess == comp:
                print(f'Correct right guess. The answer was {comp}.')
                print('YOU WIN ')

                break
            elif make_guess > comp:
                print('Too high')
            else:
                print('Too low')
        Hard_num_guess -= 1


    while easy_num_guess > 0:
        if user == 'easy':
            print(f'You have {easy_num_guess} attempts to make a guess')
            make_guess = int(input('Make a Guess: '))
            if make_guess == comp:
                print(f'Correct! right guess. The answer was {comp}.')
                print('YOU WIN ')

                break

            elif make_guess > comp:
                print('Too high')
            else:
                print('Too low')
        easy_num_guess -= 1


guess()
# alternative

''' EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess2, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess2 > answer:
        print("Too high.")
        return turns - 1
    elif guess2 < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()'''
