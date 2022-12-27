# dont contain duplicate
sets1 = {2, 4.5, 'ada', True}
sets1.add(4)
sets1.add(5)
# to add more than one value
sets1.update(['cat', 45, 'dog'])
s2 = {'pink', 'red', 'indigo'}
sets1.update([54, 55, 67], s2)
print(sets1)
# to delete an item in set
sets1.remove(4)
print(sets1)
sets1.discard(5)
print(sets1)
# the diff between discard and remove for remove if the value dosnt exist in the set it throws an error while discard
# juts prints the value in the set without throwing an error
# operations in set
s3 = {'pink', 'red', 55, 'blue'}
s4 = s2.intersection(s3, sets1)
print(s4)
s5 = sets1.difference(s2, s3)
print(s5)
# symmetric difference prints the values that both sets A and B don't have in common
s6 = [2, 'ada', 'pink', 'orange', 'egg', 67]
s7 = s2.symmetric_difference(s6)
print(s7)

l1 = [2, 3, 2, 4, 5, 3, 6, 5]
l2 = list(set(l1))
# this remove the duplicates in l1 and prints the result in list form
print(l2)
employee = ['corey', 'jim', 'steven', 'april', 'judy', 'jenn', 'john', 'jane']
gym_members = ['april', 'john', 'corey']
developers = ['judy', 'corey', 'steven', 'jane', 'april']
result = set(employee).intersection(developers)
print(result)
result2 = set(gym_members).intersection(developers)
print(list(result2))
result3 = set(employee).difference(gym_members, developers)
print(result3)
result4 = set(developers).union(gym_members)
print(result4)

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
composite = {4, 6, 8, 9, 10}
print(list(odds.union(evens)))
print(primes.intersection(odds))
print(primes.intersection(evens))
print(evens.intersection(odds))
print(primes.union(composite))
print(2 in primes)
print(9 not in evens)
help(set)
