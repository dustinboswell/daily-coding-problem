'''
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, n):
        self.item_dict = {}  # key -> Node
        self.head_node = None
        self.tail_node = None
        self.max_size = n

    def add_node(self, node):
        '''Add to head of list'''
        if not self.tail_node:
            self.tail_node = node

        if self.head_node:
            self.head_node.prev = node

        node.prev = None
        node.next = self.head_node
        self.head_node = node

    def remove_node(self, node):
        if node.next is None:
            self.tail_node = node.prev  # might be None

        if node.prev:
            node.prev.next = node.next
        else:
            self.head_node = node.next

        if node.next:
            node.next.prev = node.prev

    def get(self, key):
        node = self.item_dict.get(key)
        if node is None:
            return None

        self.remove_node(node)
        self.add_node(node)
        return node.value

    def set(self, key, value):
        node = self.get(key)
        if node is not None:
            node.value = value
            return

        node = Node(key, value)
        self.add_node(node)
        self.item_dict[key] = node

        while len(self.item_dict) > self.max_size:
            del self.item_dict[self.tail_node.key]
            self.remove_node(self.tail_node)

lru = LRU(2)
assert lru.get('a') is None
lru.set('a', 1)
assert lru.get('a') == 1
lru.set('b', 2)
assert lru.get('a') == 1
lru.set('c', 3)
assert lru.get('a') == 1
assert lru.get('b') is None
