def b(x):
    return x + 3


def is_odd(x):
    return x % 2 != 0


a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
d = list(filter(is_odd, a))
#filters all the element that are even
print(d)
#filter and map
c = list(map(b,filter(is_odd,a)))
#this is same with
_ = list(map(b,d))
print(c)