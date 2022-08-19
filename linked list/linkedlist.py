# singly linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def print(self):
        if self.head is None:
            print('list is empty')
            return
        itr = self.head
        str_itr = ''
        while itr:
            str_itr += str(itr.data) + ' >> '
            itr = itr.next
        print(str_itr)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            print('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # this stops at the element before the element we want to remove
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_data_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print('invalid index')
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        cur = self.head
        while cur:

            if count == index - 1:
                new_node = Node(data, cur.next)
                cur.next = new_node
                break
            cur = cur.next
            count += 1

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def insert_value_after(self, data_after, data_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_insert, itr.next)
                break
            itr = itr.next

    def remove_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = linked()
    ll.insert_value(['egg', 'milk', 'orange', 'beans', 'pie ', 'pepper'])
    ll.print()
    print('\n')
    ll.insert_at_beginning('fish')
    ll.print()
    ll.insert_end('butter')
    ll.print()
    ll.insert_data_at(4, 'grape')
    ll.print()
    ll.insert_value_after('orange', 'apple')
    ll.print()
    ll.remove_value('egg')
    ll.remove(4)

    ll.print()
    print('length:', ll.get_length())
