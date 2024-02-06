'''
Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.

Dustin: wait, isn't "c" a winning start letter?
Player 1: c
Player 2: a
Player 1: l [avoided 't']
Player 2: f [loses]
'''

def letters(prefix, words):
    # brute force, could use Trie instead.
    return [word[len(prefix)] for word in words if word.startswith(prefix) and len(word) > len(prefix)]

def is_winning(prefix, words):
    if prefix in words:
        return True
    next_letters = letters(prefix, words)
    if not next_letters:
        return True
    if any(not is_winning(prefix+letter, words) for letter in next_letters):
        return True
    return False

def start_letter(words):
    for letter in letters("", words):
        print(f"consider {letter}")
        if not is_winning(letter, words):
            return letter
    return None


print(start_letter(["cat", "calf", "dog", "bear"]))
