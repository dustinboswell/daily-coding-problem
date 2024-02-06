"""
This problem was asked by LinkedIn.
Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length
string of characters in C occurs exactly once. For example, suppose C = {0, 1} and k = 3. Then our sequence should contain
the substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.
Create an algorithm that finds a De Bruijn sequence.
"""

def apply(done_set, prefix, new_char, k):
    if len(prefix) < k - 1:
        return True  # just apply it, it's fine
    new_str = prefix[len(prefix)-(k-1):] + new_char
    if new_str in done_set:
        return False  # string already exists, can't apply
    done_set.add(new_str)
    return True

def undo(done_set, prefix, k):
    if len(prefix) >= k:
        done_set.remove(prefix[-k:])  # must be there first, now we remove!

def recursive_solve(done_set, done_size, prefix, chars, k, loop_index=None):
    print(f"{done_set=}, {done_size=}, {prefix=}, {loop_index=}")
    if loop_index == k-1:
        if len(done_set) == done_size:  # this is the base-case where a solution is found.
            return prefix[0:len(prefix)-(k-1)]

    if loop_index is not None:
        c = prefix[loop_index]
        if not apply(done_set, prefix, c, k):
            return False
        new_prefix = prefix + c
        solution = recursive_solve(done_set, done_size, new_prefix, chars, k, loop_index+1)
        if solution:
            return solution
        undo(done_set, new_prefix, k)
        return False

    # try each char
    for c in chars:
        if not apply(done_set, prefix, c, k):
            continue
        new_prefix = prefix + c
        solution = recursive_solve(done_set, done_size, new_prefix, chars, k)
        if solution:
            return solution
        undo(done_set, new_prefix, k)

    # also try stopping here and closing the cyclic loop
    if len(prefix) >= 2*k:  # this could be tighter
        return recursive_solve(done_set, done_size, prefix, chars, k, 0)
    return False


def solve(chars, k):
    """Try a simple backtracking solution.  Not sure how to analyze the runtime..."""
    done_set = set()
    done_size = len(chars) ** k
    return recursive_solve(done_set, done_size, "", chars, k)

for k in [1,2,3,4,5,6]:
    print(f"{solve('01', k)=}")
