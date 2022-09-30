class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class circular_doubly_linked:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create_cdl(self, nodevalue):
        newnode = Node(nodevalue)
        self.head = newnode
        self.tail = newnode
        newnode.prev = newnode
        newnode.next = newnode
        return 'the CDLL has been created'

    def insert_dll(self, value, location):
        if self.head is None:
            return ' CDLL is empty'
        else:
            newnode = Node(value)
            if location == 0:
                # inserting at beginning of list
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.head = newnode
                self.tail.next = newnode
            # inserting at the end
            elif location == 1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next = newnode
                self.tail = newnode
            else:
                curnode = self.head
                index = 0
                while index < location - 1:
                    curnode = curnode.next
                    index += 1
                newnode.next = curnode.next
                newnode.prev = curnode
                newnode.next.prev = newnode
                curnode.next = newnode
                return ' Node has been successfully inserted'

    def travasal_cdll(self):
        if self.head is None:
            return ' CDLL is empty'
        else:
            curnode = self.head
            while curnode:
                print(curnode.value)
                if curnode == self.tail:
                    break
                curnode = curnode.next

    def reverse_travasal(self):
        if self.head is None:
            return ' CDLL is empty'
        else:
            curnode = self.tail
            while curnode:
                print(curnode.value)
                if curnode == self.head:
                    break
                curnode = curnode.prev

    def searchdll(self, nodevalue):
        if self.head is None:
            return ' CDLL is empty'
        tempnode = self.head
        while tempnode:
            if tempnode.value == nodevalue:
                return tempnode.value
            if tempnode == self.tail:
                return 'value does not exit in the cdll.'
            tempnode = tempnode.next

    def deletenode(self, location):
        if self.head is None:
            return ' CDLL is empty'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.next
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curnode = self.head
                index = 0
                while index < location - 1:
                    curnode = curnode.next
                    index += 1
                curnode.next = curnode.next.next
                curnode.next.prev = curnode
            print('the node has been successfully deleted')
    def deletecdll(self):
        if self.head is None:
            return ' CDLL is empty'
        else:
            self.tail.next = None
            curnode = self.head
            while curnode:
                curnode.prev = None
                curnode = curnode.next

            self.tail = None
            self.head = None
            print('the entire cdll has been deleted successfully')

cdll = circular_doubly_linked()
print(cdll.create_cdl(5))
cdll.insert_dll(0, 0)
cdll.insert_dll(3, 1)
cdll.insert_dll(2, 2)
cdll.insert_dll(4, -1)

print([node.value for node in cdll])
cdll.travasal_cdll()
print(cdll.searchdll(8))
print('\n')
cdll.reverse_travasal()
cdll.deletenode(0)
print([node.value for node in cdll])
cdll.deletecdll()
print([node.value for node in cdll])

