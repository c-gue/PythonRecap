import csv

employee = open('EmployeePay.csv','r')

employee_file = csv.reader(employee, delimiter=',')

#to skip a line if the file contains a header record
next(employee_file)         

for record in employee_file:
    bonus = int(record[3])*float(record[4])
    total = float(record[3])+bonus
    
    print(record)
        
    print('first name:',record[1])
    print('last name:',record[2])
    print('salary:',record[3])
    print('bonus:',bonus)
    print('total pay:',total)

    
    
    input()