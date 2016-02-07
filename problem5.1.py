# Project Euler: Problem 5 Source Code. By MariinoS. 7th Feb 2016.

# Task:   2520 is the smallest number that can be divided by each of the numbers
#         from 1 to 10 without any remainder.
#         What is the smallest positive number that is evenly divisible
#         by all of the numbers from 1 to 20?
#
# My Solution:

def devisible_by_range(a,b):
    c = 1           # We start testing from this value.
    smallest = c        # Inital Value
    count = 0
    while count < b - a:
        for i in range(a,b):    # All numbers c should be divisible by.
            if c % i != 0:
                c += 1
                count = 0
                break           # Restarts while loop
            else:
                count += 1
    else:           # Result found
        smallest = c
    return smallest

print devisible_by_range(1,21)

# This is a second solution I found.
# However, I think there's both something good and bad about it.
# The good part: The code looks more readable in my opinion.
# The bad part: It takes 254.007s to finish opposing to the 54.966s in my first solution.
