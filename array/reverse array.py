def reverse_integer(num):
    temp = 0
    is_negative = 1
    if num < 0:
        is_negative = -1
        num = num * -1
    while num > 0:
        rem = num % 10
        temp = temp * 10 + rem
        num = num // 10
    if temp >= 2 ** 31 - 1 or temp <= -2 ** 31:
        return 0
    return temp * is_negative


# return -temp if is_negative  else temp

num = 120

print(reverse_integer(num))
