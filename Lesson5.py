# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:20:52 2022

@author: nquist

Site: SkillShare
Course: Data Science and Machine Learning with Python - Hands On! by Frank Kane
Lesson: 5-8
"""

listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    if (number % 2 == 0):
        print('%i is even.' % number)
    else:
        print('%i is odd.' % number)
        
print("All done.")

import numpy as np

A = np.random.normal(25.0, 5.0, 10)
print(A)

# Lists
x = list(np.arange(1, 7, 1))

x.extend([7, 8]) # add two lists together

# Dictionaries

fruits = {}
fruits['apples'] = 20
fruits['oranges'] = 3

print(fruits.get('oranges'))
print(fruits.get('grapes'))

# can itterate over keys
for ftype in fruits:
    print(ftype)
    
# You can pass funtions as arguments into other functions in python

# TO DO: Find and practice use cases for lambda functions.

#%%
# Activity: Write some code that creates a list of integers, loops though
# each element of the list, and only prints out even numbers!

int_list = list(np.arange(0, 20, 1))

for i in range(len(int_list)):
    if (int_list[i] % 2) == 0:
        print(int_list[i])
        
print('Complete!')