def get_prime_factors(num):
    factors = []
    divisor = 2
    while num > 2:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors


num = int(input('Enter a number: '))
factor = get_prime_factors(num)
print('factors of given number is: ', factor)
1