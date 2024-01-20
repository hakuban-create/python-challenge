import os
import csv

file_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    totalMonths = 0
    total = 0
    prevAmount = 0
    currentAmount = 0
    totalChange = 0
    maxChange = 0
    minChange = 0
    maxChangeMonth = ""
    minChangeMonth = ""
    index = 0

    for row in csvreader:
        temp = currentAmount 
        prevAmount = temp
        currentAmount = int(row[1])
        if index==0:
         currentAmount = int(row[1])
        else:
         change = currentAmount - prevAmount
         print(change)
         totalChange += change
         if maxChange < change:
            maxChange = change
            maxChangeMonth = row[0]
         elif minChange > change:
            minChange = change
            minChangeMonth = row[0]
        totalMonths += 1
        total += int(currentAmount)
        index += 1
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {totalMonths}')
print(f'Total: ${total}')
print(f'Average Change: ${round(totalChange/(totalMonths-1),2)}')
print(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})')
print(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')

newFile = open("./Pybank/analysis/analysis.txt", "w")   
newFile.write("Financial Analysis\n")
newFile.write("----------------------------\n")
newFile.write(f'Total Months: {totalMonths}\n')
newFile.write(f'Total: ${total}\n')
newFile.write(f'Average Change: ${round(totalChange/(totalMonths-1),2)}\n')
newFile.write(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})\n')
newFile.write(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')
newFile.close()
