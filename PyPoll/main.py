#  Need to find the data in the system

import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

# Creates an empty list of voters and candidiates
candidatelist = []
voterlist = []
candidatelistindex0 = []
candidatelistindex1 = []
candidatelistindex2 = []
candidatelistindex3 = []

# Open csv file 1 to create a candidatelist with duplicates removed

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

    for row in csvreader: 
        candidatelist.append(row[2])
    
    candidatelist = list(set(candidatelist))

# Open csv file 2 to add voters to each candidate list

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

    for row in csvreader: 
        # Adding to lists
        voterlist.append(row[0])
        if row[2] == str(candidatelist[0]):
            candidatelistindex0.append(row[0]) 
        elif row[2] == str(candidatelist[1]):
            candidatelistindex1.append(row[0])
        elif row[2] == str(candidatelist[2]):
            candidatelistindex2.append(row[0])
        elif row[2] == str(candidatelist[3]):
            candidatelistindex3.append(row[0])

# Creates a variables for printing counts and percentages by each candidate
countofvoters = len(voterlist)
countofindex0 = len(candidatelistindex0)
countofindex1 = len(candidatelistindex1)
countofindex2 = len(candidatelistindex2)
countofindex3 = len(candidatelistindex3)

index0_percentage = "{0: .2%}".format(int(countofindex0) / int(countofvoters))
index1_percentage = "{0: .2%}".format(int(countofindex1) / int(countofvoters))
index2_percentage = "{0: .2%}".format(int(countofindex2) / int(countofvoters))
index3_percentage = "{0: .2%}".format(int(countofindex3) / int(countofvoters))

# print(countofvoters)
# print(countofindex0)
# print(countofindex1)
# print(countofindex2)
# print(countofindex3)

# Creates a countlist for each candidate to be compared with each other

countlist = [int(countofindex0), int(countofindex1), int(countofindex2), int(countofindex3)]

if int(max(countlist)) == int(countofindex0):
    winnercandidate = candidatelist[0]
elif int(max(countlist)) == int(countofindex1):
    winnercandidate = candidatelist[1]
elif int(max(countlist)) == int(countofindex2):
    winnercandidate = candidatelist[2]
elif int(max(countlist)) == int(countofindex3):
    winnercandidate = candidatelist[3]


# Prints out results 
print("Election Results")
print("----------------------------------------------------------")
print(f'Total Votes: {countofvoters}')
print("----------------------------------------------------------")
print(f'{candidatelist[0]}: {index0_percentage} ({countofindex0})')
print(f'{candidatelist[1]}: {index1_percentage} ({countofindex1})')
print(f'{candidatelist[2]}: {index2_percentage} ({countofindex2})')
print(f'{candidatelist[3]}: {index3_percentage} ({countofindex3})')
print("----------------------------------------------------------")
print(f'Winner: {winnercandidate}')

