'''Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.'''

def max_no_if(a, b):
    '''There's gotta be a better way of doing this...
    Note: this only works for positive integers.
    Hmm, what counts as a "branch"?'''
    a_ge_b = bool(a // b)
    a_lt_b = (not a_ge_b) and bool(b // a)
    # todo: finish

