# Title: Unique In Order
# Description:
# Implement the function unique_in_order which takes as argument a sequence
# and returns a list of items without any elements with the same value next
# to each other and preserving the original order of elements.

def unique_in_order(iterable):
    res = []
    if len(iterable) == 0:
        return []
    res.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i - 1] != iterable[i]:
            res.append(iterable[i])
    return res


# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
