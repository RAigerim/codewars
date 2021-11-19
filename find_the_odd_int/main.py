# Title : Find the odd int
# Description:
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    c = []
    for i in seq:
        c.append(seq.count(i))
    for i in range(len(c)):
        if c[i] % 2 != 0:
            return seq[i]


# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

print(find_it([7]))
print(find_it([0]))
print(find_it([1, 1, 2]))
print(find_it([0, 1, 0, 1, 0]))
print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
