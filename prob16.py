'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
'''

from collections import deque

class OrderLog:
    def __init__(self, N):
        self.N = N
        self.recent_orders = deque()

    def record(self, order_id):
        self.recent_orders.appendleft(order_id)
        while len(self.recent_orders) > self.N:
            self.recent_orders.pop()

    def get_last(self, i):
        assert 1 <= i <= self.N
        assert i <= len(self.recent_orders)
        return self.recent_orders[i-1]

order_log = OrderLog(3)
order_log.record('a')
assert order_log.get_last(1) == 'a'
try:
    order_log.get_last(0)
except AssertionError:
    pass
else:
    raise AssertionError("expected AssertionError, but didn't get one!")
order_log.record('b')
assert order_log.get_last(1) == 'b'
assert order_log.get_last(2) == 'a'
order_log.record('c')
assert order_log.get_last(1) == 'c'
assert order_log.get_last(2) == 'b'
assert order_log.get_last(3) == 'a'
order_log.record('d')
assert order_log.get_last(1) == 'd'
assert order_log.get_last(2) == 'c'
assert order_log.get_last(3) == 'b'
