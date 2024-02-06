'''
Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
'''

'''Ways to do this:
1) start with 000000 and increment on every new URL inserted
  - optional: keep a map of url->code on the side, to re-use codes if given duplicate URL
2) pick a random code each time. If code is already used, try again.  Only requires a handful
  of attempts on average, even when 80% full.
  Codes are harder to guess this way.
'''

base62 = {}
for x in range(10):
    base62[x] = chr(ord('0')+x)
for x in range(26):
    base62[10+x] = chr(ord('a')+x)
for x in range(26):
    base62[36+x] = chr(ord('A')+x)

def int_to_code(x):
    assert 0 <= x < 62**6
    code = ''
    for d in range(6):
        slot_value = int(x / (62 ** d))
        code = base62[slot_value] + code
    return code

class Shortener:
    def __init__(self):
        pass
