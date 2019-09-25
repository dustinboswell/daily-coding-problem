'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def product_without(numbers):
    '''Fast, but uses division.'''
    assert len(numbers) >= 2
    product = 1
    for n in numbers:
        assert n >= 1
        product *= n
    return [product / n for n in numbers]

def product_without_brute(numbers):
    '''Brute force, used for unit testing.'''
    result = []
    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if j == i:
                continue
            product *= numbers[j]
        result.append(product)
    return result

def product_without_fast(numbers):
    '''E.g. if numbers is [2,3,4],
    product_up_until    = [1,  2,  6, 24]
    product_starting_at = [24, 12, 4, 1]
    '''
    product_up_until = [1]
    for n in numbers:
        product_up_until.append(n * product_up_until[-1])

    product_starting_at = [1]
    for n in reversed(numbers):
        product_starting_at.append(n * product_starting_at[-1])
    product_starting_at = product_starting_at[::-1]

    return [product_up_until[i] * product_starting_at[i+1] for i in range(len(numbers))]

def test_same(numbers):
    assert product_without_brute(numbers) == product_without_fast(numbers)

test_same([1,2,3,4,5])
test_same([2,2,0,2,2])
