import os
import csv

file_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #bypassing the column header
    next(csvreader)

#init.ing the variables
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

#reading the each rows
    for row in csvreader:
        temp = currentAmount 
        prevAmount = temp
        currentAmount = int(row[1])
        #bypassing the 1st row for changes 
        if index==0:
         currentAmount = int(row[1])
        else:
         change = currentAmount - prevAmount
         totalChange += change
         #finding the max and min changes
         if maxChange < change:
            maxChange = change
            maxChangeMonth = row[0]
         elif minChange > change:
            minChange = change
            minChangeMonth = row[0]
        totalMonths += 1
        total += int(currentAmount)
        index += 1

#printing to terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f'Total Months: {totalMonths}')
print(f'Total: ${total}')
print(f'Average Change: ${round(totalChange/(totalMonths-1),2)}')
print(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})')
print(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')

#writing to file
newFile = open("./Pybank/analysis/analysis.txt", "w")   
newFile.write("Financial Analysis\n")
newFile.write("----------------------------\n")
newFile.write(f'Total Months: {totalMonths}\n')
newFile.write(f'Total: ${total}\n')
newFile.write(f'Average Change: ${round(totalChange/(totalMonths-1),2)}\n')
newFile.write(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})\n')
newFile.write(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')
newFile.close()
