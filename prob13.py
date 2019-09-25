'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''
def find_longest_slow(s, k):
    '''Overall this is O(N^2) due to set() inside the O(N) loop'''
    best_substr = ''
    for i in range(len(s)):
        for j in range(i+len(best_substr)+1, len(s)):
            # Note that for every iteration of (i,j) either:
            # a) best_substr gets 1 longer, or
            # b) we break (and therefore advance i)
            # So this nested for i,j loop is actually only O(2N), since a) can only happen N times, and b) can only happen N times
            if len(set(s[i:j])) <= k:
                assert j-i > len(best_substr)
                best_substr = s[i:j]
            else:
                break  # no need to explore longer suffixes
    return best_substr

def find_longest(s, k):
    i, j = 0, 0
    best_i, best_j = 0, 0
    letter_counts = {}
    while i < len(s) and j < len(s):
        # consume s[j]
        letter_counts[s[j]] = 1 + letter_counts.get(s[j], 0)
        j += 1
        if len(letter_counts) <= k:
            if j - i > best_j - best_i:
                # success! improved best
                best_i, best_j = i, j
        else:
            # failure, drop a prefix letter
            letter_counts[s[i]] -= 1
            if letter_counts[s[i]] == 0:
                del letter_counts[s[i]]
            i += 1
    return s[best_i:best_j]

assert "" == find_longest("abc", k=0)
assert "a" == find_longest("abc", k=1)
assert "bcb" == find_longest("abcba", k=2)
assert "cccdcc" == find_longest("abcccdccabc", k=2)
