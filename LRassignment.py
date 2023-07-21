# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:53:01 2023

@author: kpenaalvarez

"""

import regression_equation as lr
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

# read in data
#look at column names, and I want to plot bettin line versus what actually
#happened

NFLdata = pd.read_csv('NFL2022.csv')
type(NFLdata)
names = list(NFLdata)
print(names)

# SET UP Y WHICH IS THE SCORE =function of x, x=betting line
# delta = home team score - visit team score

x = NFLdata["line"]
y = NFLdata["hScore"] - NFLdata['vScore']

b0, b1 = lr.estimate_coef(x, y)
print(b0, b1)

plt.hist(x, alpha = 0.35, label='line', bins=20)
plt.hist(y, alpha = 0.45, label='actual spread',bins=20)
plt.xlabel('points')
plt.ylabel('frequency')
plt.legend()
plt.grid()
plt.show()

plt.plot(x, y, '.')
xAxis = np.linspace(-20, 15)

yPred = b0 + b1*xAxis
plt.plot(xAxis, yPred, color='red')
plt.xlabel('line')
plt.ylabel('home score-visit score')
plt.hlines(y = 0, xmin=-20, xmax=15, color="orange")