from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    # this makes our node printable


class Linkedlist:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    # to make our list iterable
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '-> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    # create a method that adds element to the end of the list
    def add_end(self, value):
        if self.head is None:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        # this help generates a random linked list
        # number of element in list
        self.head = None
        self.tail = None
        for i in range(n):
            self.add_end(randint(min_value, max_value))
        return self


createll = Linkedlist()
createll.generate(10, 0, 100)
print(createll)
print(len(createll))