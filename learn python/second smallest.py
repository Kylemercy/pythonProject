def get_second_smallest(my_num):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(0, len(my_num)):
        if my_num[i] <= smallest:
            second_smallest = smallest
            smallest = my_num[i]
        elif my_num[i] < second_smallest:
            second_smallest = my_num[i]
    return second_smallest


my_num = [3,22, 33, 43, 45, 56, 66, 76, 88]
print(get_second_smallest(my_num))
