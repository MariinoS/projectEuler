# Project Euler: Problem 9 Source Code. By MariinoS. 7th Feb 2016.

# Task: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                                    a^2 + b^2 = c^2
#       For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#       There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#       Find the product abc.
#
# My Solution:

for a in range(1,400):      # 400 should be big enough for a I guess.
    for b in range(a,600):      # 600 should be big enough for b I guess.
        for c in range(b,800):      # 800 should be big enough for c I guess.
            if a + b + c == 1000 and a < b and b < c and a ** 2 + b ** 2 == c ** 2:
                print "a:", a
                print "b:", b
                print "c:", c
                print
                print a * b * c

# This solution works fine.
# However, it can probably go faster.
# The script finishes in 12.863s.
