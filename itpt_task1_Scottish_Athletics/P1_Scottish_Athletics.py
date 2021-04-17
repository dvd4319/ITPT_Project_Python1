""""
Task 1
Scottish Athletics is running trials for 400 metre athletes. There are four groups of
eight athletes. The runners run two separate laps and their times are recorded as
they complete each of the two laps. Any runner who completes either of the two laps
in under 50 seconds progresses to the next stage of selection. The runner from each
of the groups with the fastest lap will receive a medal of commendation.

Your task is:
  to write a program for one of the groups of female runners
  find the runners who will progress to the next stage
  find the runner with the fastest lap
  Save this information to a file. You can assume that no two runners have the same name.

The program requires the following inputs:
  a valid number of runners
  the first and second name of each runner
  the time taken to run the first lap
  the time taken to run the second lap
  The output from the program should display the fastest runner, each runner’s name
  and indicate whether they will progress to the next stage of selection.
""" 

import csv
import operator 
import os
from athletes import athletes


my_file="athletes_list.csv"
# check if file exists 
if os.path.exists(my_file):
    os.remove(my_file)
    # Print the statement once the file is deleted  
    print("The file: {} is deleted!".format(my_file))
else:
    print("The file: {} does not exist!".format(my_file))

# the number of players is 8 
team_name = 'Wonder Woman';
gender = 'Female'
nr_runners = int(input("Please insert the number of players of the team: "))
print("------------------------------------------------------------")
print("------------------------------------------------------------")

for i in range(nr_runners):
  first_name = input(f"Insert the first name of the athlet {i+1}: ");
  second_name = input(f"Insert the second name of the athlet {i+1}: ");
  first_lap = int(input(f"Insert the result (in seconds) for the first lap of the athlet {i+1}: "));
  second_lap = int(input(f"Insert the result for the second lap of the athelt {i+1}: "));
  print("---------------------------------------------------");
  # assign the class 'athletes' to the object (instance) 'ath'
  ath = athletes(first_name, second_name, first_lap, second_lap);
  # call the method (function) 'selection' from the class 'athletes'
  ath.selection();

############## DISPLAY  #############################################
print("---------------------------------------------")
print(f"###### Situation of the Team \"{team_name}\" ({nr_runners} runners, {gender})  ##########")
# create empty lists 
name_ath = []; yes_no = []; best_score = [];first_name = [];second_name = [];
# pen and read the file: my_file="athletes_list.csv"
with open(my_file, "r") as csv_file:
    # read csv file 
    csv_reader = csv.reader(csv_file, delimiter=',');
    # In the file 'athletes_list.csv', I sort the elements on the columns in ascending order, according to column no. 2 (best score)
    sort = sorted(csv_reader, key=operator.itemgetter(2)); 
    # add the sorted items to the previously defined lists
    for row in sort:
        name_ath.append(row[0]);
        yes_no.append(row[1]);
        best_score.append(row[2]);
        first_name.append(row[3]);
        second_name.append(row[4]);

# printing Aligned Header     
print(f"Fastest lap was completed by {first_name[0]}  {second_name[0]} in {best_score[0]} seconds."); 
print(f"{'Runner Name' : ^20}{'Progresses to Next Stage' : ^20}")
# printing values of variables in Aligned manner
for i in range(len(name_ath)):
    print(f"{name_ath[i] : ^20}{yes_no[i] : ^20}")










