'''
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.'''

class Tree:
    def __init__(self):
        pass
    def insert(self, n):
        '''Insert @n, and return how many items are greater than n'''
        # TODO: implement balanced search tree... uhh
        pass

def count_inversions(array):
    '''Can do it in NlgN time with a balanced binary tree.'''
    tree = Tree()
    num_inversions = 0
    for n in array:
        num_inversions += tree.insert(n)
    return num_inversions
