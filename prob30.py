'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

'''
Dustin: came up with the algorithm in a minute, but took over 60 minutes to get the code out. :/
Tried/failed to generalize the two-directional code .
'''

def trapped(heights):
    if len(heights) <= 2:
        return 0

    # i/j are inclusive positions in @heights
    water = 0
    left = 0
    right = len(heights) - 1
    scan_dir = 1

    while left < right:
        # try to find a match (>= height) for left, might fail
        w = 0  # possible water
        match_found = False

        if scan_dir == 1:
            for i in range(left+1, right+1):
                if heights[i] < heights[left]:
                    w += heights[left] - heights[i]
                else:
                    match_found = True
                    water += w
                    left = i
                    break
        else:
            for i in range(right-1, left-1, -1):
                if heights[i] < heights[right]:
                    w += heights[right] - heights[i]
                else:
                    match_found = True
                    water += w
                    right = i
                    break

        if not match_found:
            scan_dir = -scan_dir

    return water

assert trapped([2,1,2]) == 1
assert trapped([2,1,2,1,2]) == 2
assert trapped([3, 0, 1, 3, 0, 5]) == 8
assert trapped([1]) == 0
assert trapped([1,1,1]) == 0
assert trapped([1,3,1]) == 0
assert trapped([3,2,1]) == 0
assert trapped([1,2,3]) == 0
assert trapped([3,2,1,2,3]) == 4
assert trapped([3,2,1,2,9]) == 4
