# using a hashmap
def two_sum(num, target):
    result = []
    # list of stored result
    hash_map = {}
    # dictionary difference values then index
    for i, n in enumerate(num):
        # loop for each element
        difference = target - n
        if difference in hash_map:
            result.append(i)
            # appends the two values
            result.append(hash_map[difference])
        else:
            hash_map[n] = i
            # adds the difference value and index to the dictionary after visiting each element
    return result


num = [1, 2, 3, 4, 5, ]
print(two_sum(num, 9))
