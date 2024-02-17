"""
This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.
"""
from functools import lru_cache

@lru_cache(maxsize=1_000_000_000)
def count_ways(top, bottom):
    """If there are @top spaces empty on the top, and @bottom on bottom, how many ways to solve from here.
    Implementation:
    Each piece placed has to contiguously fill in the gaps on the left side (any gaps left would make it unsolvable).
    """
    if top == 0 and bottom == 0:
        return 1
    if top < 0 or bottom < 0:
        return 0
    ways = 0
    ways += count_ways(top-1, bottom-1)  # vertical domino
    ways += count_ways(top-2, bottom-2)  # two horizontal dominos; this 2-piece move is combined to avoid double-counting both paths
    ways += count_ways(top-1, bottom-2)  # bottom-heavy tromino
    ways += count_ways(top-2, bottom-1)  # top-heavy tromino
    return ways

# only works up to N=400 or so, they breaks recursion limit.
# To go past that limit, either need to increase recursion limit, or rewrite code to avoid recursion.
for N in [0,1,2,3,4,5,10,20,30,40,50,100,200,300]:
    print(f"{N=} {count_ways(N, N)=}")