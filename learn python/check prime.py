def check_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


num = int(input('Enter a number: '))
is_prime = check_prime(num)
if is_prime:
    print('Your number is a prime.')
else:
    print('Your number is not a prime.')
