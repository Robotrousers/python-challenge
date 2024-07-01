#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pathlib import Path


# In[60]:


# CSV filepath
csv_path = Path("Resources/election_data.csv", header=0)


# In[61]:


# read CSV file into DF
poll_df = pd.read_csv(csv_path)
poll_df.head()


# In[62]:


# The total number of votes cast
total_votes = len(poll_df)
total_votes


# In[63]:


# A complete list of candidates who received votes
candidates_df = poll_df["Candidate"].unique()
print(candidates_df)


# In[64]:


# The percentage of votes each candidate won
candidates_count_df = poll_df['Candidate'].value_counts()
candidate_percentages = (candidates_count_df / total_votes) * 100
candidate_percentages


# In[65]:


# The winner of the election based on popular vote
winner = candidates_count_df.idxmax()
winner


# In[66]:


# Prepare the analysis results
analysis_df = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate in candidates_df:
    analysis_df += f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidates_count_df[candidate]})\n"

analysis_df += "-------------------------\n"
analysis_df += f"Winner: {winner}\n"
analysis_df += "-------------------------\n"


# In[67]:


# Export the analysis dataframe to .txt
print(analysis_df)
with open('poll_analysis.txt', 'w') as file:
    file.write(analysis_df)

