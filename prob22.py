'''
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


Q) can you only use each set word once?, or can they be re-used?
Q) what runtime are they looking for?
Say N is the length of msg, K is the number of words in the set.
'''

def decode_msg(msg, words):
    '''@msg is a string
    @words is a list of (possibly-duplicate) words to be used in composing msg.
    Backtracking solution... unclear what the runtime is, but at least O(NK) .
    '''
    if not msg:
        return []

    solution = []
    for i, word in enumerate(words):
        if word is None:
            continue
        if not msg.startswith(word):
            continue  # word doesn't help

        solution.append(word)
        words[i] = None
        remaining_solution = decode_msg(msg[len(word):], words)
        if remaining_solution is not None:
            return solution + remaining_solution

        words[i] = word
        solution.pop()

print(decode_msg("thequickbrownfox", ["quick", "brown", "the", "fox"]))
print(decode_msg("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]))
print(decode_msg("zzz", ["bed", "bath", "bedbath", "and", "beyond"]))
