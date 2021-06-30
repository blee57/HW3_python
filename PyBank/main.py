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

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')

# Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

# Creates empty variables to store highest increase and the month associated 
maxdiff = 0
maxdate = 0


# For loop to go thru amountlist to find the biggest difference; as it loops, it stores a higher increase to maxdiff and compares to a difference in the next loop
for position in range(1,len(amountlist)):

    diff1 = amountlist[position] - amountlist[position-1]
    
    if diff1 > maxdiff: 
        maxdiff = diff1
        maxdate = monthlist[position]

# Creates empty variables to store greatest decrease and the month associated 
mindiff = 0
mindate = 0


# For loop to go thru amountlist to find the smallest difference; as it loops, it stores a greater decrease to mindiff and compares to a difference in the next loop
for position in range(1,len(amountlist)):

    diff2 = amountlist[position] - amountlist[position-1]
    
    if diff2 < mindiff: 
        mindiff = diff2
        mindate = monthlist[position]

# # To check output lists. Needs to be commented out later
# print(monthlist)
# print(amountlist)
# print(difflist)
# print(diffmax)
# print(diffmin)

# Creates a variable to print the total count of months. 
countofmonths = len(monthlist)
totalamount = sum(amountlist)
averagediff = round(average(difflist),2)

# Prints out results 
print("Financial Analysis")
print("----------------------------------------------------------")
print(f'Total Months: {countofmonths}')
print(f'Total: ${totalamount}')
print(f'Average Change: ${averagediff}')
print(f'Greatest Increase in Profits: {maxdate} (${maxdiff})')
print(f'Greatest Decrease in Profits: {mindate} (${mindiff})')


# Creates a file path for Analysis text file. 
textpath = os.path.join('Analysis','Analysis.txt')

# Writes the results to the textfile 
with open(textpath, 'w') as f: 
    f.write("Financial Analysis" + '\n')
    f.write("----------------------------------------------------------" + '\n')
    f.write(f'Total Months: {countofmonths}' + '\n')
    f.write(f'Total: ${totalamount}' + '\n')
    f.write(f'Average Change: ${averagediff}' + '\n')
    f.write(f'Greatest Increase in Profits: {maxdate} (${maxdiff})' + '\n')
    f.write(f'Greatest Decrease in Profits: {mindate} (${mindiff})' + '\n')

