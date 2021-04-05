# citit si prelucrat date 
import csv
import operator 
print("---------------------------------------------")
print("############ Class Results  ###############")
print(" ")
initials = []; mark = []; percent = []; count = 0;
with open("class_results1.csv", "r") as csv_file:
    # read csv file 
    csv_reader = csv.reader(csv_file, delimiter=',');
    # sort the terms in colommns taking in account the column with percent 
    sort = sorted(csv_reader, key=operator.itemgetter(2)); 
    for row in sort:
        #print(" ".join(row));
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
for i in range(15):
    print(f"{i+1 : <5}{initials[i] : <10}{percent[i] : ^20}{mark[i] : ^10}")
# count the number of marks 
print("---------------------------------------------")
letters = ['A', 'B', 'C', 'D', 'E']
for letter in letters: 
    print(f"Number of {letter} passes:  {mark.count(letter)}")
