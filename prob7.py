'''How many ways can a string like '111' be decoded, assuming an encoding of
'a' = '1'
'b' = '2'
...
'z' = '26'
'''

from functools import lru_cache

valid_chunks = set(str(x) for x in range(1, 27))

# Recursive solution
@lru_cache(maxsize=None)
def num_decodable_recursive(msg):
    '''Assume @msg is valid'''
    if msg == '':
        return 1
    num_ways = 0
    if msg[0:1] in valid_chunks:
        num_ways += num_decodable_recursive(msg[1:])
    if len(msg) >= 2 and msg[0:2] in valid_chunks:
        num_ways += num_decodable_recursive(msg[2:])
    return num_ways

# Dynamic programming solution
def num_decodable(msg):
    if len(msg) <= 1:
        return 1
    num_ways = [0] * (len(msg) + 1)
    num_ways[-1] = 1
    num_ways[-2] = 1
    for i in range(len(msg)-2, -1, -1):
        if msg[i:i+1] in valid_chunks:
            num_ways[i] += num_ways[i+1]
        if msg[i:i+2] in valid_chunks:
            num_ways[i] += num_ways[i+2]
    return num_ways[0]

def test_case(msg, expected_ways):
    n = num_decodable(msg)
    if n != expected_ways:
        print(f"num_decodable({msg}) got {n}, expected {expected_ways}")

test_case('111', 3)
test_case('', 1)
test_case('9', 1)
print(num_decodable('1' * 1000))
