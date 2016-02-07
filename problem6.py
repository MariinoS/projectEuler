# Project Euler: Problem 6 Source Code. By MariinoS. 6th Feb 2016.

# Task:   The sum of the squares of the first ten natural numbers is,
#                         1^2 + 2^2 + ... + 10^2 = 385
#         The square of the sum of the first ten natural numbers is,
#                     (1 + 2 + ... + 10)^2 = 55^2 = 3025
#         Hence the difference between the sum of the squares of the first
#         ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#         Find the difference between the sum of the squares of the first one
#         hundred natural numbers and the square of the sum.
#
# My Solution:

def sum_squares(input):
    total = 0
    for i in input:
        total = total + i ** 2
    return total

def square_sum(input):
    result = sum(input) ** 2
    return result

A = sum_squares(range(1,101))
B = square_sum(range(1,101))

print B - A

# I don't think there's anything special about this source code.
# This problem was the easiest yet.
