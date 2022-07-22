def find_pairs(num,target):
    for i in range(len(num)):
        for j in range(i + 1,len(num)):
            if num[i] == num[j]:
                continue
                #this prevent summation of two same integers if present
            elif num[i] + num[j] == target:
                print(i,j)
                #this print the index two pairs of num
num = [2,4,5,5,6,7,1,3,9,0,10]
find_pairs(num,9)
