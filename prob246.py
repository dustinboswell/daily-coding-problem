'''
Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic'] can form the following circle: chair --> racket --> touch --> height --> tunic --> chair
'''

def can_chain(words):
    assert len(words) >= 2  # otherwise ambiguous

    for i in range(len(words)):
        unused_words = words[0:i] + words[i+1:]
        if try_chain(unused_words, words[i][-1], words[i][0]):
            return True

    return False

def try_chain(words, starting_letter, ending_letter):
    if len(words) == 1:
        word = words[0]
        return word[0] == starting_letter and word[-1] == ending_letter

    for i in range(len(words)):
        word = words[i]
        if word[0] != starting_letter:
            continue

        unused_words = words[0:i] + words[i+1:]
        if try_chain(unused_words, word[-1], ending_letter):
            return True

    return False

def test(words, expected_answer):
    assert can_chain(words) == expected_answer

test(['a', 'a'], True)
test(['ab', 'ba'], True)
test(['ba', 'ab'], True)
test(['ab', 'bc', 'ca'], True)
test(['chair', 'height', 'racket', 'touch', 'tunic'], True)
test(['a', 'b'], False)
