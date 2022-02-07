import csv

customer = open('customers.csv','r')

customer_file = csv.reader(customer, delimiter=',')

outfile = open('customer_country_original.csv','w')
#to skip a line if the file contains a header record
next(customer_file)         

for record in customer_file:
    outfile.write(record[1]+','+record[2]+','+record[4]+'\n')

outfile.close()