# Project Euler: Problem 7 Source Code. By MariinoS. 7th Feb 2016.

# Task:   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#         we can see that the 6th prime is 13.
#         What is the 10 001st prime number?
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

def nth_prime(x):
    prime = 1
    number = 1
    true = 0
    while true < x:
        if is_prime(number) == True:
            prime = number
            number += 1
            true += 1
        else:
            number += 1
    return prime

print nth_prime(10001)

# This script finishes in 126.795s.
# The answer = 104743
