'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

Solution: advance 'i' and 'j' across the string.  The while loop iterates O(2N) times (each time either i or j advances).
Assuming set addition/removal/size is O(1), then the whole solution is O(N).
'''

from collections import defaultdict

def solve(s, k):
    letter_counts = defaultdict(int)
    i = 0
    j = 0
    longest = (0, 0)  # best (i,j) found so far
    while i < len(s) and j < len(s):
        #print(f"{s=}, {k=}, {letter_counts=}, {i=}, {j=}, {longest=}")
        if len(letter_counts) > k:
            letter_counts[s[i]] -= 1
            if letter_counts[s[i]] == 0:
                del letter_counts[s[i]]
            i += 1
            continue

        if (j - i) > (longest[1] - longest[0]):
            longest = (i,j)

        letter_counts[s[j]] += 1
        j += 1

    return s[longest[0]:longest[1]]

for s in ['abcba', 'aabbbcc']:
    for k in [1,2,3]:
        print(f'solve({s=}, {k=}) = {solve(s,k)}')
