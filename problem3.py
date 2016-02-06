# Project Euler: Problem 3 Source Code. By Marino Soro. 6th Feb 2016.

# Task:   The prime factors of 13195 are 5, 7, 13 and 29.
#         What is the largest prime factor of the number 600851475143 ?
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

def get_primes(x):
    primes = []
    if x > 1:
        for n in range (2, x):
            if is_prime(n) == True:
                primes.append(n)
        return primes

def get_primefactors(x):
    primes = get_primes(x)
    primefactors = []
    for i in primes:
        if x % i == 0 :
            primefactors.append(i)
    return primefactors

primefactors = get_primefactors(600851475143)

print primefactors[len(primefactors) - 1]

# My solution actually didn't work.
# I think it should work,
# but it needs to store too much data in memory to complete the task.
