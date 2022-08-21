# sum of closet number close to target
def threesum(num, target):
    num.sort()
    n = len(num)
    # closet value
    closet = num[0] + num[1] + num[2]

    for i in range(0, n - 2):
        # creating your pointer
        l, r = i + 1, n - 1
        while l < r:
            cur_sum = num[i] + num[l] + num[r]
            if cur_sum <= closet:
                l += 1
            else:
                r -= 1
            if abs(closet - target) > abs(cur_sum - target):
                closet = cur_sum

    return closet


num = [-1, 2, 1, -4]
print(threesum(num, 1))
