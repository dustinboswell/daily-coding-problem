'''
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
'''

def find_min_max(numbers):
    '''Uses 1.5 N comparisons'''
    assert(numbers)

    lows = []
    highs = []
    if len(numbers) % 2:
        lows.append(numbers[-1])
        highs.append(numbers[-1])
        numbers = numbers[0:-1]

    # use N/2 comparisons below to separate into 2 lists of potential mins and maxes.
    for i in range(0, len(numbers), 2):
        a, b = numbers[i], numbers[i+1]
        if a <= b:
            lows.append(a)
            highs.append(b)
        else:
            highs.append(a)
            lows.append(b)

    # could use min() and max(), but let's be explicit with comparisons
    min_ = lows[0]
    for n in lows[1:]:
        if n < min_:
            min_ = n

    max_ = highs[0]
    for n in highs[1:]:
        if n > max_:
            max_ = n

    return min_, max_
