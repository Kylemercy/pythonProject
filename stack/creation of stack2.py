class stack:
    # creationof stack with limit size
    def __init__(self, maxsize):
        self.list = []
        self.maxsize = maxsize

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    # stack without limit
    def isempty(self):
        if self.list == []:
            return True
        # this returns true showing is an empty list
        else:
            return False
        # isfull

    def isfull(self):
        if len(self.list) == self.maxsize:
            print('the list is full')
            return True

        else:
            return False

    # push
    def push(self, value):
        if self.isfull():
            'the stack is full.'
        else:
            self.list.append(value)
            'The element has been successfully inserted.'

    def pop(self):
        # removes the last element that was added
        if self.isempty():
            return 'there is no element in the stack'
        else:
            return self.list.pop()

    def peek(self):
        # checks if an element still exit in the stack
        if self.isempty():
            return 'there is no element in the stack'
        else:
            return self.list[len(self.list) - 1]
            # returns the last element that was added

    def delete_list(self):
        self.list = None


custstack = stack(4)
print(custstack.isempty())
print(custstack.isfull())
custstack.push(4)
custstack.push(6)
custstack.push(7)
custstack.push(9)
print(custstack)
print(custstack.isfull())
