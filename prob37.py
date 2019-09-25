'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

def power_set(items):
    if not items:
        return [[]]
    ps = power_set(items[1:])
    return ps + [[items[0]] + s for s in ps]

assert sorted(power_set([1,2,3])) == sorted([[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]])
