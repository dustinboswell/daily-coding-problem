"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio".
"""
import functools

s1 = s2 = s3 = ""

@functools.cache
def solve(i1, i2, i3):
    global s1, s2, s3
    if i1 == len(s1) or i2 == len(s2) or i3 == len(s3):
        return 0
    if s1[i1] == s2[i2] == s3[i3]:
        return 1 + solve(i1+1, i2+1, i3+1)
    return max(
        solve(i1+1, i2, i3),
        solve(i1, i2+1, i3),
        solve(i1, i2, i3+1),
    )

def longest_common_subsequence(a, b, c):
    global s1, s2, s3
    s1, s2, s3 = a, b, c
    return solve(0, 0, 0)

print(longest_common_subsequence("epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"))