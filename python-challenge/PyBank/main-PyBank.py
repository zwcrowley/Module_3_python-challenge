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
    # Create an empty list to save changes in :
    changes_profit_losses = []

    # Iterate over bank_data and store the colums as lists:
    for row in bank_data:
        date_bank.append(row['Date']) 
        profit_losses_bank.append(int(row['Profit/Losses']))
        
    # Iterate over profit_losses_bank and subtract each row in the list from the one before it, skipping the first row of the list:
    for row in range(1,len(profit_losses_bank)):
        changes_profit_losses.append(int(profit_losses_bank[row]-profit_losses_bank[row-1])) 
    
    # Count the length of Date for total months:
    total_months = len(date_bank)

    # Add up total Profit/Losses
    total = sum(profit_losses_bank)

    # Create the average of the changes in profits/losses list:
    ave_change = round(sum(changes_profit_losses)/len(changes_profit_losses), 2)

    # Find the max of change_profit_losses:
    max_changes = max(changes_profit_losses)

    # Find the min of change_profit_losses:
    min_changes = min(changes_profit_losses)

    # Create two vars = 0 for row counters:
    row_max_counter = 0
    row_min_counter = 0

    # For loop to find the index of max_changes to use to find date of Greatest Increase:
    for row in changes_profit_losses:
        if row == max_changes: 
            max_index = row_max_counter
        else:
            row_max_counter += 1
    # Set max_date to the index we just found and add 1 for skipping the first row in the changes of profits/losses calculation (see line 26):
    max_date = date_bank[max_index+1]

    # For loop to find the index of min_changes to use to find date of Greatest Decrease:
    for row in changes_profit_losses:
        if row == min_changes: 
            min_index = row_min_counter
        else:
            row_min_counter += 1
    # Set min_date to the index we just found and add 1 for skipping the first row in the changes of profits/losses calculation (see line 26):
    min_date = date_bank[min_index+1]

    # Print Financial Analysis
    print(f'Financial Analysis')
    print(f'----------------------------')
    # Print total months:
    print(f'Total Months: {total_months}')
    # Print total:
    print(f'Total: ${total}')
    # Print Average Change:
    print(f'Average Change: ${ave_change}')
    # Print date and amount of Greatest Increase in Profits: 
    print(f'Greatest Increase in Profits: {max_date} (${max_changes})')
    # Print date and amount of Greatest Decrease in Profits:
    print(f'Greatest Decrease in Profits: {min_date} (${min_changes})')
    
    # Print Financial Analysis
    print(financial_analysis)
    # Export a text file of the results:

