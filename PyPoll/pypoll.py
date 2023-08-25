#!/usr/bin/env python
# coding: utf-8

# In[31]:


import csv
import os


#Files to load and OUtput
pollData = os.path.join(".", "Resources", "election_data.csv")

dAnalysis = os.path.join(".", "eAnalysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_votes = {}
candidate_options = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

with open(pollData) as election_data:
    
    
    # Read the header
    reader = csv.reader(election_data)
    
    header = next(reader)
    #print(header)
    
    
    for row in reader:
        #Add to the total vote count
        total_votes = total_votes + 1
        #print(row)

        # Get the candidate name from each row
        candidate_name = row[2]
        
        # If candidate does not match any existing candidate...
        # in a way our looop is discovering candidates as it goes
        
        
        
        if candidate_name not in candidate_options:
            
            # Add it the list of candidates in the running
            candidate_options.append(candidate_name)
            
            
            
            candidate_votes[candidate_name] = 0

        candidate_votes [candidate_name] += 1
            
            
#print(candidate_votes)          
#print(candidate_options)
        
        
        
        
with open(dAnalysis, "w") as txt_file:       
    election_results = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes {total_votes}\n"
        f"------------------------\n"

    )
    
    print(election_results, end="")
    
    txt_file.write(election_results)

    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
            
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"    

        print(voter_output, end="")
    
        txt_file.write(voter_output)
        
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winnder: {winning_candidate}\n"
        f"----------------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)
    
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------


# In[ ]:




