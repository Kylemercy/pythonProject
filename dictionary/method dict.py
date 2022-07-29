# clear method clears all element in dict
sports = {'peter': 'football', 'john': 'golf', 'ken': 'running', 'dan': 'tennis', 'dil': 'swimming'}
print(sports)
sports.clear()
print(sports)
sports = {'peter': 'football', 'john': 'golf', 'ken': 'running', 'dan': 'tennis', 'dil': 'swimming'}
print(sports)
# copy method
sports.copy()  # creates a copy of the dict
print(sports)
# from keys creates a new dict
food = {}.fromkeys(['breakfast', 'lunch', 'dinner'])
print(food)
food = {}.fromkeys(['breakfast', 'lunch', 'dinner'], 'rice')
print(food)
# get method returns value for specified key
print(sports.get('peter'))
print(sports.get('drake', 'key not in dictionary'))
# items method
# returns a list of items in tuple pairs
print(sports.items())
# keys returns a list of key
print(sports.keys())
# values returns a list of value
print(sports.values())
# popitem
print(sports.items())
# setdefault set a new value for a key
print(sports.setdefault('john', 'drake'))
print(sports.setdefault('drake', 'marathon'))
print(sports)
# this adds this new element to the dict as this key doesn't exit in the dict
# update method update a key value if you don't exit in the dict
fruit = {1: 'mango', 2: 'orange', 3: 'pear'}
sports.update(fruit)
print(sports)
