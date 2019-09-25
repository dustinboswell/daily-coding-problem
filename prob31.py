'''
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

def edit_dist(X, Y):
    '''This is the grungy C++-efficient dynamic programming solution.'''
    Xn, Yn = len(X), len(Y)
    # dist[x][y] will be == edit_dist(X[x:], Y[y:])
    dist = [[Xn+Yn] * (Yn + 1) for _ in range(Xn+1)]
    dist[Xn][Yn] = 0
    for y in reversed(range(Yn+1)):
        for x in reversed(range(Xn+1)):
            if x > 0 and y > 0:
                if X[x-1] == Y[y-1]:
                    dist[x-1][y-1] = min(dist[x-1][y-1], dist[x][y])
                else:
                    dist[x-1][y-1] = min(dist[x-1][y-1], dist[x][y]+1)
            if x > 0:
                dist[x-1][y] = min(dist[x-1][y], dist[x][y]+1)
            if y > 0:
                dist[x][y-1] = min(dist[x][y-1], dist[x][y]+1)

    return dist[0][0]

def edit_dist2(X, Y):
    '''Same as edit_dist() but go forward instead of backward.'''
    Xn, Yn = len(X), len(Y)
    dist = [[Xn+Yn] * (Yn + 1) for _ in range(Xn+1)]
    dist[0][0] = 0
    for y in range(Yn+1):
        for x in range(Xn+1):
            if x < Xn and y < Yn:
                if X[x] == Y[y]:
                    dist[x+1][y+1] = min(dist[x+1][y+1], dist[x][y])
                else:
                    dist[x+1][y+1] = min(dist[x+1][y+1], dist[x][y]+1)
            if x < Xn:
                dist[x+1][y] = min(dist[x+1][y], dist[x][y]+1)
            if y < Yn:
                dist[x][y+1] = min(dist[x][y+1], dist[x][y]+1)

    return dist[Xn][Yn]

for func in [edit_dist, edit_dist2]:
    assert func("kitten", "sitting") == 3
    assert func("", "") == 0
    assert func("a", "a") == 0
    assert func("a", "b") == 1
    assert func("aa", "bb") == 2
    assert func("aa", "aabb") == 2
