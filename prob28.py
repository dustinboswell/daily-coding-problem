'''
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def make_line(words, k):
    # special-case 1 word, to avoid divide-by-0 weirdness below
    if len(words) == 1:
        return word.ljust(k)

    spaces = k - sum(len(w) for w in words)
    spaces_per_word, num_extra = divmod(spaces, len(words)-1)

    line = ''
    for i, word in enumerate(words):
        line += word
        if i < len(words)-1:
            line += ' ' * (spaces_per_word + (1 if i < num_extra else 0))
    return line

def justify(words, k):
    assert words  # otherwise, do we print a blank line or not?
    lines = []  # list of final strings to return
    line_words = []  # list of words for current line being built
    min_line_len = 0  # minimum characters required for current line
    for word in words:
        # optimistically append word, assuming there is space
        line_words.append(word)
        min_line_len += len(word)
        if len(line_words) > 1:
            min_line_len += 1  # preceeding space for new word

        # oops, line too long -- undo, print, start new line
        if min_line_len > k:
            line_words.pop()
            lines.append(make_line(line_words, k))
            line_words = [word]
            min_line_len = len(word)
    lines.append(make_line(line_words, k))
    return lines
'''
For example, given the list of words
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''
print(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))
