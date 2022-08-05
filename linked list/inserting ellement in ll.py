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
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        # inserting at the beginning of a linked list
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            # inserting at the end of the linked list
            elif location == -1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            #inserting at the middle
            tempnode = self.head
            index = 0
            while index < location - 1:
                tempnode = tempnode.next
                index += 1
                nextnode = tempnode.next
                newnode = tempnode.next
                newnode.next = nextnode