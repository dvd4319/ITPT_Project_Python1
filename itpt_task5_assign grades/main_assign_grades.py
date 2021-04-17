"""
Task 5
Implement and test a program to assign grades to exam marks for a class of 15
students, using the following criteria:
    more than 70% is an A
    more than 60% is a B
    over 50% is a C
    more than 45% is a D
    less than 45% is a fail
The program requires the highest possible score for an exam, each student’s name
(first name and surname) and each student’s mark.
The program should then:
    calculate the percentage mark for each student
    sort the percentages into order from highest to lowest
    display each student’s initials, percentage and grade in the sorted order
    display the total numbers of As, Bs, Cs, Ds and fails
""" 
#The 'csv' module implements classes to read and write tabular data in CSV format.
import csv
# The 'operator' module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y)
import operator
import os
# From module 'Student.py' import the class 'Student'
from Student import Student

# delate old file 
my_file="class_results.csv"
# check if file exists 
if os.path.exists(my_file):
    os.remove(my_file)
    # Print the statement once the file is deleted  
    print("The file: {} is deleted!".format(my_file))
else:
    print("The file: {} does not exist!".format(my_file))

#
number_students = int(input("Please insert the number of students: ")); 
highest_score = int(input("Please insert the highest possible score for the exam: "))
print("-----------------------------------------")


for i in range(number_students):
    first_name = input(f"First Name of student {i+1}: ");
    second_name = input(f"Second_Name of student {i+1}: ");
    score_student = float(input(f"Pleae insert the score of the student {i+1}: "));
    print("---------------------------------------")
    # I assign the class 'Student' to the object 'Std' 
    Std =  Student(highest_score, first_name, second_name, score_student);
    studentInitials = Std.initials() # I call the method 'initials' from the class 'Student'
    studentScore = str(Std.percent()) + "%" # I call the method 'percent' from the class 'Student'
    studentMark= Std.mark1(Std.percent()) # I call the method 'mark' from the class 'Student'
    stdList = [studentInitials, " " ,studentScore, " " ,studentMark];
    with open('class_results.csv', 'a', newline='') as stdl:
        writer = csv.writer(stdl);
        writer.writerow(stdList);
        stdl.close();

############## DISPLAY RESULTS ################################################################

print("---------------------------------------------")
print("############ Class Results  ###############")
initials = []; mark = []; percent = []; 
with open("class_results.csv", "r") as csv_file:
    # read csv file 
    csv_reader = csv.reader(csv_file, delimiter=',');
    # sort the terms in colommns taking in account the column with percent 
    sort = sorted(csv_reader, key=operator.itemgetter(2)); 
    for row in sort:
        initials.append(row[0]);
        percent.append(row[2]);
        mark.append(row[4]);

# we invert the vector, in descending order      
initials = initials[::-1] 
percent = percent[::-1]
mark = mark[::-1]           
# printing Aligned Header        
print(f"{'crt' : <5}{'Initials' : <10}{'Percentage' : ^20}{'Marks' : ^10}")
# printing values of variables in Aligned manner
for i in range(number_students):
    print(f"{i+1 : <5}{initials[i] : <10}{percent[i] : ^20}{mark[i] : ^10}")
# count the number of marks 
print("---------------------------------------------")
letters = ['A', 'B', 'C', 'D', 'Fails']
for letter in letters: 
    print(f"Number of {letter} passes:  {mark.count(letter)}")

        






