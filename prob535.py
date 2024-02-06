"""
This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.
"""

import random

cache = {}
def solve(N, k, max_trials=1e20):
    """This solution figures out the whole plan for what egg to drop when, which might be overkill.
    I'm guessing there is an analytical solution instead."""
    if (N,k) in cache:
        return cache[(N,k)]

    if k <= 0:
        return 0  # we've already figured out the solution (no floors to choose from)
    if N == 1:
        if k <= max_trials:
            return k  # no choice but to try each floor from smallest up, one by one.
        else:
            return 1e20  #oops not enough ready
    if N == 0:
        return 1e20  # infinity -- wasn't solved (we had floors to choose from, but no eggs)

    # What should be our first attempt with our first egg?
    best_trials = 1e20
    floor_options = list(range(k))
    random.shuffle(floor_options)
    for floor in floor_options:
        # suppose it breaks. we've now eliminated everything >= floor
        a1 = solve(N-1, floor, best_trials-1)  # there are 'floor' remaining floors < floor.
        # suppose it survives. must go higher
        a2 = solve(N, (k - floor) - 1, best_trials-1)

        trials = 1 + max(a1, a2)  # needs to handle the worst case
        if trials < best_trials:
            best_trials = trials

    cache[(N,k)] = best_trials
    return best_trials


for N in [1,2,3,5,10]:
    for k in [0, 1, 2, 5, 10, 100, 1000]:
        print(f"solve({N=}, {k=}) = {solve(N, k)}")
