'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

def extend_palindrome_failed(word):
    '''Blah, worked on this for 2 hours, still couldn't get it to work.'''
    letters = sorted(word)
    first = 0
    last = len(word) - 1
    num_inserted = 0
    final_prefix = ''

    while first <= last:
        # reduce
        if word[first] == word[last]:
            final_prefix += word[first]
            first += 1
            last -= 1
            continue
    
        # try prepending early letters
        continue_top = False
        for c in letters:
            if c >= word[first]:
                break
            if c == word[last]:
                final_prefix += c
                last -= 1
                num_inserted += 1
                continue_top = True
                break
       
        if continue_top:
            continue

        # try appending any letter
        for c in letters:
            if c == word[first]:
                final_prefix += c
                first += 1
                num_inserted += 1
                continue_top = True
                break

        if continue_top:
            continue

        # try prepending late letters
        continue_top = False
        for c in letters:
            if c < word[first]:
                continue
            if c == word[last]:
                final_prefix += c
                last -= 1
                num_inserted += 1
                break

    print(f"word={word}, final_prefix={final_prefix}")
    #return final_prefix + final_prefix[0:-1:-1]
    if 2*len(final_prefix) == len(word):
        return final_prefix + final_prefix[::-1]
    else:
        return final_prefix + final_prefix[-2::-1]

from functools import lru_cache
@lru_cache(maxsize=None)
def extend_palindrome(word):
    '''There are at most O(N^2) unique substrings of @word, and each call
    to extend_palindrome() does O(N) marginal work, so this is O(N^3).
    '''
    if len(word) <= 1:
        return word
    if word[0] == word[-1]:
        return word[0] + extend_palindrome(word[1:-1]) + word[-1]
    a = word[-1] + extend_palindrome(word[:-1]) + word[-1]
    b = word[0] + extend_palindrome(word[1:]) + word[0]
    if (len(a), a) < (len(b), b):
        return a
    else:
        return b


assert extend_palindrome("a") == "a"
assert extend_palindrome("aa") == "aa"
assert extend_palindrome("ab") == "aba"
assert extend_palindrome("ba") == "aba"
assert extend_palindrome("aba") == "aba"
assert extend_palindrome("aab") == "baab"
assert extend_palindrome("race") == "ecarace"
assert extend_palindrome("googl") == "lgoogl"
assert extend_palindrome("google") == "elgoogle"
