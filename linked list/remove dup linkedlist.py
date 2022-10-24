from linkedQ1 import Linkedlist


def delete_duplicate(list):
    if list.head is None:
        return 'The list is empty'

    else:

        curnode = list.head
        visited = {curnode.value}

        while curnode.next:

            if curnode.next.value in visited:
                curnode.next = curnode.next.next
            else:
                visited.add(curnode.next.value)
                curnode = curnode.next
        return list
    # creating a method with space complexity of 1


def remove_duplicate(list):
    if list.head is None:
        return 'The list is empty'
    curnode = list.head
    while curnode:
        runner = curnode
        while runner.next:
            if runner.next.value == curnode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curnode = curnode.next
    return list.head
# this has a time complexity of O(n2) but space complexity of O(1)


ll = Linkedlist()
ll.generate(10, 1, 80)
print(ll)
#delete_duplicate(ll)
remove_duplicate(ll)
print(ll)
print(len(ll))
