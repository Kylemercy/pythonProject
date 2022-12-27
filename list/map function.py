import math


def area(r):
    return math.pi * (r ** 2)


radii = [2, 5, 6.7, 8, 5.6]
# map function takes 2 argument first is the function , second is a list,tuple or dict
print(list(map(area, radii)))

# example 2

temp = [('berlin', 29), ('cario', 36), ('buenos aires', 19), ('los angles', 26), ('tokyo', 27), ('new york', 28),
        ('london', 22),
        ('beijing', 32)]
# lambda functions are used to create short functions in a single line
c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
fah = list(map(c_to_f, temp))
print(fah)

# filter use to select certain data from a list tuple
import statistics

data = [2.3, 3.3, 4.2, 5.7, 6.4, 7.9, 7.8, 8.76]
avg = statistics.mean(data)
print(avg)
# to return numbers greater than the avg use the filter fun
num = list(filter(lambda x: x > avg, data))
print(num)

countries = [ '','cairo', 'egypt', '', 'thialand', 'china',  '','nigeria', '', 'japan','','spain','']
print(list(filter(None, countries)))
