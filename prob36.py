'''
Given the root to a binary search tree, find the second largest node in the tree.
'''

# Dustin: I assume "largest" means "highest value" and not "largest subtree"
# (otherwise the "search" tree aspect is irrelevant).

def two_largest(node):
    if node.right:
        nodes = two_largest(node.right)
        if len(nodes) == 2:
            return nodes
        else:
            return nodes + [node]
    elif node.left:
        nodes = two_largest(node.left)
        return [node] + nodes[0:1]
    else:
        return [node]

from collections import namedtuple
Node = namedtuple("Node", "left right value")

root = Node(Node(None,None,1), Node(None,None,3), 2)
assert two_largest(root)[1].value == 2

root = Node(Node(None,None,1), Node(Node(None,None,2.5),None,3), 2)
assert two_largest(root)[1].value == 2.5

root = Node(Node(None,None,1), Node(Node(None,None,2.5),Node(None,None,3.5),3), 2)
assert two_largest(root)[1].value == 3
