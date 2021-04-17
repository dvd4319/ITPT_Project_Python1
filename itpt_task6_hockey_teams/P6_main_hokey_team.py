"""
Task 6
Implement and test a program to calculate the number of points gained by five hockey teams, 
given the number of wins, draws and lost games, assuming:
    a win is worth 3 points, 
    a draw 1 point, 
    and no points for a lost game.
You should create your own test data and output the results on screen, in a suitable format.
# for  the teams insert the data A = [3,1,0,1,3,3,1,1,0,3] (it is an example )
"""
import numpy as np
import roman 

# the names of the teams 
Teams = ["1. Berlin", "2. Bucharest", "3. London", "4. Paris", "5. Moscow"];
#Teams = ['T1', 'T2', 'T3', 'T4', 'T5']; # variant for teams 
# length of list 'Teams'
lungime = len(Teams);
# Square matrix (in this case 5x5), combination of 
M = np.array( [ [None] * lungime]*lungime);
my_list1 = [3,1,0,1,3,3,1,1,0,3]; # Team: 1,1,1,1,2,2,2,3,3,4
u = 0
linia1 = "-------------------------------------------------------------------------------------"
############################################################################################################
# insert the 10 values from 'my_list' in the matrix M_{5x5} above the main column (superior triangle) 
for n in range(lungime):
    for m in range(lungime):
        if m != n and n < m:
             # in the matrix M : fill the 'triagnle' above the main diagonal
            M[n][m] = my_list1[u];
            u = u + 1;
##########################################################################################################
my_list2 =[]
for i in range(lungime):
    for j in range(lungime):
        if i != j and i < j:
            # in the matrix M : fill the 'triagnle' under the main diagonal 
            if   M[i][j] == 0:  M[j][i] = 3; 
            elif M[i][j] == 1:  M[j][i] = M[i][j]; 
            elif M[i][j] == 3:  M[j][i] = 0; 
            #values under main diagonal inserted in the list 'my_list2' 
            my_list2.append(M[j][i])
##################################################################################################################
# Display the first table 
print(linia1 )
print(f"{'Table 1. Combination of teams' : ^80}"); print(linia1 )
print(f"{'3 for won, 1 for draw, 0 for lose': ^80}"); print(linia1 )
print(f"{'|' : <5}{'Crt.' : <10}{'|' : <5}{'Team 1': <20}{'|' : <5}{'Team 2' : <15}{'|' : ^1}{'Score T1': ^10}{'|' : ^1}{'Score T2': ^10}{'|' : ^1}"); print(linia1 )
u = 0; team1 = []; team2 = [];
for n in range(lungime):
    for m in range(lungime):
        if m != n and n < m:
            # the sign "<" align to the left and the sign "^" align in the middle of the column 
            print(f"{'|' : <5}{roman.toRoman(u+1) : <10}{'|' : <5}{Teams[n]: <20}{'|' : <5}{Teams[m] : <15}{'|' : ^1}{my_list1[u] : ^10}{'|' : ^1}{my_list2[u] : ^10}{'|' : ^1}")
            team1.append(Teams[n]); team2.append(Teams[m])
            u = u + 1
###################################################################################################################
# Display the second table 
print(linia1)
linia2 = "----------------------------------------------"
print(linia2)
print(f"{'|' : <5}{'Table 2. Score for each team' : ^35}{'|' : ^11}"); print(linia2)
print(f"{'|' : <5}{'Team': ^15}{'|' : <5}{'Total Points': ^20}{'|' : <5}"); print(linia2)

for k in range(lungime): M[k][k] = 0;
Mrow = [None]*5;  Mcol = [None]*5;  Mtotal = [None]*5; 
for s in range(lungime):
    Mrow[s] = np.sum(M[s,:]); Mcol[s] = np.sum(M[:,s]);
    team = Teams[s];
    print(f"{'|' : <5}{team : <15}{'|' : <5}{Mrow[s]: ^20}{'|' : <5}");
print(linia2)
##########################################################################################################################
