print('SUN OF SQUARES OF GIVEN NUMBER')
num = int(input('enter a number:'))
def sum_num(num):
    temp = 0
    for i in range(num+1):
        square = i **2
        temp += square
    return temp
print(sum_num(num))

