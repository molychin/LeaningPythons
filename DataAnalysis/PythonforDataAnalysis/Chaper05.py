# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:54:30 2019

@author: Administrator
"""

#Python for Data Analysis
#DATA WRANGLING WITH PANDAS,NUMPY, AND IPYTHON
#Wes McKinney
import numpy as np
import pandas as pd

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
    [np.nan, np.nan], [0.75, -1.3]],
    index=['a', 'b', 'c', 'd'],
    columns=['one', 'two'])
print(df)
#print(df.sum())   #按行计算汇总
#print(df.sum(axis='columns'))   #按列计算汇总
#print(df.mean(axis='columns'))
#NA values are excluded unless the entire slice (row or column in this case) is NA.
#This can be disabled with the skipna option:
#除非整个切片（本例中的行或列）为NA，否则不包括NA值。可以使用skipna选项禁用此选项：
#print(df.mean(axis='columns', skipna=False))

#Unique Values, Value Counts, and Membership
#Another class of related methods extracts information about the values contained in a
#one-dimensional Series. 
#唯一值、值计数和成员身份
#另一类相关方法提取一维序列中包含的值的信息。
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()   #获取唯一值
#print(uniques)
#print(obj.value_counts())
#不排序
#print(pd.value_counts(obj.values, sort=False))

mask = obj.isin(['b', 'c'])
print(mask)

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
    'Qu2': [2, 3, 1, 2, 3],
    'Qu3': [1, 5, 2, 4, 4]})
print(data)
#Here, the row labels in the result are the distinct values occurring in all of the col‐
#umns. The values are the respective counts of these values in each column.
#这里，结果中的行标签是所有列中出现的不同值。这些值是每列中这些值的各自计数。
#result = data.apply(pd.value_counts)
result = data.apply(pd.value_counts).fillna(0)
#print(result)





