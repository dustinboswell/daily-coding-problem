'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''

from collections import namedtuple
Node = namedtuple("Tree", "left right value")

def reconstruct_tree(preorder, inorder):
    if not preorder:
        return None
    root_value = preorder[0]
    x = inorder.index(root_value)
    return Node(
            left = reconstruct_tree(preorder[1:x+1], inorder[0:x]),
            right = reconstruct_tree(preorder[x+1:], inorder[x+1:]),
            value = root_value)

root = reconstruct_tree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert root.value == 'a'
assert root.left.value == 'b'
assert root.left.left.value == 'd'
assert root.right.value == 'c'
assert root.right.right.value == 'g'
