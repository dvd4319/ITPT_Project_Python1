"""
Task 9
Implement and test a program in your programming language which does the following:
    Fills an array with 20 random integers between 1 and 10.
    Prints the array contents to screen.
    Finds and displays the maximum and minimum values in the array.
    Asks the user for an integer between 1 and 10 using input validation and displays how many times it occurs in the array.
    Asks the user for an integer between 1 and 10 using input validation and display where in the array that number first occurs and indicates when it is not present.
"""

import random as rd

# Fills an array with 20 random integers between 1 and 10.
a = []
for i in range(1,20):
    a.append(rd.randint(1, 10))

# Prints the array contents to screen.
print("The array is: ")
print(a)

# Finds and displays the maximum and minimum values in the array.
max_array = print("The maximum in the array is: ", max(a))
min_array = print("The minimum in the array is: ", min(a))
# Asks the user for an integer between 1 and 10 using input validation and ....
int1 = int(input("Please insert a first integer between 1 and 10: "))
samebnumber = a.count(int1)
# .... displays how many times it occurs in the array.
print(f"The first integer {int1} apears {samebnumber} time in the array.")
# Asks the user for an integer between 1 and 10 using input validation and ...
int2 = int(input("Please insert a second integer between 1 and 10: "))

# ... display where in the array that number first occurs and indicates when it is not present.
try:
    value_index = a.index(int2)
    print(f"The position of {int2} is {value_index}.")
except:
    value_index = -1;
    print(f"The integer {int2} is not present.")









