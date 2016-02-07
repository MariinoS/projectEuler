# Project Euler: Problem 10 Source Code. By MariinoS. 7th Feb 2016.

# Task:   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#         Find the sum of all the primes below two million.
#
# My Solution:

def is_prime(x):
    if x > 1:
        for n in range(2, x):
            if x % n == 0:
                return False
                break
        else:
            return True
    else:
        return False

def sum_primes_range(x):
    total = 0
    for i in range(x):
        if is_prime(i) == True:
            total = total + i
    return total

print sum_primes_range(4000)

# This method checks every single number from 2 to 2M for primality.
# I think it should work, but saying that it takes too much time is an understatement.
# Therefore, I found another solution that has something to do with "the sieve of Eratosthenes algorithm"
# The solution can be found in "problem10.1.py".
# Since I'm not familiar with everything in the source code, I need to look
# into it before merging it with the main branch.
