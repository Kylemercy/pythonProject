# searching for element in a tuple
newtuple = ('a', 'b', 'g', 't', 'r', 'h', 'k')
# using in operator
print('s' in newtuple)
print('a' in newtuple)


# this returns a boolean value
# using linear search
def searchtuple(value, newtuple):
    for i in newtuple:
        if i == value:
            return newtuple[i]
    return 'value not found'



print(searchtuple('o', newtuple))
