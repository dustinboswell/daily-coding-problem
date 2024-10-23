""" Daily Coding Problem #599
This problem was asked by Two Sigma.
Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word,
or creates a prefix for which there is no possible continuation, loses. Here is a sample game:
    Player 1: g
    Player 2: h
    Player 1: o
    Player 2: s
    Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.
For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
"""

def win_letters_prefix(prefix, alphabet, words, prefixes):
    """Return which letter-moves would lead to guaranteed victory."""
    winners = []
    for letter in alphabet:
        new_prefix = prefix + letter
        if new_prefix in words:
            continue  # definitely not a winning move ("first person to spell a word loses")
        if new_prefix not in prefixes:
            continue  # also not a winner (no continuation available == lose)
        if not win_letters_prefix(new_prefix, alphabet, words, prefixes):
            winners.append(letter)
    return winners

def win_letters(words):
    prefixes = {word[0:i+1] for word in words for i in range(len(word))}
    alphabet = {letter for word in words for letter in word}  # unsorted set
    alphabet = {letter: None for letter in sorted(alphabet)}  # sorted dict helps with debugging/testing
    return win_letters_prefix("", alphabet, words, prefixes)

def test_win_letters(words, expected_first_moves): 
    first_moves = win_letters(words)
    if first_moves != expected_first_moves:
        raise AssertionError(f"win_letters({words=}) returned {first_moves}, expected {expected_first_moves}")
    
if __name__ == '__main__':
    test_win_letters(["cat", "calf", "dog", "bear"], ['b', 'c'])
    test_win_letters([], [])
    print("ALL TESTS PASSED")