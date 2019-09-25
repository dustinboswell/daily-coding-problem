'''
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
from collections import deque 

def shortest_path(board, start, end):
    '''Return number of steps needed, or None'''
    min_steps = [[None]*len(board[0]) for _ in range(len(board))]
    min_steps[start[0]][start[1]] = 0

    frontier = deque()
    def explore(r, c, steps):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
        if board[r][c]:
            return
        if min_steps[r][c] is not None:  # already explored
            return
        min_steps[r][c] = steps
        frontier.append((r,c))

    frontier.append(start)
    while frontier and min_steps[end[0]][end[1]] is None:
        r, c = frontier.popleft()
        steps = min_steps[r][c]
        explore(r+1, c, steps+1)
        explore(r, c+1, steps+1)
        explore(r, c-1, steps+1)
        explore(r-1, c, steps+1)

    return min_steps[end[0]][end[1]]

board = [[False, False, False, False], [True, True, False, True], [False, False, False, False], [False, False, False, False]]
print(shortest_path(board, (3,0), (0,0)))
