'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

Dustin: had to look this one up "rolling max algorithm"
'''

from collections import deque

def sliding_max_slow(numbers, k):
    maxes = []
    for i in range((len(numbers)-k)+1):
        maxes.append(max(numbers[i:i+k]))
    return maxes

def sliding_max(numbers, k):
    d = deque()
    def add_tail(x):
        while d and x > d[-1]:
            d.pop()
        d.append(x)  # may be duplicate, that's ok
    def pop_head(x):
        if d and x >= d[0]:
            # only pop 1 (remember, duplicates)
            d.popleft()

    for n in numbers[0:k]:
        add_tail(n)
    yield d[0]

    for j in range(k, len(numbers)):
        add_tail(numbers[j])
        pop_head(numbers[j-k])
        yield d[0]


import collections

def add_candidate(candidates, v):
    while candidates and candidates[-1] < v:
        candidates.pop()
    candidates.append(v)

def remove_candidate(candidates, v):
    if v == candidates[0]:
        candidates.popleft()

def subarray_maxes(a, k):
    output = []
    candidates = collections.deque()

    for end in range(k):
        add_candidate(candidates, a[end])
    output.append(candidates[0])

    begin = 0
    for end in range(k, len(a)):
        remove_candidate(candidates, a[begin])
        begin += 1

        add_candidate(candidates, a[end])
        output.append(candidates[0])

    return output


def test(numbers, k):
    #print(f"Testing {numbers}, k={k}")
    assert list(sliding_max(numbers, k)) == sliding_max_slow(numbers, k)
    assert list(subarray_maxes(numbers, k)) == sliding_max_slow(numbers, k)

test([10,5,2,7,8,7], 3)
test([9,8,7,6,5,4,3,2,1], 4)
test([1,2,3,4,5,6,7,8,9], 4)

import random
for n in range(1,7):
    for k in range(1,n):
        for _ in range(100):
            numbers = [random.randint(0, n) for i in range(n)]
            test(numbers, k)
