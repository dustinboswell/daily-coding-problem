'''
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
'''
from itertools import permutations
import random

def can_arbitrage(exchanges, debug=False):
    '''@exchanges[a][b] is the amount of 'b' you get for 1 'a' '''
    exchanges = [list(row) for row in exchanges]  # deep copy
    N = len(exchanges)
    for repeat in range(N):
        improvement = False
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    via_b = exchanges[a][b] * exchanges[b][c]
                    if via_b > exchanges[a][c]:
                        exchanges[a][c] = via_b
                        improvement = True
        if not improvement:
            break  # typically happens after 1 or 2 repeats
    if debug:
        print(exchanges)
    return any(exchanges[a][a] > 1.0 for a in range(N))

def can_arbitrage_brute(exchanges):
    if any(exchanges[a][a] > 1.0 for a in range(len(exchanges))):
        return True  # degenerate case: self-exchange already arbitrage
    for perm in permutations(range(len(exchanges))):
        currency = 1
        prev_i = perm[0]
        # don't self-exchange, just start with another currency
        for i in perm[1:]:
            currency *= exchanges[prev_i][i]
            # would completing the loop right here be arbitrage?
            if currency * exchanges[i][perm[0]] > 1.0:
                return True
            prev_i = i
    return False

def rand_matrix(n, values=[0.5, 1.0, 1.5]):
    return [[random.choice(values) for x in range(n)] for y in range(n)]

for n in range(1, 10):
    for _ in range(10000):
        m = rand_matrix(n)
        if can_arbitrage_brute(m) != can_arbitrage(m):
            print(f"can_arbitrage_brute={can_arbitrage_brute(m)}, can_arbitrage={can_arbitrage(m, True)}")
            print(m)
            break
