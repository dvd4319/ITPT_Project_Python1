"""
Implement and test a program to simulate a simple game. Your program should do the following:

1. Store six colours in an external file (Note: these colours can be your choice of words or graphics).
2. Create three arrays and input the colours to each of the arrays.
3. For each of the three arrays, create a random number between 1 and 6 and output that colour to the screen.
4. If two of the colours match, the user wins 50 pence.
5. If all three colours match, the user wins £1.
6. Allow the user to have five ‘shots’ and keep track of their winnings.
7. Display suitable messages on screen.
"""
#The 'csv' module implements classes to read and write tabular data in CSV format.
import csv
# The 'operator' module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y)
import operator
import os
import random 

# 1. Store six colours in an external file (Note: these colours can be your choice of words or graphics).
my_file="six_colors.csv"
# check if file exists 
if os.path.exists(my_file):
    os.remove(my_file)
    # Print the statement once the file is deleted  
    print("The file: {} is deleted!".format(my_file))
else:
    print("The file: {} does not exist!".format(my_file))

colorList = ['red', 'green', 'blue', 'yellow', 'purple', 'black']
#for i in range(len(colorList)):
with open('six_colors.csv', 'a', newline='') as cl:
    writer = csv.writer(cl);
    writer.writerow(colorList);
    cl.close();


# 2. Create three arrays and input the colours to each of the arrays.
vec1 = []; vec2 = []; vec3 = [];
with open("six_colors.csv", "r") as csv_file:
    # read csv file 
    csv_reader = csv.reader(csv_file, delimiter=',');   
    for row in csv_reader:
        for i in range(len(colorList)):
            vec1.append(row[i]);
            vec2.append(row[i]);
            vec3.append(row[i]);

# 3. For each of the three arrays, create a random number between 1 and 6 and output that colour to the screen.
#6. Allow the user to have five ‘shots’ and keep track of their winnings.
count = 5; count50 =0; count1 = 0; count0 = 0
while count > 0:
    enter1 = input(f"You have {count} tries. Press ENTER!")
    ran3 = []
    for i in range(3): ran3.append(random.randrange(1,6));
    c1 = vec1[ran3[0]]; c2 = vec2[ran3[1]]; c3 = vec3[ran3[2]];
    linie1 = "-------------------------------------------------------------------------------"
    print(linie1)
    print(c1, c2 , c3 )
    print(linie1)
    # 4. If two of the colours match, the user wins 50 pence.
    if (c1 == c2) or (c1 == c3) or (c2 == c3):
        print("You won 50 pence.")
        count50 = count50 +1
    # 5. If all three colours match, the user wins £1.
    elif (c1 == c2) and (c1 == c3) and (c2 == c3):
        print("You won £1.")
        count1 = count1 +1
    else:
        print("Try again!")
        count0 = count0 + 1
    print(linie1)
    count = count - 1 

# 7. Display suitable messages on screen.
print(f"You won 50 X {count50} = £ {(count50 * 50)/100}")
print(f"You won £1 X {count1} = £ {count1*1}")
print(f"You lost {count0} time(s) ")




