class Student:


    def __init__ (self, highest_score, first_name, second_name, score_student):
        self.highest_score  = highest_score ;
        self.score_student = score_student;
        self.first_name = first_name;
        self.second_name = second_name; 
    
    def percent(self):
        pss = round((self.score_student/100)*self.highest_score);
        return pss;

    def mark1(self, pss):
        # declare an empty string 'mark'
        mark = ' ';
        if (pss > 0 and pss < 45) :
            mark = 'Fails';
            return mark;
        elif (pss >= 45 and  pss <= 50):
            mark = 'D';
            return mark
        elif (pss > 50 and  pss <= 60):
            mark = 'C';
            return mark;
        elif (pss > 60 and  pss <= 70):
            mark = 'B';
            return mark;
        elif (pss > 70 and  pss <= 100):
            mark = 'A';
            return mark;
        else:
            mark = ("Please insert a score between 1 and 100.");
            return mark;

    def initials(self):
        firstName = self.first_name[0];
        secondName = self.second_name[0]; 
        # the name is written using Upper letters :) 
        FSN = firstName.upper() + secondName.upper();
        return FSN;




    


    
