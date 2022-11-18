class stack:
    def __init__(self):
        self.list = []

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

    # push
    def push(self, value):
        self.list.append(value)
        return 'the element has been successfully inserted'

    # pop
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


custstack = stack()
print(custstack.isempty())
custstack.push(2)
custstack.push(3)
custstack.push(4)
custstack.push(5)
print(custstack.peek())
print(custstack.pop())
print(custstack)
