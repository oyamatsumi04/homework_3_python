#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dictionaries

import pandas as pd
import os


# In[2]:


#open and read first 5 rows of the csv

pybank_path="PyBank.csv"
pybank_df=pd.read_csv(pybank_path)
pybank_df.head()


# In[7]:


#Using the dif function to calculate changes from previous month

profit_dif_test=pybank_df['Profit/Losses'].diff()
pybank_df['Profit Change'] = profit_dif_test

pybank_df.head()


# In[26]:


#printing outputs

print("")
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(pybank_df.shape[0]))
print("Total: $" + str(pybank_df['Profit/Losses'].sum()))
print("Average Monthly Change: $" + str(pybank_df['Profit Change'].mean()))
print("Greatest Increase in Profits: $" + str(pybank_df['Profit Change'].max()) + " occurred during " + pybank_df.loc[pybank_df['Profit Change'].idxmax(), 'Date'])
print("Greatest Decrease in Profits: $" + str(pybank_df['Profit Change'].min()) + " occurred during " + pybank_df.loc[pybank_df['Profit Change'].idxmin(), 'Date'])

