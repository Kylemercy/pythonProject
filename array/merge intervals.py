# merging 2 lists if the overlap with one another
class solution:
    def mergearray(self, intervals):
        # time comp is O(nlogn)
        intervals.sort(key=lambda i: i[0])
        # this sort the sub list base on their first value
        output = [intervals[0]]
        # output contains the merged lists and the unmerged lists
        # it is initialised using the values of the fist list
        for start, end in intervals[1:]:
            # this starts iterating from the second element
            lastend = output[-1][1]
            '''this gives the last value of the last entered entry,note our sub lists contains only 2 values'''
            if start <= lastend:
                output[-1][1] = max(lastend, end)
                '''this checks if the starting value of the next interval is less than than the last value of the last
                entry if so we then initialise the last value to the max value between the last entry and the new interval
                last '''
            else:
                # if the intervals are not overlapping we then append the intervals
                output.append([start, end])
                #
        return output


ll = solution()
print(ll.mergearray([[1, 3], [2, 6], [8, 10], [8, 13], [15, 18], [17, 23]]))
