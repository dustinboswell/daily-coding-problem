'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

"""
The simplest solution is to do 2 passes:
    - count the number of elements, N
    - advance N-K-1 steps from the head

To do this in one pass, not sure if this qualifies, but you can maintain 2 pointers, where the first is allowed to advance K steps ahead, and then keep advancing both of them in sync until the first hits the end, then you know the second pointer is K behind.
You're effectively doing 2 passes in parallel, though.
"""
