# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 12:41:21 2022

@author: nquist

Site: SkillShare
Course: Data Science and Machine Learning with Python - Hands On! by Frank Kane
Lesson: 12
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#%% Mean
incomes = np.random.normal(27000, 15000, 10000)
print(np.mean(incomes))

#plt.hist(incomes, 50)
#plt.show()

print(np.median(incomes))

incomes = np.append(incomes, [1000000000])
print(np.median(incomes))
print(np.mean(incomes))

#%% Mode

ages = np.random.randint(18, high=90, size=500)
print(ages)

print(stats.mode(ages))

#%% Exercise: Mean & Median Customer Spend

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()

print(np.mean(incomes))
print(np.median(incomes))