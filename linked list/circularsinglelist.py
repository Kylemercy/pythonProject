class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Circular_ll:
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

    def createcircular(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        print('circular single linked list has been created.')
        return

    def insertion_node(self, value, location):
        if self.head is None:
            return 'the list is empty.'
        else:
            # inserting at the beginning of the list
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                # to insert in the end of the list the location must be 1
                # inserting at the end
                new_node.next = self.tail.next
                # this creates reference between the newnode and the head
                self.tail.next = new_node
                # this creates a link between the tail and new node
                self.tail = new_node
            else:
                # inserting at the middle
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                    # this loops through until the index matches the location
                # if index equals location-1 ie stops at an index before our location
                nextnode = tempnode.next
                tempnode.next = new_node
                new_node.next = nextnode
                return
        # print('the node has been successfully inserted')

    def travasal(self):
        if self.head is None:
            print('list is empty.')
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                # to break the loop
                if tempnode == self.tail.next:
                    break

    def searching(self, nodevalue):
        # search if a value exist in the list and returns the value if it exit
        if self.head is None:
            return 'list is empty'
        else:
            tempnode = self.head
            count = 0
            while tempnode:

                if tempnode.value == nodevalue:
                    return f'index of value is {count} '
                tempnode = tempnode.next
                count += 1
                if tempnode == self.tail.next:
                    # at the end of the list
                    return 'the value dose not exit'

    def deletion(self, location):
        if self.head is None:
            return 'list is empty'
        else:
            # deleting the first node
            if location == 0:
                if self.head.next == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    # this is used to delete an element in a list that contains only one node
                else:
                    # deleting in alist with more than one node
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                # deleting from the end of  the list
                # if the list has one node
                if self.head.next == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        # to find the node before the last node
                        if node.next == self.tail:
                            break
                        node = node.next
                    # to make the new node the tail
                    node.next = self.head
                    node = self.tail
            else:
                # to delete in the middle
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                # if we get to the index before our location
                nextnode = tempnode.next
                # the nextnode is the curent next node
                # we now make our current next to point to our nextnode next
                # our cur node 4 now points to 5
                tempnode.next = nextnode.next
                # this ceates a link between our current node and the next node

    def delete_list(self):
        self.head = None
        self.tail.next = None
        self.tail = None



cll = Circular_ll()
cll.createcircular(1)
cll.insertion_node(0, 0)
cll.insertion_node(2, 1)
cll.insertion_node(3, 1)
cll.insertion_node(2, 2)
cll.insertion_node(4, 1)
cll.insertion_node(5, 3)
cll.travasal()
print([node.value for node in cll])
cll.deletion(2)
cll.deletion(1)
print([node.value for node in cll])
print(cll.searching(2))
print([node.value for node in cll])
cll.delete_list()
print([node.value for node in cll])