'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

'''

def subset_sum(S, k):
    '''Backtracking solution.  O(2^N) worst case.  Useful for small N, but huge k'''
    if k == 0:
        return []
    elif k < 0 or not S:
        return None
    # try using S[0] ...
    subset = subset_sum(S[1:], k - S[0])
    if subset is not None:
        return S[0:1] + subset
    # try skipping S[0]
    return subset_sum(S[1:], k)

def subset_sum_dp(S, k):
    '''Dynamic Programming, kinda.  O(min(k, 2^N) * N) worst case'''
    last_element = {0:None}  # last_element[sum] is the element of S that got to sum
    for s in S:
        for sum_ in list(last_element.keys()):
            new_sum = sum_ + s
            if new_sum not in last_element and new_sum <= k:
                last_element[new_sum] = s

    if k not in last_element:
        return None
    subset = []
    while k > 0:
        subset.append(last_element[k])
        k -= last_element[k]
    return subset


for func in [subset_sum, subset_sum_dp]:
    print(sorted(func([12,1,61,5,9,2], 24)))
    assert sorted(func([12,1,61,5,9,2], 24)) == [1,2,9,12]
