num = [2,3,4,2,1,5,6,7,8,9,5,0]
def remove_dup(num):
    temp = [ ]
    for i in num:
        if i in temp:
            continue
        else:
            temp.append(i)

    return temp
print(remove_dup(num))