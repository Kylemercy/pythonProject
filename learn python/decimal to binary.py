print('Coveting decimal number to binary using recursion')


def decimal_binary(num):
    if num > 1:
        decimal_binary(num // 2)
    print(num % 2, end='')


num = int(input('Enter your decimal number: '))
decimal_binary(num)
