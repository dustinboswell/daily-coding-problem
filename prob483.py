'''
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
'''

def solve(n, k):
    '''Note: Returns a number from 0 to n-1.
    Implementation: given exactly n alive prisoners, execute just 1 (the kth) and recurse.'''
    if n == 1:
        return 0
    # The answer from the smaller subproblem is in the [0, n-2] range, which we re-map to our range.
    return (solve(n-1, k) + k) % n

for k in [1,2,3]:
    for n in [1,2,3,4,5,6,7,8,9,10,11,12]:
        print(f'solve({n=}, {k=}) = {solve(n,k) + 1})')  # plus-one because answer was asked base-1
