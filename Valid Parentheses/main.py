# Title: Valid Parentheses
# Description: Write a function that takes a string of parentheses, and determines
# if the order of the parentheses is valid. The function should return true if the
# string is valid, and false if it's invalid.


def valid_parentheses(string):
    if len(string) == 0: return True
    s = [i for i in string if i == '(' or i == ')']
    t = [1 if i == '(' else -1 for i in s]
    count, k = 0, 0
    for i in t:
        if k < 0: return False
        k += i
    return k == 0


# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
# Furthermore, the input string may be empty and/or not contain any parentheses at all.
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
