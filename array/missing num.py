#solvimg for a missing number in a given array
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30]

def missing_num(array,n):
    sum1 = 30  * 31/ 2
    sum2 = sum(array)
    print(sum1 - sum2)
missing_num(array,30)