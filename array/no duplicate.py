my_list = [5, 4, 2, 5, 6, 7, 8, 9, 11, 13, 14, 15]


def unique(my_list):
    empty_list = []
    for i in my_list:
        if i in empty_list:
            print(i)
            return False
        else:
            empty_list.append(i)
    return True


print(unique(my_list))
