# reversing a string using stack
def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    rev = ''
    while len(stack) > 0:
        
        last = stack.pop()
        rev = rev + last
    return rev


string = input('Enter your string: ')
reverse = reverse_string(string)
print('Reversed string is ', reverse)
