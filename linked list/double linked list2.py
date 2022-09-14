# Creating double linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class doubly_linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def creation_doubly(self, nodevalue):
        node = Node(nodevalue)
        self.head = node
        self.tail = node
        return 'The double linked list has been created'

    def insertion(self, nodevalue, location):
        if self.head is None:
            print('the list is empty')

        else:
            # inserting at the beginning of the list
            newnode = Node(nodevalue)
            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode

            # at the end
            elif location == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                # note tempnode means curnode
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                # creating link between our newnode and next node
                tempnode.next = newnode

    def travasal(self):
        if self.head is None:
            print('list is empty')
        else:
            curnode = self.head
            while curnode:
                print(curnode.value, end=' ')
                curnode = curnode.next

    def backward_travasal(self):

        if self.head is None:
            print('list is empty')
        else:
            curnode = self.tail
            while curnode:
                print(curnode.value, end=' ')
                curnode = curnode.prev

    def searching(self, nodevalue):
        if self.head is None:
            print('list is empty')
        else:
            curnode = self.head
            while curnode:
                if curnode.value == nodevalue:
                    return curnode.value
                curnode = curnode.next
            return ' the value dose not exit in the list.'

    def deletion_node(self, location):
        if self.head is None:
            print('list is empty')

        else:
            if location == 0:
                # if it's the only node in list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # has more than one node in list
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                # deletion at the end of list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # has more than one node in list
                    self.tail = self.tail.prev
                    self.tail.next = None
            # deletion at anywhere in the list
            else:
                curnode = self.head
                index = 0
                while index < location - 1:
                    curnode = curnode.next
                    index += 1
                curnode.next = curnode.next.next
                curnode.next.prev = curnode
            print('the node has been deleted')

    def delete(self):
        if self.head is None:
            print('list is empty')
        else:

            curnode = self.head
            while curnode:
                curnode.prev = None
                curnode = curnode.next
            self.head = None
            self.tail = None
            print('the DLL has been successfully deleted')


dll = doubly_linked()
dll.creation_doubly(5)
print([node.value for node in dll])
dll.insertion(0, 0)
dll.insertion(2, 1)
dll.insertion(6, -3)
dll.insertion(7, 2)
dll.insertion(4, 3)
print([node.value for node in dll])
dll.deletion_node(0)
dll.deletion_node(1)
dll.deletion_node(2)
dll.deletion_node(-1)
print([node.value for node in dll])
dll.travasal()
print('\n')
dll.backward_travasal()
print('\n')
print(dll.searching(6))
dll.delete()
print([node.value for node in dll])
