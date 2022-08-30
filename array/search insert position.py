# search for the insert position of a given target if it doesn't exit in the array
# but if it exit return the index of the target
def insert_position(num, target):
    # using binary search since the array is sorted
    left, right = 0, len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        if num[mid] == target:
            return mid
        if target > num[mid]:
            left = mid + 1
        else:
            right = mid - 1
            # this return the index of the left pointer  if the target doesn't exit
            '''cause when the target dosent exit in the array it gets to a point the left 
            and right pointers exchange position in such case return the index of the left pointer'''
    return left


#
num = [2, 3, 5, 6, 7, 8]
print(insert_position(num, 9))
