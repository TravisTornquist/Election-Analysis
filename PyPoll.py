#Import our dependencies
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
#assign a variable to save the file to a path
file_to_save = os.path.join('Analysis','election_analysis.txt')

#open the elction results and read the file
with open(file_to_load) as election_data:
    
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)
    

