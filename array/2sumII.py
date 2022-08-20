# sum of 2  that the  two number sum to the Target
# note the array is sorted and the firsts index of the number is < than the second num index
def twosum_ii(num, target):
    # pointers
    l, r = 0, len(num) - 1
    while l < r:
        cur_sum = num[l] + num[r]
        if cur_sum > target:
            r -= 1
            # this shift the right pointer to thr left
        elif cur_sum < target:
            l += 1
            # this shift our left pointer to the right
            # note our list is sorted
        else:
            return [l + 1, r + 1]
        # according to the rule we add 1 to the index


num = [3, 4, 5, 6, 7, 8, 9]
print(twosum_ii(num, 13))
