"""
This problem was asked by Walmart Labs.
There are M people sitting in a row of N seats, where M < N.
Your task is to redistribute people such that there are no gaps between any of them,
while keeping overall movement to a minimum.
For example, suppose you are faced with an input of
[0, 1, 1, 0, 1, 0, 0, 0, 1],
where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the
person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute
distance each person must move, so that the cost here would be five.
Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
"""

def lowest_cost(seats):
    # First, trim off 0's from the ends
    if seats[0] == 0:
        return lowest_cost(seats[1:])
    if seats[-1] == 0:
        return lowest_cost(seats[:-1])
    # Greedy solution: see whether first vs last is easier to move.
    for dist in range(1, len(seats)):
        if seats[dist] == 0:
            seats[dist] = 1
            return dist + lowest_cost(seats[1:])
        if seats[-(dist+1)] == 0:
            seats[-(dist+1)] = 1
            return dist + lowest_cost(seats[:-1])
    return 0  # no holes, we're done!

if __name__ == '__main__':
    assert lowest_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
    assert lowest_cost([0, 0, 0, 0, 1, 0, 0, 0, 0]) == 0
    assert lowest_cost([0, 0, 0, 1, 1, 0, 0, 0, 0]) == 0
    assert lowest_cost([0, 0, 0, 1, 0, 1, 0, 0, 0]) == 1
    assert lowest_cost([1, 1, 1, 1, 0, 1, 0, 0, 0]) == 1
    assert lowest_cost([0, 0, 0, 1, 0, 1, 1, 1, 1]) == 1
    print("ALL TESTS PASSED")