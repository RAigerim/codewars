def find_it(seq):
    c = []
    for i in seq:
        c.append(seq.count(i))
    for i in range(len(c)):
        if c[i] % 2 != 0:
            return seq[i]