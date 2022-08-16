def get_smallest_prime_factor(num):
    factor = 2
    while num % factor != 0:
        factor += 1
    return factor
num = int(input('Enter a number: '))
smallest_num = get_smallest_prime_factor(num)
print('the smallest prime factor is: ',smallest_num)
