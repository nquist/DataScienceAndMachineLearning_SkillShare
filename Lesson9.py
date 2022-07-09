# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:22:38 2022

@author: nquist

Site: SkillShare
Course: Data Science and Machine Learning with Python - Hands On! by Frank Kane
Lesson: 9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PastHires.csv")
print(df.head()) # Default 5 rows, can specify the number of rows

print(df.tail()) # same with the end of the table

df.shape # returns the shape of the file (rows, columns)
df.size # returns number of cells
len(df) # returns number of rows
df.columns # returns the titles of the columns


print(df['Hired'][:5]) #extract column and specific rows

test = df[['Years Experience', 'Hired']]

df.sort_values(['Years Experience']) # sorts table values by columns

degree_counts = df['Level of Education'].value_counts()
print(degree_counts)

degree_counts.plot(kind='bar')


#%%

# Exercise: Try extracting rows 5-10 of our DataFrame, preserving on the 
# "Previous Employers" and "Hired" columns. Assign that to a new DataFrame, 
# and create a histogram plotting the distribution of the previous employers in 
# the subset of the data.

df_subset = df[["Previous employers", "Hired"]][5:11]
employ_counts = df_subset['Previous employers'].value_counts()

employ_counts.plot(kind='bar')
