'''
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''

from collections import defaultdict

def neighbors(x, y):
    for dx in [-1,0,+1]:
        for dy in [-1,0,+1]:
            if dx or dy:
                yield (x+dx, y+dy)

def game_of_life(init_cells, num_steps):
    '''@init_cells is a list of [x,y]'''
    board = set(init_cells)

    for step in range(num_steps):
        if not board:
            print("------------ All cells dead ------------")
            break
        min_x = min(x for x,y in board)
        min_y = min(y for x,y in board)
        next_y_print = min_y
        next_x_print = min_x
        print(f'---------- Round {step} ------------------')
        for x,y in sorted(board, key=lambda item: (item[1],item[0])):
            if next_y_print < y:
                print('\n' * (y - next_y_print), end='')
                next_y_print = y
                next_x_print = min_x

            if next_x_print < x:
                print(' ' * (x - next_x_print), end='')
                next_x_print = x

            if (x,y) in board: 
                print('*', end='')
            else:
                print('.', end='')
            next_x_print += 1
        print()

        neighbor_counts = defaultdict(int)
        for x,y in board:
            for nx, ny in neighbors(x,y):
                neighbor_counts[(nx,ny)] += 1

        for (x,y), count in neighbor_counts.items():
            if (x,y) in board:
                if count < 2 or count > 3:
                    board.remove((x,y))
            else:
                if count == 3:
                    board.add((x,y))

        # also kill live cells with 0 neighbors
        for x,y in list(board):
            if neighbor_counts.get((x,y),0) == 0:
                board.remove((x,y))


game_of_life([(x,y) for x in [1,2,3,5] for y in [1,2,3,4,5]], 20)
