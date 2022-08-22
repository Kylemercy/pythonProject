# remove element
def remove_element(num: list[int], value):
    count = 1
    for i in range(1, len(num)):
        if num[i] != value:
            # updating our array
            num[count] = num[i]
            count += 1

    return count


num = [0, 1, 2, 2, 3, 4, 6]

print(remove_element(num, 2))
