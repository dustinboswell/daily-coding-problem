'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def is_balanced(parens):
    '''Assume each char in parens is from the 6 list below'''
    stack = []
    open_to_close = { '(': ')', '[': ']', '{': '}'}
    for c in parens:
        if c in open_to_close:
            stack.append(c)
        elif not stack:
            return False  # close with no stack left
        elif c != open_to_close[stack[-1]]:
            return False  # close with no matching open
        else:
            stack.pop()
    return not stack  # stack should be empty

assert is_balanced("([])[]({})")
assert not is_balanced("([)]")
assert not is_balanced("((()")
assert is_balanced("")
assert is_balanced("([{()[]{}}])")
assert not is_balanced("(")
assert not is_balanced(")")
