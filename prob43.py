'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack:
    def __init__(self):
        self.values = []
        self.maxs = []

    def push(self, val):
        self.values.append(val)
        if not self.maxs:
            self.maxs.append(val)
        else:
            self.maxs.append(max(val, self.maxs[-1]))

    def pop(self):
        self.values.pop()
        self.maxs.pop()

    def max(self):
        return self.maxs[-1]

stack = Stack()
stack.push(1)
assert stack.max() == 1
stack.pop()

stack.push(3)
stack.push(2)
stack.push(4)
assert stack.max() == 4
stack.pop()
assert stack.max() == 3
stack.pop()
assert stack.max() == 3
