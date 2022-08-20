def threesum(num):
    num.sort()
    res = []
    for i, a in enumerate(num):
        # to avoid duplicates e do this
        if i > 0 and a == num[i - 1]:
            continue
            # i here has an index of 1 this checks if the first and second num are the same
            # pointers
        l, r = i + 1, len(num) - 1
        while l < r:
            threesum = a + num[l] + num[r]
            # a = value of i
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([a, num[l], num[r]])
                # to be able to move our left pointer to avoid duplicates as our list is sorted
                l += 1
                while num[l] == num[l - 1] and l < r:
                    l += 1
    return res


num = [-1, 0, 1, 2, -1, -4]
print(threesum(num))
