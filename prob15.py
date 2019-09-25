'''
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

import random
from collections import Counter

def pick_from_stream(stream):
    selected = None
    num_seen = 0
    for item in stream:
        num_seen += 1
        if random.random() <= (1 / num_seen):
            selected = item
    return selected

def test_pick_from_stream(items):
    num_repeat = 1000*1000
    counter = Counter()
    for _ in range(num_repeat):
        counter[pick_from_stream(items)] += 1
    for item, count in counter.most_common():
        expected_count = num_repeat / len(items)
        err = abs(count - expected_count) / expected_count
        assert err < 0.02

test_pick_from_stream([1])
test_pick_from_stream([1, 2])
test_pick_from_stream(list(range(10)))
