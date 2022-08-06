def rev_num(num):
    temp = 0
    while num > 0:
        rem = num % 10
        temp = temp * 10 + rem
        num = num // 10
    return temp
num = 1278009
print(rev_num(num))
