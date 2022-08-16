# reverse a string using recursion
def reverse_recursion(string):
    if len(string) == 0:
        return string
    else:
        return reverse_recursion(string[1:] + string[0])
# here we are adding the first element at the end each time we call the recursion thereby reversing the string we then return the string when len == 0

string = input('Enter your string: ')
reverse = reverse_recursion(string)
print('Reversed string is ', reverse)
