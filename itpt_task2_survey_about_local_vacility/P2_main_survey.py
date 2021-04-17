"""
Implement and test a program which will allow users to complete a survey about local
facilities. The survey has 15 questions with different possible responses — some
numerical answers and some text answers. Only one response is possible for each
question. Every question has an option of ‘Do not know’. You should use a record
structure to store details of the survey questions. There should also be an option in
the program to calculate the total number of ‘Do not know’ responses.
You should test the program with five users.
""" 
import csv
import os

print("Edinburgh Council would like your views on their facilities, please spare some time to complete this questionnaire.")
number_of_users=int(input("how many users?: "))
print("you have to fill this form",number_of_users,"times")
############################################################################################################################################
#list of question in my survey
questions_list1 = ["Do you use sport pitches in the borough?",
                  "How would you rate the quality of the pitches you use? ",
                  "Please tell us which pitch or pitches you visit in the borough?",
                  "How would you rate the quality of the facilities for the pitches you use?",
                  "How often do you make use of the facilities?",
                  "When looking at the number of sport facilities to hire from the Council, how do you rate the number available?",
                  "What additional indoor or outdoor sports facilities would you like the Council to provide?",
                  "What improvements would you like to see in the sports facilities that you use? (please also name the facility)",
                  "What are the main problems you face when using a sports facility provided by the Council?",
                  "The Council is considering the introduction of an on-line booking system for sports facility bookings, which would mean all bookings of sports facilities and associated payments (via paypal or similar) would be done on-line. \n Do you believe this would cause any problems in booking sports facilities for your league / team?",
                  "How much are you charged for pitch hire currently?",
                  "Edinburgh Council is currently reviewing pricing for pitch use. In order to make pitches and facilities sustainable for the future the Council will have to make decisions regarding cuts in service, or fees to cover maintenance. \n With this in mind, do you expect prices to increase?",
                  "In order to ensure the future of local facilities is this acceptable?  ",
                  "Are you male or female?",
                  "Age?"]
# The questions in the list are numbered              
length = len(questions_list1)
questions_list = [None]*length
for i in range(length):
    questions_list[i] = str(i+1) + ". " + questions_list1[i]

###################################################################################################################################################
# Dictionary of options for each of those questions
q1 = q10 = q12 = q13 = {"A":"Yes", "B":"No", "C" : "Don't know"}
q3 = q7 = q8 = q9 = q11 = {"X":"X"}
q2 = q4 =  {"A": "Excellent", "B" : "Good", "C" : "Average", "D" : "Poor", "E" : "Very Poor", "F" : "Don't know"}
q5 = {"A": "More than once a week", "B" : "Weekly", "C" : "Monthly", "D" : "Don't know"}
q6 = {"A" : "Too many ", "B" : "The right number", "C" : "Too few", "D" : "Don't know"}
q14 = {"A": "Male", "B" : "Female", "C": "Don't know"}
q15 = {"A" : " Under 15",  "B" : "16 - 20", "C" : "21 - 30" , "D" : "31 - 40", "E" : "41 - 50", "F" : "51 - 60", "G" :"60+", "H":"Don't know"}

answers_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]
################################################################################################################################################
users = 1;
while users <= number_of_users: 
    ##########################################################################################################################################
    # delate old file 
    my_file="User_" + str(users) + "_survey_results.csv"
    # check if file exists 
    if os.path.exists(my_file):
        os.remove(my_file)
        # Print the statement once the file is deleted  
        print("The file: {} is deleted!".format(my_file))
    else:
        print("The file: {} does not exist!".format(my_file))
    ##############################################################################################################################################
    count1 = count2 = 0
    # Make pare of (questions_list1,answers_list)  = (i,j)
    for i, j in zip(questions_list,range(len(answers_list))):
        flag = False 
        # from the list "answers_list" print the question on the position i
        print(i)
        for k in  answers_list[j]:
            if answers_list[j][k] != "X":
                print(k + ") " + answers_list[j][k])
            else:
                val = answers_list[j].get(input("Please insert letter X for \'Don't know\' or press \"Enter\" to insert your tex: "))
                flag = True 
                if val == "X":
                    val = "Don't know"
                    count1 = count1 +1
                else:
                    val = input("Insert your text: ")
        if flag == False:
            val = answers_list[j].get( input("Please make Your choise: "))
            if val == "Don't know":
                count2 = count2 +1
        lista = [i, val]
        with open(my_file, 'a', newline='') as stdl:
            writer = csv.writer(stdl);
            writer.writerow(lista);
            stdl.close();
        print("-------------------")
    #############################################################################################################################################
    print("The number of \"Don't know\" is: ", count1+count2)
    count_list = ["The number of \"Don't know\" is: ",  count1+count2]
    with open(my_file, 'a', newline='') as stdl:
        writer = csv.writer(stdl);
        writer.writerow(count_list);
        stdl.close();
    ##############################################################################################################################################
    users = users + 1


