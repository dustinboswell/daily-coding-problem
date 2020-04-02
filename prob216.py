"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14
"""

ROMAN_VALUES = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }

def decode_roman(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = ROMAN_VALUES[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total

def test(roman, number):
    decoded = decode_roman(roman)
    if decoded != number:
        print(f"ERROR: decode_roman({roman}) returned {decoded}, expected {number}")
        raise AssertionError()

test("", 0)
test("X", 10)
test("XX", 20)
test("XXX", 30)
test("XL", 40)
test("XLIV", 44)
test("XIV", 14)
print("ALL TESTS PASSED")
