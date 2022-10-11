import os
import csv

# Path to get data from the Resources folder:
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file:
with open(bank_csv) as csvfile:
    # Read in the bank data as a dictionary:
    bank_data = csv.DictReader(csvfile)

    # Store each column as a var:
    # First, create 2 empty lists as names for vars:
    date_bank = []
    profit_losses_bank = []
    
    for row in bank_data:
        date_bank.append(row['Date'])
        profit_losses_bank.append(int(row['Profit/Losses']))

    # Count the length of Date for total months:
    total_months = len(date_bank)

    # Add up total Profit/Losses
    total = sum(profit_losses_bank)
    

    # Print Financial Analysis
    print(f'Financial Analysis')
    print(f'----------------------------')
    # Print total months:
    print(f'Total Months: {total_months}')
    # Print total:
    print(f'Total: ${total}')
    # Print Average Change:
    # print(f'Average Change: ${}')
    # Print date and amount of Greatest Increase in Profits: 
    # print(f'Greatest Increase in Profits: {}')
    # Print date and amount of Greatest Decrease in Profits:
    # print(f'Greatest Decrease in Profits: {}')
