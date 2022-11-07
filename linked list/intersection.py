from linkedQ1 import Linkedlist, Node

''' finding were 2 linked list intersect,returns the intersecting node,the intersection
is defined based on reference not value.that is if the kth noe of the 
first list is exact same node(by reference) as the jth node of the second list
the are intersecting'''


def intersection(llA, llB):
    # to check if the last node of both list are pointing the same if not return false
    if llA.tail is not llB.tail:
        return
    # this means the list are not intersecting

    lenA = len(llA)
    lenB = len(llB)
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA
    diff = len(longer) - len(shorter)
    longernode = longer.head
    shorternode = shorter.head
    for i in range(diff):
        # this will start looping from the diff of the two list
        longernode = longernode.next
    # to start looping
    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next
    # this loops executes aslong as the shorter node and longer node are not intercepting
    return longernode


def add_samenode(llA, llB, value):
    # to add same node at the end of both linked list a and b
    tempnode = Node(value)
    llA.tail.next = tempnode
    llA.tail = tempnode

    llB.tail.next = tempnode
    llB.tail = tempnode


llA = Linkedlist()
llA.generate(5, 0, 15)
llB = Linkedlist()
llB.generate(7, 0, 15)
add_samenode(llA, llB, 8)
add_samenode(llA, llB, 14)
print(llA)
print(llB)
print(intersection(llA, llB))
