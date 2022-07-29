sports = {'peter': 'football', 'john': 'golf', 'ken': 'running', 'dan': 'tennis', 'dil': 'swimming'}
print(sports)


def searching(sports, value):
    for key in sports:
        if sports[key] == value:
            return key, value

    return 'value not found'


print(searching(sports, 'high jump'))
print(searching(sports, 'golf'))
