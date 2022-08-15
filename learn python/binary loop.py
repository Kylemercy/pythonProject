def dec_to_binary(n):
    bits = []
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    bits.reverse()
    binary = ' '
    for bit in bits:
        binary += str(bit)
    return binary


n = int(input('Enter your decimal number: '))
result = dec_to_binary(n)
print('your binary number is: ', result)
