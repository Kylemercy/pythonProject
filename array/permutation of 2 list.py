#permutation of two list
#checking if two list contains thesame elememt
def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
list1 = [3,4,5,6,7,8]
list2 = [3,4,5,7,7,8]
list3 = ['a','d','c','b']
list4 = ['a','b','c','d']
print(permutation(list1,list2))
print(permutation(list3,list4))