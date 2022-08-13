def get_second_largest(my_num):
    largest = my_num[0]
    second_largest = my_num[0]
    for i in range(1, len(my_num)):
        if my_num[i] > largest:
            second_largest = largest
            largest = my_num[i]
        elif my_num[i] > second_largest:
            second_largest = my_num[i]
    return second_largest


my_num = [3, 33, 43, 45, 56, 66,76,88]
print(get_second_largest(my_num))
