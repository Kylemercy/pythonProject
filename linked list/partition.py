# it partitions the list based on the given n value with the value < n at the left and  value > on the right
from linkedQ1 import Linkedlist


def partition(ll, x):
    curnode = ll.head
    ll.tail = ll.head
    while curnode:
        nextnode = curnode.next
        curnode.next = None
        # inserting at the beginning if next value is < than n
        if curnode.value < x:
            curnode.next = ll.head
            ll.head = curnode
        else:
            ll.tail.next = curnode
            ll.tail = curnode
        curnode = nextnode
        # if the value is  > than n
        # to set tail next reference to none
        if ll.tail.next is not None:
            ll.tail.next = None


ll = Linkedlist()
ll.generate(10, 0, 90)
print(ll)
partition(ll, 30)
print(ll)
