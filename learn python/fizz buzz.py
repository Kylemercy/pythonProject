# fizz buzz
for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print('FrizzBuzz')


    elif i % 5 == 0:
        print('Frizz')


    elif i % 3 == 0:
        print('Buzz')


    else:
        print(i)
