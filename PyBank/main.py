# Need to find the data in the system

import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# Creates a blank list to be appended for counting months

monthlist=[]

# Creates a blank list to be appended for summing up

amountlist=[]

# Creates a variable to print the sum of amounts 

# Open csv file

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

# Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

    for row in csvreader: 
# Adding to lists. For amount, must convert to int due to negative values?
        monthlist.append(row[0])
        amountlist.append(int(row[1]))

# To check output lists. Needs to be commented out later
print(monthlist)
print(amountlist)

# Creates a variable to print the total count of months. 

countofmonths = len(monthlist)
totalamount = sum(amountlist)

print("Financial Analysis")
print("----------------------------------------------------------")
print(f'Total Months: {countofmonths}')
print(f'Total: ${totalamount}')



