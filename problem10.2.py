# Project Euler: Problem 10 Source Code. By MariinoS. 7th Feb 2016.

'''
# Task:   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#         Find the sum of all the primes below two million.
#
# My Solution:
'''

sieve = [True] * 2000000    # True means the index is a prime.

# We start with all values of True.
# Next, we convert True to False for the multiples of every number starting at 2

def delete_from_sieve(x):   # Removes all multiples of x from sieve
    for i in xrange(x+x, len(sieve), x):    # Only the multiples, not the nr itself. Hence the x+x
        sieve[i] = False

for i in xrange(2, int(len(sieve) * 0.5)):  # 0.5 because from the middle, there can't be any multiples of i inside range
    delete_from_sieve(i)

# Now we have a sieve without multiples of any previous number.
# This means the remaining numbers in the sieve are all prime numbers!

print sum(i for i in xrange(2, len(sieve)) if sieve[i] == True)

'''
# I took a closer look in the source code of "problem10.1.py"
# and tried to understand what was going on.
# I hadn't heard about this method before, so it was an enriching experience for me.
# Once I understood the proces, I tried to rewrite something similar myselfself.
# (Without cheating ofc.) This is what I came up with.
# I still don't understand everything. For example, why would you stop at the sqrt?
# Because I do not yet understand it, I decedid to keep checking until the middle.
# Therefore, my code needs some extra time to finish but oh well..
#
# The script finishes in 4.55s.
# The answer = 142913828922
'''
