# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#     0
#    / \
#   1   0
#      / \
#     1   0
#    / \
#   1   1

class Node:
    def __init__(self, value):
        '''value cannot be None'''
        self.value = value
        self.left = None
        self.right = None

    def count_univals(self):
        '''Return (num_univals, common_value_or_None)'''
        num_univals = 0
        is_unival = True  # innocent until proven guilty
        if self.left:
            n, common_value = self.left.count_univals()
            num_univals += n
            if common_value != self.value:
                is_unival = False
        if self.right:
            n, common_value = self.right.count_univals()
            num_univals += n
            if common_value != self.value:
                is_unival = False
        if is_unival:
            return num_univals+1, self.value
        else:
            return num_univals, None

def count_univals(root):
    n, common_value = root.count_univals()
    return n
    
tree = Node(0)
assert count_univals(tree) == 1
tree.left = Node(1)
tree.right = Node(0)
assert count_univals(tree) == 2
tree.right.right = Node(0)
tree.right.left = Node(1)
tree.right.left.left = Node(1)
tree.right.left.right = Node(1)
assert count_univals(tree) == 5
