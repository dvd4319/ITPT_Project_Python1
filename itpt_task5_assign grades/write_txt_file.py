import csv
"""
a = ['name','department','birthday month']
b = ['John Smith','Accounting','November']
c = ['Erica Meyers','IT','March']


with open("employee_birthday.txt", "a") as output:
    output.write(str(a))
"""
"""
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""
# define list of places
places_list = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in places_list)