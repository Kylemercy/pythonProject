# lambda function a nameless function
num = lambda x: 3 * x + 1
print(num(7))
# strip use to remove white spaces fom string title use to capitalize the first later of a string
fullname = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print(fullname('  mercy', 'OBED'))
scifi_authors = ['Isacc Amosiv', 'Ray Radson', 'Robert Heinlen', 'Arthur C.Clarke,', 'Frank Hebert', 'Orson Scott Card',
                 'Douglas Adams', 'H.G.Wells', 'Leigh Brackket']
# to get the last name
# split() is use to split the string were ever there is a space and -1 is use to get the last name
# this sort the list base on their last name
scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)


def build_quadratic(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic(2, 3, -5)
print(f(2))
f = build_quadratic(3, 0, 1)
print(f(2))
