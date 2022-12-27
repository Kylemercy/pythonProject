"""def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
        #this method is only suitable for small numbers like numbers less than 100


for n in range(1, 1000):
    print(n, '=', fibonacci(n))
    #this first function is slow """
# using memoization to make our code faster
fibano_cache = {}

'''def fibonacci(n):
    #if the value has already been cached return it
    if n in fibano_cache:
        return  fibano_cache[n]
    elif n == 1:
        value = 1
    elif n == 2:
        value =1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fibano_cache[n] = value
    return value

for n in range(1, 1000):
    print(n, '=', fibonacci(n))
 this method uses memorization'''

# using inbuilt memorization
from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 500):
    print(n, '=', fibonacci(n))
    # ratio of fibonacci numbers follows the golden ratio
for n in range(1, 50):
    print(fibonacci(n + 1) / fibonacci(n))
