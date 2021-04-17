
import json
import csv

class athletes:

  
  def __init__(self, first_name, second_name, first_lap, second_lap):
    self.first_name = first_name;
    self.second_name = second_name;
    self.first_lap= first_lap;
    self.second_lap = second_lap;

  def selection(self):
      if self.first_lap < self.second_lap:
        best_score1 = self.first_lap;
        #return best_score1;
      else: 
        best_score1 = self.second_lap;
        #return best_score1; 
      atList = [self.first_name[0]+ " " + self.second_name, " ", best_score1, self.first_name, self.second_name];
      if (best_score1 < 50):
          atList[1] = "Yes";
          with open('athletes_list.csv', 'a', newline='') as al:
            writer = csv.writer(al);
            writer.writerow(atList);
            al.close();
      else: 
          atList[1] = "No";
          with open('athletes_list.csv', 'a', newline='') as al:
            writer = csv.writer(al);
            writer.writerow(atList);
            al.close();



  



