import collections

# named tuple allows us to access our tuple via index
points = collections.namedtuple('point', 'x y z')
newp = points(3, 4, 5)
print(newp)
# works for both dict and list
print(newp.y, newp.x)
print(newp[2])
print(newp._asdict())
print(newp._replace(y=6))
p2 = points._make(['a', 'b', 'c'])
print(p2)
# deque datatype in collection module
# is very fast in adding elements to the beginning and end of a list
from collections import deque

d = deque('hello')
# methods
d.append(4)
d.append(8)
# to append to thw beginning
d.appendleft(3)
d.pop()
d.popleft()
# remove the first element
d.extend('rat')
d.extendleft('hey')
# this adds this element in reverse other to the front of the deque

print(d)
d.rotate(-1)
print(d)
d.rotate(-2)
print(d)
d.rotate(1)
print(d)
p = deque('hello', maxlen=5)
p.extend([1, 2])
print(p)
