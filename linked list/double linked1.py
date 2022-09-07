class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class doubly_linked:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("double linked list is empty")
            return

        cur = self.head
        str_itr = ' '
        while cur:
            str_itr += str(cur.data) + ' >> '
            cur = cur.next

        print(str_itr)

    def get_last_node(self):
        cur = self.head
        while cur.next:
            cur = cur.next

        return cur

    def print_backward(self):
        if self.head is None:
            return
        last_node = self.get_last_node()
        str_itr = ' '
        cur = last_node
        while cur:
            str_itr += str(cur.data) + ' >> '
            cur = cur.prev

        print("Doubly_linked list in reverse order: \n", str_itr)

    def get_length(self):
        if self.head is None:
            return
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        return count

    def insert_beginning(self, data):
        if self.head is None:
            new_node = Node(data, self.head, None)
            self.head = new_node

        else:
            new_node = Node(data, self.head, None)
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(data, None, cur)
        # next node is none ad prev is our last_node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid index")

        if index == 0:
            self.insert_beginning(data)
            return
        count = 0
        cur = self.head
        while cur:
            if count == index - 1:
                # this stop at the prev node before the
                # one we want to change
                new_node = Node(data, cur.next, cur)
                cur.next = new_node
                # creates a link between the newnode next and the newnode
                if new_node.next:
                    new_node.next.prev = new_node

                cur.next = new_node
                break
            cur = cur.next
            count += 1

    def remove_at(self, index):
        if index <= 0 or index > self.get_length():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        cur = self.head
        while cur:
            if count == index:
                cur.prev.next = cur.next
                # creates a link between our previous node and next node
                if cur.next:
                    cur.prev.next = cur.next
                    break
                cur = cur.next
                count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)


if __name__ == '__main__':
    ll = doubly_linked()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
    ll.insert_at(0, "pear")
    ll.print_forward()
    print("length of list:", ll.get_length())
    ll.remove_at(1)
