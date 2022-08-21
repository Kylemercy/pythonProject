# foursome sum of 4 unique num that sum to the target
def foursum(num, target):
    # sort the array
    num.sort()
    quad = []
    if num is None or len(num) < 4:
        return quad
    n = len(num)
    for i in range(0, n - 3):
        # this so because we have three pointers here
        # checking for duplicates
        if i > 0 and num[i] == num[i - 1]:
            continue
        # reducing to 3 sum
        for j in range(i + 1, n - 2):
            # check for duplicates to skip
            if j != i + 1 and num[j] == num[j - 1]:
                continue
                # left and right pointers
            l, r = j + 1, n - 1
            while l < r:
                cur_sum = num[i] + num[j] + num[l] + num[r]
                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    quad.append([num[i], num[j], num[l], num[r]])
                    l += 1
                    r -= 1
                    while l < r and num[l] == num[l + 1]:
                        l += 1
                    while l < r and num[r] == num[r + 1]:
                        r -= 1
    return quad


num = [1, 0, -1, 0, -2, 2]
print(foursum(num, 2))
