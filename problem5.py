# Project Euler: Problem 5 Source Code. By MariinoS. 6th Feb 2016.

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


# I get the feeling there should be an easier way to do this..
# The script finishes in 54.966s.
# I'm thinking this is rather long.
# The code looks a bit strange as well, hence the amount of comments.
# The answer = 232792560
