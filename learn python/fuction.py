# functions with more than one input
def greet(name, location):
    print(f'Hello {name}.')
    print(f'How is it like in {location}.')


greet(name='ada', location='enugu')
# this is called keyword argument


import math


def paint_calc(height, width, cover):
    area = (height * width) / cover
    num_of_cans = math.ceil(area)
    # ceil is used to round a num to the nearest whole number
    print(f'You will need {num_of_cans} of paint')


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


def prime_checker(number):
    is_prime = True
    for i in range(2, number):

        if number % i == 0:
            is_prime = False

    if is_prime:
        print("it's a prime number")

    else:
        print("it's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
