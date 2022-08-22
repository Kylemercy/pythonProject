# container with the most water
def maxarea(height: list[int]):
    res = 0
    # pointers
    l, r = 0, len(height) - 1
    while l < r:
        # this checks for the minimum between the two height to avoid water spilling
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        # r - l is used to find the weight of the container
        # to shift our pointer
        if height[l] < height[r]:
            l += 1
        else:
            # when both height are equal or left height is  > than right height then shift right
            r -= 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxarea(height))
