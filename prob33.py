'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

from heapq import heappush, heappop

class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, n):
        heappush(self.heap, n)
    def min(self):
        return self.heap[0]
    def popmin(self):
        return heappop(self.heap)
    def size(self):
        return len(self.heap)

class MaxHeap:
    '''Same as MinHeap, but negate values, to transform heapq into a max heap'''
    def __init__(self):
        self.heap = []
    def insert(self, n):
        heappush(self.heap, -n)
    def max(self):
        return -self.heap[0]
    def popmax(self):
        return -heappop(self.heap)
    def size(self):
        return len(self.heap)

def stream_medians(number_stream):
    '''O(NlgN) algorithm, since we do a handful of O(lg) operations per number'''
    left = MaxHeap()
    right = MinHeap()
    for n in number_stream:
        # insert n to the correct side
        if right.size() and n >= right.min():
            right.insert(n)
        else:
            left.insert(n)
    
        # rebalance -- make sure sizes are different by at most 1
        while left.size() >= right.size() + 2:
            right.insert(left.popmax())
        while right.size() >= left.size() + 2:
            left.insert(right.popmin())

        # yield median
        if left.size() > right.size():
            yield left.max()
        elif right.size() > left.size():
            yield right.min()
        else:
            yield (left.max() + right.min()) / 2


print(list(stream_medians([2, 1, 5, 7, 2, 0, 5])))
assert list(stream_medians([2, 1, 5, 7, 2, 0, 5])) == [2, 1.5, 2, 3.5, 2, 2, 2]
