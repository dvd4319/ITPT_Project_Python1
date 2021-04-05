class Student:


    def __init__ (self, highest_score, first_name, second_name, score_student):
        self.highest_score  = highest_score ;
        self.score_student = score_student;
        self.first_name = first_name;
        self.second_name = second_name; 
    
    def percent(self):
        pss = (self.score_student/100)*self.highest_score;
        return pss;

    def mark1(self, pss):
        # declare an empty string 'mark'
        mark = ' ';
        if (pss > 0 and pss < 45) :
            mark = 'E';
            return mark;
        elif (self.score_student >= 45 and  self.score_student <= 50):
            mark = 'D';
            return mark
        elif (self.score_student > 50 and  self.score_student <= 60):
            mark = 'C';
            return mark;
        elif (self.score_student > 60 and  self.score_student <= 70):
            mark = 'B';
            return mark;
        elif (self.score_student > 70 and  self.score_student <= 100):
            mark = 'A';
            return mark;
        else:
            mark = ("Please insert a score between 1 and 100.");
            return mark;

    def initials(self):
        firstName = self.first_name[0];
        secondName = self.second_name[0]; 
        # the name is written using Upper letters :) 
        FSN = firstName.upper() +secondName.upper();
        return FSN;




    


    
