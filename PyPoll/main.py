import os
import csv

file_path = os.path.join('..', 'Resources', 'election_data.csv')

#init.ing the variables
resultDic = {}
totalCount = 0

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #reading each rows in the files
    for row in csvreader:
        totalCount += 1
        currentCandidate = row[2]
        #counting each candidate vote occurance and saving in dictionary
        if currentCandidate in resultDic:
            resultDic[currentCandidate] += 1
        else:
            resultDic[currentCandidate] = 1
#finding the winner who has the most vote
v = list(resultDic.values())
k = list(resultDic.keys())
winnerName = k[v.index(max(v))]

#printing to terminal
print("\nElection Results")
print("-------------------------")
print(f'Total Votes: {totalCount}')
print("-------------------------")
for key, value in resultDic.items():
    print(f'{key}: {round(value*100/totalCount, 3)}% ({value})')
print("-------------------------")
print(f'Winner: {winnerName}')
print("-------------------------\n")

#writing to file
newFile = open("./PyPoll/analysis/result.txt", "w")  
newFile.write("Election Results\n")
newFile.write("-------------------------\n")
newFile.write(f'Total Votes: {totalCount}\n')
newFile.write("-------------------------\n")
for key, value in resultDic.items():
    newFile.write(f'{key}: {round(value*100/totalCount, 3)}% ({value})\n')
newFile.write("-------------------------\n")
newFile.write(f'Winner: {winnerName}\n')
newFile.write("-------------------------")




