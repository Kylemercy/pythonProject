from linkedQ1 import Linkedlist


# returning nth element from the last
def nth_last(list, n):
    pointer1 = list.head
    pointer2 = list.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


custll = Linkedlist()
custll.generate(10, 0, 90)
print(custll)
print(nth_last(custll, 5))