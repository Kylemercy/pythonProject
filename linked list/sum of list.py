# adding 2 linked list and creating another linked list of the result

from linkedQ1 import Linkedlist


def sumlist(lla, llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    # creating a temporary linked list that will return the sum of lla and llb
    ll = Linkedlist()
    while n1 or n2:
        result = carry
        # carry here is the reminder from summing the two list
        if n1:
            result += n1.value
            n1 = n1.next

        if n2:
            result += n2.value
            n2 = n2.next
        # adding the result of the sum of the two linked list to the temporary linkedlist
        ll.add(int(result % 10))
        # this adds the reminder to the linked list
        carry = result / 10
        # this gives us the remaining number we are to carry
    return ll


lla = Linkedlist()
lla.add(7)
lla.add(1)
lla.add(6)

llb = Linkedlist()
llb.add(5)
llb.add(9)
llb.add(2)
print(lla)
print(llb)
print(sumlist(lla, llb))
