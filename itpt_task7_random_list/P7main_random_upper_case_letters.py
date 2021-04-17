"""
Implement and test a program to create a list of 35 random, upper case letters and
then stores the list in an array. You should then sort the list into order, A to Z, and
output the character in the middle of the list.
"""

import string
import random
import numpy


length = 35; 

def my_random_string(length):
    randomList = []
    for i in range(length):
        randomList.append(random.choice(string.ascii_uppercase));
    my_array = numpy.array(randomList)
    sortString = sorted(my_array)
    return sortString;

a = my_random_string(length)
print(a)

if (length%2 != 0):
    middle = int(length / 2)+1; # = int(2.5) = 2
else:
    middle = int(length / 2); # = int(2.5) = 2
print(middle)
print(a[middle]) 