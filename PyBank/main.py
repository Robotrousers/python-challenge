#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
from pathlib import Path


# In[82]:


# CSV filepath
csv_path = Path("Resources/budget_data.csv", header=0)


# In[83]:


# read CSV file into DF
bank_df = pd.read_csv(csv_path)
bank_df.head()


# In[84]:


# The total number of months included in the dataset
total_months = bank_df['Date'].nunique()


# In[85]:


# The net total amount of "Profit/Losses" over the entire period
net_total = bank_df['Profit/Losses'].sum()


# In[86]:


# The changes in "Profit/Losses" over the entire period, and then the average of those changes
bank_df['Change'] = bank_df['Profit/Losses'].diff()


# In[87]:


# The greatest increase in profits (date and amount) over the entire period
greatest_increase = bank_df.loc[bank_df['Change'].idxmax()]


# In[88]:


# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = bank_df.loc[bank_df['Change'].idxmin()]


# In[89]:


# average of those changes
average_change = bank_df['Change'].mean()


# In[90]:


# making the analysis fit the instruction example
analysis_df = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})\n"
)


# In[91]:


# Export the DataFrame to .txt
with open('bank_analysis.txt', 'w') as file:
    file.write(analysis_df)
print(analysis_df)


# In[ ]:




