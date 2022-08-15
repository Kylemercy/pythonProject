print('CONVERTING MILES TO KILOMETRES')


def distance(mile):
    temp = mile * 1.609344
    result = round(temp, 2)
    print('Your distance covered in kilometers is: ', result, 'kilometers')


mile = int(input('enter your distance in miles: '))
distance(mile)
