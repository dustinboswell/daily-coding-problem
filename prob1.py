'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def subset_pair(numbers, k):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j == i:
                continue  # must be distinct elements
            if numbers[i] + numbers[j] == k:
                return True
    return False

def subset_pair_fast(numbers, k):
    seen = set()
    for n in numbers:
        if k-n in seen:
            return True
        seen.add(n)
    return False

assert subset_pair_fast([10, 15, 3, 7], 17)
assert not subset_pair_fast([1, 3], 2)
