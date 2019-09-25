'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

def max_sum_subarray_brute(array):
    return max(sum(array[i:j]) for i in range(len(array)) for j in range(len(array)+1)) if array else 0

def max_sum_subarray(array):
    '''Took me 20 minutes to figure this out...'''
    best_sum = 0  # best sum ever seen
    best_sum_with_last = 0  # best sum ever seen, utilizing the latest element
    for n in array:
        best_sum_with_last = max(n, best_sum_with_last + n)  # max(start fresh, extend)
        best_sum = max(best_sum, best_sum_with_last)
    return best_sum

import random
for n in range(10):
    for repeat in range(10000):
        array = [random.randint(-10,10) for _ in range(n)]
        assert max_sum_subarray(array) == max_sum_subarray_brute(array), (max_sum_subarray(array), max_sum_subarray_brute(array))

assert max_sum_subarray([34, -50, 42, 14, -5, 86]) == 137
assert max_sum_subarray([-1, -2]) == 0
