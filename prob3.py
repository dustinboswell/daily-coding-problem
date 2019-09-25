'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        '''Encode the lengths of each string, then the strings.
        E.g. "123,234,345;<val><left><right>"
        '''
        if self.left:
            left_body = self.left.serialize()
            left_body_len = len(left_body)
        else:
            left_body = ''
            left_body_len = -1

        if self.right:
            right_body = self.right.serialize()
            right_body_len = len(right_body)
        else:
            right_body = ''
            right_body_len = -1

        return f"{len(self.val)},{left_body_len},{right_body_len};{self.val}{left_body}{right_body}"

    def deserialize(self, data):
        header, body = data.split(';', 1)
        val_len, left_len, right_len = (int(x) for x in header.split(','))
        self.val = body[0:val_len]
        left_body = body[val_len:val_len+left_len]
        right_body = body[-right_len:]
        if left_len >= 0:
            self.left = Node('')
            self.left.deserialize(left_body)
        else:
            self.left = None

        if right_len >= 0:
            self.right = Node('')
            self.right.deserialize(right_body)
        else:
            self.right = None

def serialize(node):
    return node.serialize()

def deserialize(data):
    node = Node('')
    node.deserialize(data)
    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
