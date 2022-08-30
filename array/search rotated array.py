# search a sorted array in ascending order suppose it's been rotated at a pivot unknown
def rotate_sorted(num, target):
    # note the array is already  sorted
    l, r = 0, len(num) - 1
    # left and right pointers
    # run a binary search as the array is sorted
    while l <= r:
        mid = (l + r) // 2
        if target == num[mid]:
            return mid
        # to check if the mid-value  is on the left side of the sorted array
        if num[l] < num[mid]:
            # this means the mid-value is at the left
            if target > num[mid] or target < num[l]:
                # this checks whether the target is less than the value in the left
                l = mid + 1
                # we search towards the right l becomes a num after our mid-value and a new mid is found
            else:
                r = mid - 1
                # r becomes the num before our former mid value

        # to check if the mid-value is in the right side
        else:
            if target < num[mid] or target > num[r]:
                r = mid - 1
            else:
                l = mid + 1
    return


num = [8, 9, 10, 11, 12, 2, 3, 4, 5, 6, 7]
print(rotate_sorted(num, 9))
