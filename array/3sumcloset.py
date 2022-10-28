# sum of closet number close to target
def threesum(num, target):
    num.sort()
    n = len(num)
    # closet value
    closet = num[0] + num[1] + num[2]

    for i in range(0, n - 2):
        # creating your pointer
        # we use n -2 cause of our 2 pointers l,r were l starts from were n stops and r is always the last value
        l, r = i + 1, n - 1
        while l < r:
            cur_sum = num[i] + num[l] + num[r]
            if closet == target:
                return closet
            if cur_sum <= closet:
                l += 1
            else:
                r -= 1
            if abs(closet - target) > abs(cur_sum - target):
                closet = cur_sum

    return closet
#note this loop stops when l and r points at same value ie l is no longer less than r


num = [-1, 2, 1, -4]
print(threesum(num, 1))
