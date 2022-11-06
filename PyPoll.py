#Import our dependencies
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
#assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

#add total votes variable
total_votes = 0

candidate_options = []
candidate_votes = {}

winner = ""
winning_count = 0
winning_percentage = 0

#open the elction results and read the file
with open(file_to_load) as election_data:
    
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        total_votes += 1
print(candidate_votes)

for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percentage = (votes/total_votes)*100
    if votes >= winning_count:
        winning_count= votes
        winning_percentage = vote_percentage
        winner = candidate
    print(f"{candidate} recieved {vote_percentage:.1f}% of the vote")
print(f"The winner is {winner} with {winning_count} votes and {winning_percentage:.1f}% of the vote")