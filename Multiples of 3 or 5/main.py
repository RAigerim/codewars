# Title: Multiples of 3 or 5
# Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number < 0: return 0
    sum = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0: sum += i
    return sum


print(solution(4))  # Should return 3 for n=4
print(solution(6))  # Should return 8 for n=6
print(solution(16))  # Should return 60 for n=16
