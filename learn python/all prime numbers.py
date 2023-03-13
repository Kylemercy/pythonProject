def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
def all_primes(num):
    primes = [ ]
    for i in range(2,num + 1):
        if check_prime(i) is True:
            primes.append(i)
    return primes


num = int(input('Enter a number: '))
is_primes = all_primes(num)
print(f'All prime numbers within the given range of given number is:{is_primes}')