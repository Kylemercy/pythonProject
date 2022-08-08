import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_image = [rock,paper,scissors]

user = int(input(' choose either 0 for rock,1 for paper, or 2 for scissors. \n'))
if user < 0 or user >= 3:
    print('invalid index you loose')
else:
    print(game_image[user])
computer = random.randint(0, 2)
print('computer chose:')
print(game_image[computer])
if computer == 2 and user == 2:
    print('its a draw!')
elif computer == 1 and user == 1:
    print('its a draw!')
elif computer == 0 and user == 0:
    print('its a draw!')
elif computer == 2 and user == 1:
    print('computer wins !')
elif computer == 1 and user == 2:
    print('You win !')
elif computer == 2 and user == 0:
    print('you win!')
elif computer == 0 and user == 2:
    print('computer wins!')
elif computer == 1 and user == 0:
    print('computer wins!')
elif computer == 0 and user == 1:
    print('you win!')
