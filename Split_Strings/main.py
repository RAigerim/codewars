# Title: Split Strings
# Description:
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').

def solution(s):
    res = [s[i:i + 2] for i in range(0, len(s), 2)]
    if len(s) % 2 != 0:
        res[-1] += "_"
    return res


# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

print(solution('abc'))
print(solution('abcdef'))
