x = 100000
y = 7000
t = x + y
print(f'{t:,}')
# how to add separators to our result
# enumerate returns the index and value of list we are looping over
names = ['joe', 'mia', 'mark', 'sandy', 'tim']
for index, name in enumerate(names):
    print(index, name)
# or
for index, name in enumerate(names, start=2):
    print(index, name)
# looping over 2 list
# we use zip as it allows us to loop over 2 or more list lists at ones
names1 = ['wilson parker', 'Clark kent', 'Wade wilson', 'Bruce wayne']
heroes = ['spider man', 'superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero in zip(names1, heroes):
    print(f'{name} is actually {hero}')
print('\n')
for name, hero, universe in zip(names1, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
print('\n')

for value in zip(names1, heroes, universes):
    print(value)
    # unpacking
a, b = (1, 2)
print(a)
print(b)
a, b, *c = (1, 2, 3, 4, 5, 6)
print(a)
print(b)
print(c)
# underscore is used to name the value we want to ignore to prevent error
# getpass function
from getpass import getpass

username = input('Name:')
password = getpass('password:')
print('logging in.....')