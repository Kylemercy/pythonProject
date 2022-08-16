def reverse_string(txt):
    verse = ' '
    for char in txt:
        verse = char + verse
        # the trick is here we add each char after the loop at the back of each added letter that is char + verse
    return verse


txt = input('Entre your string: ')
result = reverse_string(txt)
print('Your reversed string is: ', result)
