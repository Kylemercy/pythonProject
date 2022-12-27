earth_metals = ['beryllium', 'magnesium', 'calcium', 'strontium', 'barium', 'radium']
# base on increasing atomic number
earth_metals.sort()
# this sort the list alphabetically
print(earth_metals)
# for reverse order
earth_metals.sort(reverse=True)
print(earth_metals)
# storing this in a tuple
earth_metals = ('beryllium', 'magnesium', 'calcium', 'strontium', 'barium', 'radium')
# this gives an error as tuple are immutable
planets = [('mecury', 2440, 5.43, 0.395),
           ('venus', 6052, 5.24, 0.734),
           ('earth', 6378, 5.52, 1.00),
           ('mars', 3396, 3.93, 1.530),
           ('jupiter', 71492, 1.33, 5.210),
           ('saturn', 60268, 0.69, 9.531),
           ('uranus', 25559, 1.27, 19.231),
           ('neptune', 24789, 1.64, 30.070)]
# to sort to base on the largest to the smallest planet
size = lambda planet: planet[1]
# this returns the second index of the tuple as index starts from one
planets.sort(key=size, reverse=True)
print(planets)
# sorting base on density starting from the least dense
density = lambda planet: planet[2]
planets.sort(key=density)
print(f'sorting planets based on their density from the least dense to the highest: {planets}')
# sorted method this creates a copy of the data and can be use to sort tuples
sorted_earth = sorted(earth_metals)
print(sorted_earth)
data = (3, 2, 6, 4, 76, 45, 89, 55, 47, 49)
sort_data = sorted(data)
print(sort_data)
# note sorted returns the sorted tuple in list
