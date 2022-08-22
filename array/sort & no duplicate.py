# remove duplicate from sorted array
def sort_array(num):
    count = 1
    for i in range(1, len(num)):
        if num[i] != num[i - 1]:
            # updating our array
            num[count] = num[i]
            count += 1

    return count


num = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(sort_array(num))
