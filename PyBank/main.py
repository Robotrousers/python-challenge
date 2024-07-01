import csv
from pathlib import Path
from statistics import mean

# CSV filepath
csv_path = Path("Resources/budget_data.csv")

# Read CSV file
with open(csv_path, mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# The total number of months included in the dataset
dates = [row['Date'] for row in data]
total_months = len(set(dates))

# The net total amount of "Profit/Losses" over the entire period
profit_losses = [int(row['Profit/Losses']) for row in data]
net_total = sum(profit_losses)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]

# The greatest increase in profits (date and amount) over the entire period
greatest_increase_amount = max(changes)
greatest_increase_index = changes.index(greatest_increase_amount) + 1
greatest_increase_date = data[greatest_increase_index]['Date']

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease_amount = min(changes)
greatest_decrease_index = changes.index(greatest_decrease_amount) + 1
greatest_decrease_date = data[greatest_decrease_index]['Date']

# Average of those changes
average_change = mean(changes)

# Making the analysis fit the instruction example
analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n"
)

# Export the analysis to .txt
with open('bank_analysis.txt', 'w') as file:
    file.write(analysis)

print(analysis)
