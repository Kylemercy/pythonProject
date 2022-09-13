# HANGMAN GAME
import random
from hangman_wordlist import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

lives = len(stages) - 1
game_is_finished = False
choice = random.choice(word_list)
word_length = len(choice)
print(choice)
display = []
for i in range(word_length):
    display += '_'
print(display)

while not game_is_finished:
    guess = input('GUESS A LETTER: \n').lower()
    if guess in display:
        print(f'You have already guessed {guess}.')

    for i in range(len(choice)):
        letter = choice[i]
        if letter == guess:
            display[i] = letter
    print(f"{' '.join(display)}")
    if guess not in choice:
        print(f'you guessed {guess},that is not in the word.you lose a live!  ')
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print('YOU LOSE!\n GAME OVER')
    if not'_' in display:
        end_game = True
        print('YOU WIN!')
    print(stages[lives])
