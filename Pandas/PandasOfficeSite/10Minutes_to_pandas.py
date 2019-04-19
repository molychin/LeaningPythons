# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:40:17 2019

@author: Administrator
"""

## 10 Minutes to pandas
#This is a short introduction to pandas, geared mainly for new users. You can see more complex recipes in the Cookbook.
import numpy as np
import pandas as pd

#pandas 版本
#c:/>python -m pip list   查看matplotlib版本   0.23.4
#c:/>python -m pip install --upgrade matplotlib   升级matplotlib 3.02
### Object Creation
#See the Data Structure Intro section.
#Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 5, np.nan, 6, 8])  #3->3.0;np.nan->NaN;
#print(s)

#Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods=6)
print(dates)

