#finding the max product of two numbers
import numpy as np
num = np.array([11,3,4,5,6,8,9,11,12,13,16,17,34,50,30])

def productmax(num):
    max_product = 0
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] * num[j] > max_product:
                max_product =  num[i] * num[j]
                pairs = str(num[i]) + ' ' + str(num[j])
    print(pairs)
    print(max_product)
productmax(num)