# creation of singly linked list
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
class slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
singlylinkedlist = slinkedlist()
node1 = Node()
node2 = Node()
singlylinkedlist.head = node1
singlylinkedlist.head.next = node2
singlylinkedlist.tail = node2