#finding the maximum number in an array
import numpy as np
num = np.array([11,3,4,5,6,8,9,11,12,13,16,17,34,50,30])
def search_num(num):
    max_num = num[0]
    for i in range(len(num)):
        if num[i] > max_num:
            max_num = num[i]
    print(max_num)
search_num(num)