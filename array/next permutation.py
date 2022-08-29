# next permutation
# permutation
def nextpermutation(num):
    n = len(num)
    # this is where our aray stop being sorted we call the last num pivot ie its stops increasing and that's decreasing
    # find our pivot start from the last element
    pivot = None
    for i in range(n - 1, 0, -1):
        if num[i] > num[i - 1]:
            # this checks if I is > than the next element if so the pivot becomes the next element i - 1
            pivot = i - 1
            break

    else:
        # we don't have a pivot this means the array is already sorted in ascending order
        num.reverse()
        return
    swap = n - 1
    while num[swap] <= num[pivot]:
        swap -= 1
        # this checks whether our swap is < pivot  if so it keeps on iterating till we see a num greater than pivot which becomes our swap
    num[pivot], num[swap] = num[swap], num[pivot]
    # we swap the 2 element when we find an element greater than the pivot
    num[pivot + 1:] = reversed(num[pivot + 1:])

    return


num = [1, 2, 5, 8, 7]
nextpermutation(num)
