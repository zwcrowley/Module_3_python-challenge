# PyRoll- Module 3: by Zack Crowley
# Import dependencies:
import os
import csv

# Read in the CSV file using the os.path:
with open(os.path.join('Resources', 'election_data.csv')) as csvfile:
    # Read in the voter data as a dictionary:
    votes_data = csv.DictReader(csvfile)

