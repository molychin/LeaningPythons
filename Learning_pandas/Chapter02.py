# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:09:11 2019

@author: Administrator
"""

#Up and Running with pandas
'''
In this chapter will cover the following topics:
●Installation of Anaconda, pandas, and IPython/Jupyter Notebook
●Using IPython and Jupyter Notebook
●Jupyter and its notebooks
●Setting up your pandas environments
●A quick introduction to the pandas Series and DataFrame
●Loading data from a CSV file
●Generating a visualization of pandas data

IPython and Jupyter Notebook
So far we have executed Python from the command line or Terminal. This is the 
default Read-Eval-PrintLoop (REPL) that comes with Python. This can be used to 
run all the examples in this book, but the book
will use IPython for statements in the text and the code package Jupyter Notebook. 
Let's take a brief look at both.


Introducing the pandas Series and DataFrame
Let's jump into using some pandas with a brief introduction to pandas two main data structures, the Series
and the DataFrame. We will examine the following:
●Importing pandas into your application
●Creating and manipulating a pandas Series
●Creating and manipulating a pandas DataFrame
●Loading data from a file into a DataFrame


'''
import numpy as np
import pandas as pd

#The pandas Series is the base data structure of pandas. A series is similar to a NumPy array, but it differs
#by having an index, which allows for much richer lookup of items instead of just a zero-based array index
#value. The following creates a series from a Python list:
#大熊猫系列是大熊猫的基础数据结构。序列类似于numpy数组，但不同的是它有一个索引，它允许对项目进行更丰富的查找，
#而不仅仅是基于零的数组索引值。下面从python列表创建一个系列：

s1=pd.Series([2,5,7,9])
#print (s1)
s1=pd.Series([2,5,7,9,np.nan])   #加入np.nan后，整数自动转化为浮点数
#print(s1[[1,3]])
#A Series object can be created with a user-defined index by specifying the labels for
#the index using the index parameter.
s2=pd.Series([34,44,2,65],index=['a','d','e','伤害'])
#print(s2)

#Data in the Series object can now be accessed by alphanumeric index labels by
#passing a list of the desired labels, as the following demonstrates:
print(s2[['a','伤害']])

#The s.index property allows direct access to the index of the Series object.
print(s2.index)

































