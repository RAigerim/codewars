# Title: Exes and Ohs
# Description:
# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.


def xo(s):
    if 'x' and 'o' not in s.lower(): return True
    x = s.lower().count('x')
    o = s.lower().count('o')
    return x == o


# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# Test Cases:

print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
