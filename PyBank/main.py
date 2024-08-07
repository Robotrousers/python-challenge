import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

monthly_changes = []
dates = []
greatest_increase_date = []
greatest_decrease_date = []

total_months = 0
total_profit = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
previous_profit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# The total number of months included in the dataset
    for row in csvreader:
        total_months += 1
        
#dates index
        dates.append(row[0])
  
# The net total amount of "Profit/Losses" over the entire period
        total_profit += int(row[1])

# -The changes in "Profit/Losses" over the entire period 
        current_profit = int(row[1])
        profit_change =  current_profit - previous_profit
        monthly_changes.append(profit_change)

        previous_profit = current_profit

#slice, exlude 1st
total_change=sum(monthly_changes[1:])

#and then the average of those changes
average_change = total_change / (total_months - 1)

# The greatest increase in profits (date and amount) over the entire period
greatest_increase_profits = max(monthly_changes)
greatest_increase_date = dates[monthly_changes.index(greatest_increase_profits)]

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease_profits = min(monthly_changes)
greatest_decrease_date = dates[monthly_changes.index(greatest_decrease_profits)]

analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_profits})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_profits})\n"
)
print(analysis)

with open('bank_analysis.txt', 'w') as file:
    file.write(analysis)