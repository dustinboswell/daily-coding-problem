'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

'''
thoughts: what can we do with the sum of the numbers?
We can do a 2-pass maybe?
First, to compute the sum.
Then check if sum-x and sum+2x are divisble by 3?
This check might pass though if the number (x-s)
'''


def find_singleton(numbers):
    pass
