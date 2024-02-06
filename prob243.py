'''Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].
'''

def min_partition_sum(N, k):
    assert k >= 1
    if k == 1:
        return sum(N)

    assert len(N) >= k
    if len(N) == k:
        return max(N)

    best_sum = None
    for i in range(1, (len(N) - k) + 1):
        cur_sum = max(sum(N[0:i]), min_partition_sum(N[i:], k-1))
        if best_sum is None or cur_sum < best_sum:
            best_sum = cur_sum

    return best_sum

def test(N, k, expected_answer):
    min_sum = min_partition_sum(N, k)
    if min_sum != expected_answer:
        print(f"min_partition_sum({N}, {k}) got {min_sum}, expected {expected_answer}")
    # TODO: write an alternate implementation (brute force all combinations?) and compare answers

test([5,1,2,7,3,4], 3, 8)
test([5], 1, 5)
test([5, 6], 1, 11)
test([5, 6], 1, 11)
