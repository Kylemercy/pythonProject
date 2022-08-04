#list in python
integers = [2,6,7,5,8]
print(integers)
stringlist = ['milk','sugar','egg','fish']
print(stringlist)
mixedlist = [23,4.8,'frog']
print(mixedlist)
nestedlist = [34,56,['egg',6,7],7.8]
print(nestedlist)
#acessing or travasing through a list
print(stringlist[0])
print('milk' in stringlist)
print('bread' in stringlist)
#travasing through list
for i in stringlist:
    print(i)
for i in range(len(stringlist)):
    stringlist[i] = stringlist[i] + '+'
    print(stringlist[i])