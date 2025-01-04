"""
Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"

Notes: this was a lot harder than expected.  I spent about 70 minutes on this, and still not sure if it's 100% right.
I contemplated a state machine solution, but ended up with a recursive decent parser instead.  Although less efficient,
I think it's fairly readable and adaptable.
"""

class NumberParser:
    def __init__(self, s):
        self.s = s
        self.offset = 0

    def chars_left(self):
        return len(self.s) - self.offset

    def cur_char(self):
        return self.s[self.offset]

    def is_number(self):
        """The primary external method."""
        self.consume_letter('-')  # optional sign.  Ignore return value
        if not self.consume_decimal(): return False
        if not self.chars_left(): return True

        if not self.consume_letter('e'): return False
        self.consume_letter('-')  # optional sign.  Ignore return value
        if not self.consume_integer(): return False
        if not self.chars_left(): return True

        return False  # unused letters remain

    def consume_letter(self, min_c, max_c=None):
        """Note this is the only method that actually "consumes" by incrementing self.offset.
        Every other method must eventually call this.
        """
        if not self.chars_left(): return False
        if max_c is None:
            max_c = min_c
        if min_c <= self.cur_char() <= max_c:
            self.offset += 1
            return True
        return False

    def consume_decimal(self):
        """Greedily consume a string of digits like "123" or "123.001".  No sign prefix."""
        if not self.chars_left(): return False
        if not self.consume_integer(): return False
        if self.consume_letter('.'):
            if not self.consume_digits(): return False
        return True

    def consume_integer(self):
        """Greedily consume a whole number.  Must start with non-zero."""
        if not self.chars_left(): return False
        if self.consume_letter('0'): return True  # the number zero. stop, don't consume more.
        if not self.consume_letter('1', '9'): return False
        self.consume_digits()  # optionally eat more digits, ignore return value.
        return True

    def consume_digits(self):
        if not self.chars_left(): return False
        num_consumed = 0
        while self.consume_letter('0', '9'):
            num_consumed += 1
        return num_consumed > 0


TEST_CASES = [
    ('0', True),
    ('0.0', True),
    ('0.01', True),
    ('1', True),
    ('10', True),
    ('+10', False), # plus-sign wasn't in the specification, sorry
    ('-10', True),
    ('10.1', True),
    ('-10.1', True),
    ('1e5', True),
    ('1e0', True),  # 0 exponent is ok right?
    ('-1e5', True),
    ('-1e-5', True),
    ('-1e-5.0', False),  # no decimals in the exponent
    ('-1.0e-5', True),
    ('a', False),
    (' 1', False),
    ('1 ', False),
    ('0 ', False),
    (' 0', False),
    ('e 1', False),
    ('e1', False),
    ('e -1', False),
    ('-', False),
]
def main():
    for s, is_number in TEST_CASES:
        parser = NumberParser(s)
        if is_number != parser.is_number():
            raise ValueError(f"Error: input '{s}' failed to return output {is_number}")
    print(f"ALL {len(TEST_CASES)} TESTS PASSED")

if __name__ == '__main__':
    main()
