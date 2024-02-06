'''
Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given [10, 7, 76, 415], you should return 77641510
'''

def largest_possible_int(numbers):
    return largest_possible_int_recursive(numbers, [False] * len(numbers))

def largest_possible_int_recursive(numbers, used):
    best_so_far = ""
    for i, n in enumerate(numbers):
        if used[i]:
            continue
        # try
        used[i] = True
        candidate = str(n) + largest_possible_int_recursive(numbers, used)
        used[i] = False

        if candidate > best_so_far:
            best_so_far = candidate

        if candidate[0] < best_so_far[0]:
            break  # only gets worse from here
        
    return best_so_far

def test(numbers, expected_answer):
    answer = largest_possible_int(numbers)
    if answer != expected_answer:
        print(f"largest({numbers}) got {answer} expected {expected_answer}")

test([10,7,76,415], "77641510")
test([0], "0")
test([0, 1], "10")
test([1, 0], "10")
test([1], "1")
test([1,1], "11")
test([1,22,333], "333221")
test([111,22,3], "322111")
