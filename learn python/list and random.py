"""choice(L) picks a random item from L
sample(L,n) picks a group of n random items from L
shuffle(L) Shuffles the items of L"""
# We can use choice to pick a name from a list of names.
from random import choice

names = ['Joe', 'Bob', 'Sue', 'Sally']
current_player = choice(names)
print(current_player)
'''The sample function is similar to choice. Whereas choice picks one item from a
list, sample can be used to pick several.'''
from random import sample

names = ['Joe', 'Bob', 'Sue', 'Sally']
team = sample(names, 2)
print(team)

'''The choice function also works with strings, picking a random character from a
string. Here is an example that uses choice to fill the screen with a bunch of 
random characters.'''
from random import choice

s = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
for i in range(10):
    print(choice(s), end='')
""" Here is a nice use of shuffle to pick a random ordering of players in a game."""
from random import shuffle

players = ['Joe', 'Bob', 'Sue', 'Sally']
shuffle(players)
for p in players:
    print(p, 'it is your turn.')
# code to play the game goes here...
"""Example 5 Here we use shuffle divide a group of people into teams of two.
 Assume we are
given a list called names."""
names = ['Joe', 'Bob', 'Sue', 'Sally', 'David', 'Peter']
shuffle(names)
teams = []
for i in range(0, len(names), 2):
    teams.append([names[i], names[i + 1]])
print(teams)
