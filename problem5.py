# Project Euler: Problem 5 Source Code. By Marino Soro. 6th Feb 2016.

# Task:   2520 is the smallest number that can be divided by each of the numbers
#         from 1 to 10 without any remainder.
#         What is the smallest positive number that is evenly divisible
#         by all of the numbers from 1 to 20?
#
# My Solution:

def devisible_by_range(a,b):
    c = 1           #We start testing from this value.
    smallest = c        #Inital Value
    dummy = 2               #Dummy to be able to exit the while loop.
    while dummy == 2:
        count = 0
        for i in range(a,b):    #All numbers c should be divisible by.
            if c % i == 0:
                smallest = c
                count += 1
                if count == b - a:  #If this count is reached, it means c is evenly devisible by the entire range.
                    dummy += 1      #Exits the while loop
                    break           #Exits the for loop.
            else:           #This code runs whenever c isn't evenly devisible by any number in the range.
                c += 1          #Starts checking for the next number.
                dummy = 2           #Restarts while loop.
    return smallest

print devisible_by_range(1,21)


# Hier moet echt wel een simpelere manier voor bestaan..
# Het script is werd voltooid in 55,194s.
# Dit lijkt me vrij lang.
# De code ziet er ook niet erg duidelijk uit.
# Het antwoord = 232792560
