# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# recursive solution -- not linear
def largest_sum_recursive(integers):
    if not integers:
        return 0
    # 2 choices, either take the first integer, or not
    return max(largest_sum_recursive(integers[1:]), integers[0] + largest_sum_recursive(integers[2:]))

# recursive solution with memoization, O(N) 
def largest_sum_memo(integers):
    cache = {}
    def largest_subsum(i):
        if i >= len(integers):
            return 0
        if i not in cache:
            cache[i] = max(largest_subsum(i+1), integers[i] + largest_subsum(i+2))
        return cache[i]
    return largest_subsum(0)

# dynamic programming solution, O(N) space
def largest_sum(integers):
    N = len(integers)
    if N == 0:
        return 0
    largest_sums = [0] * (N + 2)
    for i in range(N-1, -1, -1):
        #                     take this integer & skip      ,  or skip this integer
        largest_sums[i] = max(integers[i] + largest_sums[i+2], largest_sums[i+1])
    return largest_sums[0]

for func in [largest_sum_recursive, largest_sum_memo, largest_sum]:
    assert func([2, 4, 6, 2, 5]) == 13
    assert func([5, 1, 1, 5]) == 10
    assert func([]) == 0
    assert func([-1]) == 0
    assert func([-1, 1]) == 1
    assert func([1, -1]) == 1
