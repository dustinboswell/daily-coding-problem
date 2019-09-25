'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random
def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        rand25 = 5 * (rand5() - 1) + (rand5() - 1)  # 0 to 24
        if rand25 < 21:
            return 1 + (rand25 % 7)
