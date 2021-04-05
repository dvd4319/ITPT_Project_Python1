# Align strings 

# assigning list values to the variables
names = ['Raj', 'Shivam', 'Shreeya', 'Kartik']
marks = [7, 9, 8, 5]
div = ['A', 'A', 'C', 'B']
id = [21, 52, 27, 38]
  
# printing Aligned Header
print(f"{'Name' : <10}{'Marks' : ^10}{'Division' : ^10}{'ID' : >5}")
  
# printing values of variables in Aligned manner
for i in range(0, 4):
    print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}")