'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def first_missing(numbers):
    '''Strategy: move each number to its proper location, leaving 0's behind.
    Any unfilled 0 is a missing number.'''
    i = 0
    while i < len(numbers):
        #print(f"numbers={numbers}, i={i}")
        n = numbers[i]
        numbers[i] = 0  # devour input (saved as local variable n)
        # easy case: number is irrelevant
        if n <= 0 or n > len(numbers):
            i += 1
            continue
        # number belongs "to the left" (or at our location) -- move it there
        if n <= (i+1):
            numbers[n-1] = n
            i += 1
            continue
        # (else) number belongs "to the right" ...

        # number is a duplicate of the one to the right -- nothing to do
        if n == numbers[n-1]:
            i += 1
            continue

        # swap:
        # - move @n to it's place to the right
        # - move that displaced number here
        numbers[i] = numbers[n-1]
        numbers[n-1] = n

        # Argument for why this function is O(N):
        # each iteration of while loop either advances i, or puts
        # one more numbers[] in place.  So at most 2n iterations.

    for i in range(len(numbers)):
        if numbers[i] == 0:
            return i+1
    # else: input had all unique numbers
    return len(numbers)+1


def test_case(numbers, expected_answer):
    answer = first_missing(list(numbers))
    if answer != expected_answer:
        print(f"first_missing({numbers}) returned {answer}, expected {expected_answer}")

test_case([3,4,-1,1], 2)
test_case([1,2,0], 3)
test_case([], 1)
test_case([0], 1)
test_case([0, 0], 1)
test_case([2, 0], 1)
test_case([1], 2)
test_case([1, 2, 3], 4)
test_case([2, 1, 3], 4)
test_case([3, 1, 2], 4)
test_case([1, 1, 2, 2], 3)
