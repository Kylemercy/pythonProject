# To convert from base 10 to base 2
def dec_to_binary(num):
    bits = []
    while num > 0:
        bits.append(num % 2)
        num = num // 2
    bits.reverse()

    binary = " "
    for bit in bits:
        binary += str(bit)
    return binary


num = int(input("Enter your number in base10: "))
result = dec_to_binary(num)


# To convert from base 10 to base 2
def dec_to_binary(num):
    bits = []
    while num > 0:
        bits.append(num % 2)
        num = num // 2
    bits.reverse()

    binary = " "
    for bit in bits:
        binary += str(bit)
    return binary



num = int(input("Enter your number in base10: "))
result = dec_to_binary(num)
print("you number in base2 is:", result)
