def decimal_binary(num):
    bit = 0
    decimal = 0
    while num != 0:
        last_digit = num % 10
        cur_decimal = last_digit * pow(2, bit)
        # pow means 2 raise to power of i
        decimal = decimal + cur_decimal
        num = num // 10
        bit += 1
    return decimal


num = int(input('Enter your binary number: '))
binary = decimal_binary(num)
print('Your decimal in decimal is ', binary)
