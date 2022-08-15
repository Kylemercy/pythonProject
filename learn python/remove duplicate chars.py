def remove_duplicate(string):
    temp = ''
    for i in string:
        if i in temp:
            continue
        else:
            temp += i
    return temp


string = input('ENTER YOUR STRING: ')
result = remove_duplicate(string)
print('your string without duplicate: ',result)
