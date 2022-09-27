# this returns the max sum of sub arrays when added together
class solution:
    def max_subarray(self, array):
        maxsum = array[0]
        # initialise the maxsum to the first number
        cursum = 0
        for i in array:
            if cursum < 0:
                cursum = 0
                # if the cursum is less than 0 we initialise the cursum to 0 else we keep our cur i and add it to our cur sum
            cursum += i
            maxsum = max(maxsum, cursum)
        return maxsum


ll = solution()
print(ll.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
