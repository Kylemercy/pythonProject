#searching for element in an array
import numpy as np
num = np.array([11,3,4,5,6,8,9,11,12,13,16,17,34,30])
def search_num(num,target):
    for i in range(len(num)):
        if i == target:
           print('number found at indeex:',num[i])
           return


    print('number not found')
    return
search_num(num,19)

