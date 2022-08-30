##to find the first and last index of a target value in a sorted aray
# using binary search
def findfirstoccurance(num, target):
    # left and right pointers
    left, right = 0, len(num) - 1
    firstoccurance = -1
    # we loop until the two pointers meet
    while left <= right:
        # middle index
        mid = (left + right) // 2
        # check if you have found the value
        if target == num[mid]:
            firstoccurance = mid
            right = mid - 1
            # keep on shifting the right pointer till it reaches the left
        elif target < num[mid]:
            # if target is less than the num in the middle shift the right pointer to the left
            right = mid - 1
        else:
            # the target is greater than the num in the middle shift the left pointer to the right
            left = mid + 1

    return firstoccurance


def lastoccurance(num, target):
    # left and right pointers
    left, right = 0, len(num) - 1
    lastoccurance = -1
    # we loop until the two pointers meet
    while left <= right:
        # middle index
        mid = (left + right) // 2
        # check if you have found the value
        if target == num[mid]:
            lastoccurance = mid
            left = mid + 1
            # moving the left pointer to the right till it overlap with the right pointer
            #
        elif target < num[mid]:
            # if target is less than the num in the middle shift the right pointer to the left
            right = mid - 1
        else:
            # the target is greater than the num in the middle shift the left pointer to the right
            left = mid + 1
    return lastoccurance


def search(num, target):
    return [findfirstoccurance(num, target), lastoccurance(num, target)]


num = [2, 3, 4, 6, 7, 7, 7]
# this only works for sorted arrays
print(search(num, 7))
