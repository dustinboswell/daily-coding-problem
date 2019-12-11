"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        self.next = Node(val)
        return self.next

def intersecting_node(ll1, ll2):
    len1 = 0
    node = ll1
    while node.next:
        len1 += 1
        node = node.next

    len2 = 0
    node = ll2
    while node.next:
        len2 += 1
        node = node.next

    while len1 > len2:
        ll1 = ll1.next
        len1 -= 1
    while len2 > len1:
        ll2 = ll2.next
        len2 -= 1

    while ll1.val != ll2.val:
        ll1 = ll1.next
        ll2 = ll2.next

    return ll1.val


ll1 = Node(3)
ll1.add(7).add(8).add(10)
ll2 = Node(99)
ll2.add(1).add(8).add(10)
assert intersecting_node(ll1, ll2) == 8

def list_of_n_random(n):
    # return head, tail
    head = Node(random.random())
    node = head
    for _ in range(n-1):
        node = node.add(random.random())
    return head, node

head_common, _ = list_of_n_random(random.randint(1, 10000))
head1, tail1 = list_of_n_random(random.randint(1, 10000))
tail1.next = head_common
head2, tail2 = list_of_n_random(random.randint(1, 10000))
tail2.next = head_common

assert intersecting_node(head1, head2) == head_common.val

