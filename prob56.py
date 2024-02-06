'''
Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
'''

def can_color(graph, k, colors=None):
    if colors is None:
        colors = [None] * len(graph)

    try:
        first_uncolored = colors.index(None)
    except ValueError:
        return True

    for color in range(k):
        if any(graph[first_uncolored][i] and colors[i] == color for i in range(len(graph))):
            continue

        colors[first_uncolored] = color
        if can_color(graph, k, colors):
            return True

        colors[first_uncolored] = None

    return False

assert can_color([], 1)
assert can_color([[False]], 1)
assert can_color([[True]], 1)
assert can_color([[False, False], [False, False]], 1)
assert not can_color([[False, True], [True, False]], 1)
assert can_color([[False, True], [True, False]], 2)
# TODO: better test cases
