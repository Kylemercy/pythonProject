# difference between lists and tuple
list1 = [3, 4, 5, 1, 2]
list1[2] = 7
print(list1)
# here the 2index element is modified showing that list are mutable
# to resign all the element in a list
list1 = [8, 6, 5, 12, 11, 34, 56]
# all the elements in the list are reassigned
print(list1)
tuple1 = (3, 4, 5, 1, 2)
# changing a list using index
# tuple1[1] = 9
print(tuple1)
# this gives an error
# tuple reassignment
tuple1 = (8, 6, 5, 12, 11, 34, 56)
print(tuple1)
# deleting aan element from a tuple gives an error
# del tuple[1]
# rather we del all the elements
# storing a tuple in a list
list2 = [(1, 2), (3, 4), (7, 8)]
print(list2)
# creating a list in a tuple
tuple2 = ([10, 11], [67, 89], [89, 90])
print(tuple2)
