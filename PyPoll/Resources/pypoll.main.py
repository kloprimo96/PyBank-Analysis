#!/usr/bin/env python
# coding: utf-8

# In[47]:


import os
import csv

election_data = os.path.join(".","election_data.csv")

results_to_output = os.path.join(".","pypoll_analysis.txt")

total_votes = 0


candidate_votes = {}
candidate_options = []


winning_candidate = ""
winning_count = 0

with open (election_data) as csvfile:
    reader = csv.reader(csvfile)
    
    
    header = next(reader)
    
    for row in reader: 
        
        total_votes = total_votes + 1
        
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
            

election_results = (
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes {total_votes}\n"

    )        

print(election_results)


with open(results_to_output, "w") as txt_file:
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes: 
        
        votes = candidate_votes[candidate]
        voter_percentage = float(votes) / float(total_votes) * 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {voter_percentage:.3f}% ({votes}) \n"
        
        print(voter_output)
        
        txt_file.write(voter_output)
        
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n")
    
    txt_file.write(winning_candidate_summary)
    


# In[ ]:





# In[ ]:




