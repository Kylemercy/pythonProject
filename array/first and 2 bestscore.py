list = [2,4,5,7,8,9,10,11,43]
def firstsecond(list):
    a = list
    a.sort(reverse= True)
    print(a)
    first = a[0]
    second = None
    for i in list:
        if i != first:
            second = i

            return first,second
print(firstsecond(list))
