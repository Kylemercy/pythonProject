# inserting into a singly linkedlist
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertsinglylist(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        # inserting at the beginning of a linked list
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            # inserting at the end of the linked list
            elif location == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            #inserting at the middle

            else:
                tempnode = self.head
                count = 0
                while count < location - 1:
                    tempnode = tempnode.next
                    count += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode

    def list_travasal(self):
        if self.head is None:
            print('list is empty')
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
ll = slinkedlist()
ll.insertsinglylist(0,1)
ll.insertsinglylist(1,2)
ll.insertsinglylist(2,3)
ll.insertsinglylist(3,4)
ll.insertsinglylist(4,5)
print([node.value for node in ll])