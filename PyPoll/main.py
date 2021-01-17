# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy as np

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

voter_id = []
county = []
candidate = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_votes = len(voter_id)

#count the number of times each candidate appear
frequencies = [ [i,candidate.count(i)] for i in set(candidate) ]

#separate lists into candidates and number of votes achieves
candidates, number_votes = map(list, zip(*frequencies)) 
number_candidates = len(candidates)

#calculate the percentage of votes and insert into a new list
percentage_votes = []
for value in number_votes:
    percentage = (round(int(value) / int(total_votes)*100,2))
    percentage_votes.append(percentage)

#get the winner by the greatest percentage of votes
max_votes = max(percentage_votes)
index_winner = percentage_votes.index(max_votes)

Winner = candidates[index_winner]

#Print Results
print("Election Results")
print("------------------")
print(f"Total Votes: {total_votes}")
print("------------------")
print(f"{candidates[0]}: {percentage_votes[0]}% ({number_votes[0]})")
print(f"{candidates[1]}: {percentage_votes[1]}% ({number_votes[1]})")
print(f"{candidates[2]}: {percentage_votes[2]}% ({number_votes[2]})")
print(f"{candidates[3]}: {percentage_votes[3]}% ({number_votes[3]})")
print("------------------")
print(f"Winner: {Winner}")
print("------------------")

#Export Data to TXT FILE inside Analysis Folder
txtpath = os.path.join( 'Analysis', 'poll_results.txt')
f=open(txtpath,"w+")
f.write("Election Results\r\n")
f.write("---------------------\r\n")
f.write(f"Total Votes: {total_votes}\r\n")
f.write("---------------------\r\n")
f.write(f"{candidates[0]}: {percentage_votes[0]}% ({number_votes[0]})\r\n")
f.write(f"{candidates[1]}: {percentage_votes[1]}% ({number_votes[1]})\r\n")
f.write(f"{candidates[2]}: {percentage_votes[2]}% ({number_votes[2]})\r\n")
f.write(f"{candidates[3]}: {percentage_votes[3]}% ({number_votes[3]})\r\n")
f.write("---------------------\r\n")
f.write(f"Winner: {Winner}\r\n")
f.write("---------------------\r\n")
f.close()