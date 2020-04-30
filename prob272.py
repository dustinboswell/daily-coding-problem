'''
Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def throw_dict(N, faces, total):
    if total > N * faces:
        return 0
    if total < N:
        return 0
    if N == 0:
        return 1
    return sum(throw_dict(N-1, faces, total - x) for x in range(1, faces+1))

assert throw_dict(3, 6, 7) == 15
