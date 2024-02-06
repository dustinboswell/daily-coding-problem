def first_empty(board):
    for r in range(0, 9):
        for c in range(0, 9):
            if board[r][c] is None:
                return r, c
    return None, None

def solve(board, row_sets, col_sets, block_sets):
    # find first empty slot
    r, c = first_empty(board)
    if r is None:
        return True
    block = (int(r/3) * 3) + int(c/3)
    #print(f"{r}, {c}, {block}")

    for number in range(1, 10):
        # would number be legal?
        if number in row_sets[r]: continue
        if number in col_sets[c]: continue
        if number in block_sets[block]: continue

        # accept number
        board[r][c] = number
        row_sets[r].add(number)
        col_sets[c].add(number)
        block_sets[block].add(number)

        if solve(board, row_sets, col_sets, block_sets):
            return True

        # undo number
        board[r][c] = None
        row_sets[r].remove(number)
        col_sets[c].remove(number)
        block_sets[block].remove(number)

    return False

def solve_board(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    block_sets = [set() for _ in range(9)]
    for r in range(0,9):
        for c in range(0,9):
            if board[r][c] is None: continue

            block = (int(r/3) * 3) + int(c/3)
            row_sets[r].add(board[r][c])
            col_sets[c].add(board[r][c])
            block_sets[block].add(board[r][c])

    return solve(board, row_sets, col_sets, block_sets)

board = [
        [5,3,None,None,7,None,None,None,None],
        [6,None,None,1,9,5,None,None,None],
        [None,9,8,None,None,None,None,6,None],
        [8,None,None,None,6,None,None,None,3],
        [4,None,None,8,None,3,None,None,1],
        [7,None,None,None,2,None,None,None,6],
        [None,6,None,None,None,None,2,8,None],
        [None,None,None,4,1,9,None,None,5],
        [None,None,None,None,8,None,None,7,9]]
assert solve_board(board)
for row in board:
    print(row)
