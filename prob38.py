'''
The N queens puzzle is the classic backtracking problem. The question is this:

You have an N by N board. Write a function that returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
'''

def num_arrangements(N, col, occupied_rows, occupied_diag_ups, occupied_diag_downs):
    '''rows_assigned is either 0 to N-1, or -1 to mean "unasigned"
    @col is the first queen that needs assignment
    return 0 if no arrangements can be made.
    '''
    if col == N:
        return 1

    good_arrangements = 0
    for row in range(N):
        if row in occupied_rows:
            continue

        diag_up = col - row
        if diag_up in occupied_diag_ups:
            continue

        diag_down = col + row
        if diag_down in occupied_diag_downs:
            continue

        occupied_rows.add(row)
        occupied_diag_ups.add(diag_up)
        occupied_diag_downs.add(diag_down)

        good_arrangements += num_arrangements(N, col+1, occupied_rows, occupied_diag_ups, occupied_diag_downs)

        occupied_rows.remove(row)
        occupied_diag_ups.remove(diag_up)
        occupied_diag_downs.remove(diag_down)

    return good_arrangements

print(num_arrangements(8, 0, set(), set(), set()))
