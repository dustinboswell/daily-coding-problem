'''
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

'''
Thoughts:
a*abc, 'aaabc'
-> greedy doesn't work,
-> non-greedy doesn't work either
-> will this require backtracking?
-> isn't there a O(N) way to do all this?

Consider
a*aaaaaaaaaa,
aaaaaaaaaaaaaa
How can you avoid N^2 behavior here?
'''

def re_match(s, regex):
    re_pieces = []
    i = 0
    while i < len(regex):
        assert regex[i] != '*'  # malformed
        if i+1 < len(regex) and regex[i+1] == '*':
            re_pieces.append(regex[i:i+2])
            i += 2
        else:
            re_pieces.append(regex[i])
            i += 1
    return re_match_pieces(s, re_pieces)

def re_match_pieces(s, pieces):
    '''Runtime is horrible, lots of copies and backtracking.'''
    if not pieces:
        return s == ''

    piece = pieces[0]
    if len(piece) == 2:  # e.g ".*" or "a*"
        for i in range(len(s)):
            if re_match_pieces(s[i:], pieces[1:]):
                return True
            if piece[0] != '.' and s[i] != piece[0]:
                break  # can no longer consume
        return False

    # else len(piece) == 1
    if piece[0] != '.' and s[0] != piece[0]:
        return False  # failed to consume 1 char

    return re_match_pieces(s[1:], pieces[1:])

assert re_match("aaabc", "a*abc")
assert re_match("ray", "ra.")
assert not re_match("raymond", "ra.")
assert re_match("chat", ".*at")
assert not re_match("chats", ".*at")
