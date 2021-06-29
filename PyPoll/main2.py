#  Need to find the data in the system

import os
import csv

csvpath = os.path.join('Resources2','election_data.csv')

# List of candidates
candidatelist = ["Khan","Correy","Li","O'Tooley"]

# Creates an empty list of voters and candidiates
voterlist = []
khanlist = []
correylist = []
lilist = []
otooleylist = []

# Open csv file

with open(csvpath) as csvfile: 

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skips header so that it doesn't count the first row for total month counted
    next(csvreader, None)

    for row in csvreader: 
        # Adding to lists
        voterlist.append(row[0])
        if row[2] == str(candidatelist[0]):
            khanlist.append(row[0]) 
        elif row[2] == str(candidatelist[1]):
            correylist.append(row[0])
        elif row[2] == str(candidatelist[2]):
            lilist.append(row[0])
        elif row[2] == str(candidatelist[3]):
            otooleylist.append(row[0])
                    
# To check output lists. Needs to be commented out later
# print(voterlist)

# Creates a variables for printing counts and percentages by each candidate
countofvoters = len(voterlist)
countofkhan = len(khanlist)
countofcorrey = len(correylist)
countofli = len(lilist)
countofotooley = len(otooleylist)

khan_percentage = "{0: .2%}".format(int(countofkhan) / int(countofvoters))
correy_percentage = "{0: .2%}".format(int(countofcorrey) / int(countofvoters))
li_percentage = "{0: .2%}".format(int(countofli) / int(countofvoters))
otooley_percentage = "{0: .2%}".format(int(countofotooley) / int(countofvoters))

# print(countofvoters)
# print(countofkhan)
# print(countofcorrey)
# print(countofli)
# print(countofotooley)

# Creates a countlist for each candidate to be compared with each other

countlist = [int(countofkhan), int(countofcorrey), int(countofli), int(countofotooley)]

if int(max(countlist)) == int(countofkhan):
    winnercandidate = candidatelist[0]
elif int(max(countlist)) == int(countofcorrey):
    winnercandidate = candidatelist[1]
elif int(max(countlist)) == int(countofli):
    winnercandidate = candidatelist[2]
elif int(max(countlist)) == int(countoftooley):
    winnercandidate = candidatelist[3]


# Prints out results 
print("Election Results")
print("----------------------------------------------------------")
print(f'Total Votes: {countofvoters}')
print("----------------------------------------------------------")
print(f'{candidatelist[0]}: {khan_percentage} ({countofkhan})')
print(f'{candidatelist[1]}: {correy_percentage} ({countofcorrey})')
print(f'{candidatelist[2]}: {li_percentage} ({countofli})')
print(f'{candidatelist[3]}: {otooley_percentage} ({countofotooley})')
print("----------------------------------------------------------")
print(f'Winner: {winnercandidate}')

