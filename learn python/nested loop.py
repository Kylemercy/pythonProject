n1 = [['red', 'yellow', 'blue', 'green'], ['fish', 'egg', 'rice', 'beans'], ['apple', 'banana', 'orange'],
      ['carrot', 'pepper', 'rice', 'onion']]
# to check whether an element is present in a list
print('red' in n1)
# this will return false which is wrong for nested loop we use the ANY method
print(any('apple' in inner_list for inner_list in n1))  # this returns true

print(any('pie' in inner_list for inner_list in n1))  # this returns false
# reversing a nested loop
my_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
result = my_list[::-1]
print(result)
# or using reverse func
my_list.reverse()
print(my_list)
# reversing element in a sub list
for sub_list in my_list:
    sub_list.reverse()
print(my_list)
# flatten nested list
result = [n for sub_list in n1 for n in sub_list]
print(result)
# finding index of all occurrence in a nested list
for sub_list in n1:
    if 'rice' in sub_list:
        print((n1.index(sub_list), sub_list.index('rice')))
# checking whether all the listed occurrence of rice is correct
print(n1[1][2])
print(n1[3][2])
# enumerate function
grocery = ['bread', 'milk', 'butter', 'biscuit']
# enumerate method adds counter to an iterable and returns it
enumerategrocery = enumerate(grocery)
print(enumerategrocery)
print(list(enumerategrocery))
enumerategrocery = enumerate(grocery, 10)
print(tuple(enumerategrocery))
# looping through enumerate object
for item in enumerate(grocery):
    print(item)
print('\n')
for count, item in enumerate(grocery):
    print(count, item)
print('\n')
for count, item in enumerate(grocery, 100):
    print(count, item)
# renumerate nested list
txt = [(i1, i2) for (i1, v1) in enumerate(n1) for (i2, v2) in enumerate(v1) if v2 == 'rice']
print(txt)
# count function
rez = sum(t.count('rice') for t in n1)
print(rez)
# remove element in nested list
for sub in n1:
    for n in sub:
        if n == 'carrot':
            sub.remove('carrot')
print(n1)
# how to insert in a nested loop
for ind, sub_list in enumerate(n1):
    print(ind, sub_list)
print('\n')
for ind, sub_list in enumerate(n1):
    if ind == 2:
        sub_list.insert(1, 'tomato')
print(n1)

# replacing all occurrences in a nested list
my_list = [[1, 2, 2], [1, 3, 4], [2, 5, 6, 7]]
for i1, sublist in enumerate(my_list):
    for i2, elem in enumerate(sublist):
        if elem == 2:
            my_list[i1][i2] = 23
print(my_list)
# convert nested loop to dictionary
my_list = [['fruit', 'orange'], ['colour', 'red'], ['food', 'potato']]
result = {}
for sub_list in my_list:
    result[sub_list[0]] = sub_list[1]
print(result)

