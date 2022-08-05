def middle(mylist):
    newlist = mylist[1: ]
    del newlist[-1]
    return newlist

mylist = [1,2,3,4]
print(middle(mylist))
