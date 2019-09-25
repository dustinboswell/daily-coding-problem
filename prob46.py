'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

def longest_sub_palindrome(s):
    '''O(N^2) solution.  Find progressively longer palidromes at each starting location.'''
    best = [1] * len(s)   # best[i] is the longest palindrome length starting at s[i]
    for length in range(2, len(s)+1):
        for i in range(len(s)+1-length):
            if s[i] == s[i+length-1] and best[i+1] >= length-2:
                best[i] = length

    max_best = max(best)
    for i in range(len(s)):
        if best[i] == max_best:
            return s[i:i+best[i]]

assert longest_sub_palindrome("aabcdcb") == "bcdcb", longest_sub_palindrome("aabcdcb")
assert longest_sub_palindrome("bananas") == "anana"
assert longest_sub_palindrome("a") == "a"
assert longest_sub_palindrome("aa") == "aa"
assert longest_sub_palindrome("ab") == "a"
assert longest_sub_palindrome("aaa") == "aaa"
assert longest_sub_palindrome("aba") == "aba"
assert longest_sub_palindrome("aaaa") == "aaaa"
assert longest_sub_palindrome("abba") == "abba"
