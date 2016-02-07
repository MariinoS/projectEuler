# Project Euler: Problem 4 Source Code. By MariinoS. 6th Feb 2016.

# Task:   A palindromic number reads the same both ways.
#         The largest palindrome made from the product of
#         two 2-digit numbers is 9009 = 91 × 99.
#         Find the largest palindrome made from the product of two 3-digit numbers.
#
# My Solution:

def largest_palindrome(x):  # Palindrome formed by two x-digit numbers.
    largest = 1
    for a in range(10 ** (x - 1), 10 ** x):
        for b in range (10 ** (x - 1), 10 ** x):
            if str(a * b) == str(a * b)[::-1] and a * b > largest:
                largest = a * b
    return largest

print largest_palindrome(3)

# In deze functie wordt iedere berekening 2x uitgevoerd, dit is tijdverlies.
# Bijvoorbeeld,
#     als x = 3:
#     a en b varieren van 100 tot 999
#     Het product wordt telkens berekend en vergeleken.
#     Maar, 105 * 100 = 100 * 105
#     Het is dus overbodig deze berekiningen allebei uit te voeren.
#     Hoe kan dit vermeden worden?
