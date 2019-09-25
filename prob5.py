def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    '''pair is a callable, taking a callable f, that will be called on (a,b)'''
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def second(a, b):
        return b
    return pair(second)

assert 3 == car(cons(3, 4))
assert 4 == cdr(cons(3, 4))
