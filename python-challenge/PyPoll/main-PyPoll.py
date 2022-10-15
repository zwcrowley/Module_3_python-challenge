# PyRoll- Module 3: by Zack Crowley
# Import dependencies:
import os
import csv
from collections import Counter

# Read in the CSV file using the os.path:
with open(os.path.join('Resources', 'election_data.csv')) as csvfile:
    # Read in the voter data as a dictionary:
    votes_data = csv.DictReader(csvfile)

    # Store ballot id and candidate columns each as a seperate list:
    # First, create 2 empty lists for ballot id and candidate:
    candidate_votes = []
    ballot_votes =[]

    # Iterate over votes_data and store each column as a list (skipping county col), both stored as strings:
    for row in votes_data:
        ballot_votes.append(row['Ballot ID']) 
        candidate_votes.append(row['Candidate'])
    
    # Calculate the total votes in total_votes by using the length function on ballot id list, this will count up all the votes cast:
    total_votes = len(ballot_votes)

    # Count the number of votes for each candidate using the Counter function, which counts unique items in a list and returns a dict, the keys will be the candidate name and the values will be the number of votes they received:
    vote_count_dict = Counter(candidate_votes)
    # Sort by the keys in vote_count_dict to get a dict in alphabetical order (to use to get the output to match the example output in assignment description):
    vote_count_abc = sorted(vote_count_dict)

    # Extract the keys from vote_count_abc to save the candidate names as vars:
    stockham_name = list(vote_count_abc)[0]
    degette_name = list(vote_count_abc)[1]
    doane_name = list(vote_count_abc)[2]

    # Store values from vote_count_dict to save the # of votes for each candidate as vars:
    degette_voteCount = vote_count_dict['Diana DeGette']
    stockham_voteCount = vote_count_dict['Charles Casper Stockham']
    doane_voteCount = vote_count_dict['Raymon Anthony Doane']

    # Next, calculate and save the percent vote for each of the three candidates as vars:
    degette_perc = round((degette_voteCount/total_votes)*100,3)
    stockham_perc = round((stockham_voteCount/total_votes)*100,3)
    doane_perc = round((doane_voteCount/total_votes)*100,3)
    
    # Now, use the most_common function to return the candidate with the most votes in the vote_count_dict, this will be a list of tuples (one tuple containing the winner's name and # of votes received):
    winner_tpl = vote_count_dict.most_common(1)
    # Pull out first element of tpl (name of winner):
    winner = (winner_tpl[0][0])

    # Save text for Election Results as a tuple = voter_analysis
    # use the new line var to create a new line inside the f-strings in the tuple:
    new_line = '\n'
    voter_analysis = (
    f'Election Results{new_line}'
    f'------------------------- {new_line}'
    f'Total Votes: {total_votes}{new_line}'
    f'------------------------- {new_line}'
    f'{stockham_name}: {stockham_perc}% ({stockham_voteCount}){new_line}'
    f'{degette_name}: {degette_perc}% ({degette_voteCount}){new_line}'
    f'{doane_name}: {doane_perc}% ({doane_voteCount}){new_line}'
    f'------------------------- {new_line}'
    f'Winner: {winner}{new_line}'
    f'------------------------- {new_line}'
    )
    
    # Print Election Results (voter_analysis) to terminal
    print(voter_analysis)

# Export a text file of the election results to the 'output' folder:
with open(os.path.join("Analysis-PyPoll", 'analysis.txt'), "w") as txtfile:
    txtfile.write(voter_analysis)
    

