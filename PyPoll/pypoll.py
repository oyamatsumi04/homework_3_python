#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dictionaries

import pandas as pd
import os


# In[2]:


#open and read first 5 rows of the csv

pypoll_path="Pypoll.csv"
pypoll_df=pd.read_csv(pypoll_path)
pypoll_df.head()


# In[7]:


#Display distinct candidates

pypoll_df['Candidate'].unique()


# In[29]:


#Set up percentages by candidate

Khan_share = (pypoll_df.loc[pypoll_df['Candidate'] == 'Khan', 'Candidate'].count())/(pypoll_df.shape[0])
Khan_share = Khan_share.round(2)*100
print(Khan_share)

Correy_share = (pypoll_df.loc[pypoll_df['Candidate'] == 'Correy', 'Candidate'].count())/(pypoll_df.shape[0])
Correy_share = Correy_share.round(2)*100
print(Correy_share)

Li_share = (pypoll_df.loc[pypoll_df['Candidate'] == 'Li', 'Candidate'].count())/(pypoll_df.shape[0])
Li_share = Li_share.round(2)*100
print(Li_share)

OTooley_share = (pypoll_df.loc[pypoll_df['Candidate'] == "O'Tooley", 'Candidate'].count())/(pypoll_df.shape[0])
OTooley_share = OTooley_share.round(2)*100
print(OTooley_share)


# In[53]:


winner=""
if ((Correy_share>Khan_share) and (Correy_share>Li_share) and (Correy_share>OTooley_share)):
    winner="Correy"
elif ((Khan_share>Correy_share) and (Khan_share>Li_share) and (Khan_share>OTooley_share)):
    winner="Khan"
elif ((Li_share>Correy_share) and (Li_share>Khan_share) and (Li_share>OTooley_share)):
    winner="Li"
else: winner="O'Tooley"
print(winner)


# In[55]:


#printing outputs

print("")
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(pypoll_df.shape[0]))
print("------------------------------")
print("Votes for Correy: " + str(pypoll_df.loc[pypoll_df['Candidate'] == 'Correy', 'Candidate'].count()) + " (" + str(Correy_share) + "%)") 
print("Votes for Khan: " + str(pypoll_df.loc[pypoll_df['Candidate'] == 'Khan', 'Candidate'].count()) + " (" + str(Khan_share) + "%)") 
print("Votes for Li: " + str(pypoll_df.loc[pypoll_df['Candidate'] == 'Li', 'Candidate'].count()) + " (" + str(Li_share) + "%)") 
print("Votes for O'Tooley: " + str(pypoll_df.loc[pypoll_df['Candidate'] == "O'Tooley", 'Candidate'].count()) + " (" + str(OTooley_share) + "%)")
print("------------------------------")
print("Winner: " + winner)


# In[ ]:





# In[ ]:




