'''Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class Queue:
    def __init__(self):
        self.instack = []  # oldest elements on the left/front
        self.outstack = [] # oldest elements on the right/back

    def enqueue(self, x):
        # shift everything to instack
        while self.outstack:
            self.instack.append(self.outstack.pop())
        self.instack.append(x)

    def dequeue(self):
        # shift everything to outstack
        while self.instack:
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Queue()
q.enqueue(1)
assert q.dequeue() == 1

q.enqueue(2)
q.enqueue(3)
assert q.dequeue() == 2
assert q.dequeue() == 3

q.enqueue(4)
q.enqueue(5)
assert q.dequeue() == 4
q.enqueue(6)
assert q.dequeue() == 5
assert q.dequeue() == 6
