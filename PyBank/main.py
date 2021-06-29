# Need to find the data in the system

import os
import csv

from statistics import mean

def average(l):
    avg = mean(l)
    return avg

csvpath = os.path.join('Resources','budget_data.csv')

# Creates a blank list to be appended for counting months

monthlist=[]

# Creates a blank list to be appended for summing up

amountlist=[]

# Creates an empty list to store differences between months

difflist=[]

# Creates a vairable to calculate differences between months
diffchange = 0
pmonthamount = 0

# Open csv file

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

# Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

    for row in csvreader: 
# Adding to lists. For amount, must convert to int due to ///NEGATIVE VALUES///?
        monthlist.append(row[0])
        amountlist.append(int(row[1]))
        diffchange = int(row[1])-pmonthamount
        difflist.append(int(diffchange))
        # To store an amount of for next loop
        pmonthamount = int(row[1])

# Removes the object at the index 0 to get ride of the difference that should not be in the list
difflist.pop(0)

# Stores values for maximum and minimum from difflist 
diffmax = max(difflist)
diffmin = min(difflist)

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

# Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

#for loop to lookup dates against the min and max differences 
    for row in csvreader: 
            if row[1] == diffmax:
                print(row[0])
            
# To check output lists. Needs to be commented out later
print(monthlist)
print(amountlist)
print(difflist)
print(diffmax)
print(diffmin)


# Creates a variable to print the total count of months. 
countofmonths = len(monthlist)
totalamount = sum(amountlist)
averagediff = average(difflist)


# Prints out results 
print("Financial Analysis")
print("----------------------------------------------------------")
print(f'Total Months: {countofmonths}')
print(f'Total: ${totalamount}')
print(f'Average Change: ${averagediff}')

textpath = os.path.join('Analysis','Analysis.txt')

with open(textpath, 'w') as f: 
    f.write("Financial Analysis" + '\n')
    f.write("----------------------------------------------------------" + '\n')
    f.write(f'Total Months: {countofmonths}' + '\n')
    f.write(f'Total: ${totalamount}' + '\n')
    f.write(f'Average Change: ${averagediff}' + '\n')
    
