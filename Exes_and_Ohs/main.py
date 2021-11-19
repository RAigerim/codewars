def xo(s):
    if 'x' and 'o' not in s.lower(): return True
    x = s.lower().count('x')
    o = s.lower().count('o')
    return x == o