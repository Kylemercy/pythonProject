num = [5,6,7,8,12,2,3,1,9]
def pairs(num,n):
    result = [ ]
    for i in range(len(num)):
        for j in range(1,len(num)):
            if num[i] == num[j]:
                continue
            elif num[i] + num[j] == n:
                result.append(str(num[i]) + '+' + str(num[j]))
    return result
print(pairs(num,12))