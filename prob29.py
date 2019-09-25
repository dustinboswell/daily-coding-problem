'''
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def encode(msg):
    code = ''
    prev_char = None
    count = 0

    def flush():
        nonlocal code
        if count > 0:
            code += f"{count}{prev_char}"
            
    for c in msg:
        if c == prev_char:
            count += 1
            continue

        flush()
        prev_char = c
        count = 1
   
    flush()
    return code

def decode(code):
    msg = ''
    i = 0
    while i < len(code):
        j = i
        while code[j].isdigit():
            j += 1
        msg += code[j] * int(code[i:j])
        i = j + 1
    return msg

def test(msg):
    msg_after = decode(encode(msg))
    if msg != msg_after:
        print(f"encode({msg}) = {encode(msg)}, decode(encode(msg)) = {msg_after}")
    assert msg == msg_after

test("AAAABBBCCDAA")
test("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBC")
test("")
