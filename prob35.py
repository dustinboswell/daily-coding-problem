'''
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def sort_rgb(array):
    '''Not sure why this problem was marked as "hard".  By "linear-time" did they mean "one pass"?'''
    i = 0  # where to insert
    j = 0  # where to read

    for c in ['R', 'G']:
        for j in range(i, len(array)):
            if array[j] != c: continue
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
    return array

def sort_rgb_onepass(array):
    '''Ok, let's try the one-pass... Yeah, that was harder.'''
    r = 0
    b = len(array)-1
    i = 0
    def swap(x, y):
        tmp = array[x]
        array[x] = array[y]
        array[y] = tmp

    while i <= b:
        if array[i] == 'G':
            i += 1
        elif array[i] == 'R':
            swap(r, i)
            r += 1
            i += 1
        elif array[i] == 'B':
            swap(b, i)
            b -= 1
    return array

for func in [sort_rgb, sort_rgb_onepass]:
    assert func(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    assert func([]) == []
    assert func(['R']) == ['R']
    assert func(['G']) == ['G']
    assert func(['B']) == ['B']
