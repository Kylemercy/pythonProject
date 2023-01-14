# when a function use yield rather than return
# the are functions that act as iterators the generated the element we are to loop over
import string
import itertools


def letters():
    for letter in string.ascii_lowercase:
        yield letter


for c in letters():
    print(c)


def prime_num():
    yield 2
    # 2 is the first prime num
    prime_cache = [2]
    # to loop through positive odd integers
    for n in itertools.count(3, 2):
        # our loop starts from 3 and move 2 step forward
        is_prime = True
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n


for p in prime_num():
    print(p)
    if p > 100:
        break

# alternate way to create generator
squares = (x ** 2 for x in itertools.count(1))
for x in squares:
    print(x)
    if x > 300:
        squares.close()
