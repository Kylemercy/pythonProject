sports = {'peter': 'football', 'john': 'golf', 'ken': 'running', 'dan': 'tennis', 'dil': 'swimming'}
# operations in dictionary
print('ken' in sports)
print('ken' in sports.values())
# for operator
for key in sports:
    print(key)
# to print key and value
for key in sports:
    print(key, sports[key])
# all operator returns true if all element in the iterable are true
mydict = {1: True, 2: True, 3: True}
print(all(mydict))
# this returns true
mydict3 = {}
print(all(mydict3))
# this returns true
dict1 = {0: True, 1: False, 2: True}
print(all(dict1))
# this returns false as one element is false
mydict2 = {0: False, 1: False, 2: False}
print(all(mydict2))
# returns false
mydict4 = {0: False, 1: False, 2: True}
print(all(mydict4))
# returns false
# any method
mydict = {1: True, 2: True, 3: True}
print(any(mydict))
# this returns true
mydict3 = {}
print(any(mydict3))
# this returns false
dict1 = {0: True, 1: False, 2: True}
print(any(dict1))
# this returns tue as one element is true
mydict4 = {0: False, 1: False, 2: True}
print(any(mydict4))
# Returns true
dict2 = {0: False, 1: False}
print(any(dict2))
# returns false
# len method
print(len(sports))
# sorted method
# prints the list of the key in ordered formaT
print(sorted(sports))
print(sorted(sports, reverse=True))
# using the key parameter of sorted method
print(sorted(sports, key=len))
# this sort the dict based on their length
