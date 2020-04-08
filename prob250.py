'''A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY
may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.
'''

def solve(a, b, c):
    front_letters = {a[0], b[0], c[0]}
    assignments = {' ': 0}
    used_digits = set()

    # left-pad with spaces to make all strings same length (for convenience)
    a = " " * (len(c) - len(a)) + a
    b = " " * (len(c) - len(b)) + b

    def solve_partial(col, row, carry):
        if col < 0: return True

        if row == 2:
            required_value = assignments[a[col]] + assignments[b[col]] + carry
            if required_value >= 10:
                required_value -= 10
                next_carry = 1
            else:
                next_carry = 0
            next_row = 0
            next_col = col - 1
        else:
            required_value = None
            next_carry = carry
            next_row = row + 1
            next_col = col

        current_letter = [a,b,c][row][col]
        current_value = assignments.get(current_letter)

        if current_value is None:  # unassigned currently, so try all values...
            for value in range(10):
                if value in used_digits:
                    continue
                if required_value is not None and value != required_value:
                    continue
                if value == 0 and current_letter in front_letters:
                    continue  # e.g. can't have "0123" as a solution

                # try using this value
                assignments[current_letter] = value
                used_digits.add(value)
                if solve_partial(next_col, next_row, next_carry):
                    return True
                
                # undo this assignment
                used_digits.remove(value)
                del assignments[current_letter]
        else:
            if required_value is not None:
                if current_value != required_value:
                    return False
            return solve_partial(next_col, next_row, next_carry)

        return False

    if solve_partial(len(c)-1, 0, 0):
        return assignments
    else:
        return None


def test(a, b, c):
    solution = solve(a, b, c)
    print(solution)
    #assert solution == expected_solution

test("SEND", "MORE", "MONEY")
# {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
