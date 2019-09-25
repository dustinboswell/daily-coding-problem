'''
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

# Note that only the cheapest 3 colors are relevant for any 1 house.

def minimum_cost(costs):
    '''costs[n][k] will become the minimum cost to color the subrange of houses starting at n,
    assuming n is colored k.  We write over costs in place.
    '''
    N = len(costs)
    K = len(costs[0])
    def find_min(array, exclude_i):
        return min((array[i], i) for i in range(len(array)) if i != exclude_i)

    for n in reversed(range(N-1)):
        # Find the best 2 costs (and colors) from n+1 and beyond [O(K) work]
        min_next_cost, min_next_i = find_min(costs[n+1], None)
        min_next_cost2, min_next_i2 = find_min(costs[n+1], min_next_i)

        # Also O(K)
        for k in range(K):  # color options for this house
            if k == min_next_i:
                costs[n][k] += min_next_cost2
            else:
                costs[n][k] += min_next_cost
    return min(costs[0][k] for k in range(K))

assert 5 == minimum_cost([[1,2,3], [3,2,1], [1,1,1], [2,2,2]])
