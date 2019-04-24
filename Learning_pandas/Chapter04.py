# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:45:09 2019

@author: Administrator
"""


# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
#get_ipython().magic('matplotlib inline')



#Representing Tabular and Multivariate Data
#with the DataFrame
#The pandas DataFrame object extends the capabilities of the Series object into two-dimensions. Instead of a
#single series of values, each row of a data frame can have multiple values, each of which is represented
#as a column. Each row of a data frame can then model multiple related properties of a subject under
#observation, and with each column being able to represent different types of data.
#表示表格和多变量数据
#通过数据帧，熊猫数据帧对象将系列对象的功能扩展到二维。数据帧的每一行可以有多个值，而不是一系列的值，
#每一行都表示为一列。然后，数据帧的每一行可以为被观察对象的多个相关属性建模，并且每一列可以表示不同类型的数据。
#
#
#This automatic alignment makes a data frame much more capable of exploratory data analysis than
#spreadsheets or databases. Combined with the ability to slice data simultaneously across both rows and
#columns, this ability to interact with and explore data in a data frame is incredibly effective for finding the
#required information.
#这种自动对齐使数据框架比电子表格或数据库更能进行探索性数据分析。与跨行和列同时切片数据的能力相结合，
#这种在数据帧中与数据交互和探索数据的能力对于查找所需信息是非常有效的。
#
#Specifically, in this chapter we will cover the following topics:
#Creating a DataFrame from Python objects, NumPy functions, Python dictionaries, pandas Series objects,
#and CSV files
#Determining the size of the dimensions of a data frame
#Specifying and manipulating the names of the columns in a data frame
#Alignment of rows during the creation of a data frame
#Selecting specific columns and rows of a data frame
#Applying slicing to a data frame
#Selecting rows and columns of a data frame by location and label
#Scalar value lookup
#Boolean selection as applied to a data frame




# # Creating a DataFrame using NumPy function results
# From a 1-d array
df_01=pd.DataFrame(np.arange(1, 6))
#print(df_01)

# create a DataFrame from a 2-d ndarray
df = pd.DataFrame(np.array([[10, 11], [20, 21]]))
#print(df)

# retrieve the columns index
print(df.columns)

# specify column names
df = pd.DataFrame(np.array([[70, 71], [90, 91]]),
                  columns=['Missoula', 'Philadelphia'])
#print(df)

# how many rows?
#print(len(df))   #=2

# what is the dimensionality
#print(df.shape)   #=(2, 2)


# # Creating a DataFrame using a Python dictionary and pandas Series objects
# initialization using a python dictionary
temps_missoula = [70, 71]
temps_philly = [90, 91]
temperatures = {'Missoula': temps_missoula,
                'Philadelphia': temps_philly}
df_01=pd.DataFrame(temperatures)
#print(df_01)


# create a DataFrame for a list of Series objects
temps_at_time0 = pd.Series([70, 90])
temps_at_time1 = pd.Series([71, 91])
df = pd.DataFrame([temps_at_time0, temps_at_time1])
#print(df)

#This result is different from what we perhaps expected, as the values have been filled with NaN. This can
#be rectified in two ways. The first is to assign the column names to the .columns property:
#这一结果与我们可能预期的不同，因为数值已经用NaN填充。这可以通过两种方式加以纠正。第一种方法是将列名分配给.columns属性：
# try to specify column names
df = pd.DataFrame([temps_at_time0, temps_at_time1],
                  columns=['Missoula', 'Philadelphia'])
#print(df)   #NaN

# specify names of columns after creation
df = pd.DataFrame([temps_at_time0, temps_at_time1])
df.columns = ['Missoula', 'Philadelphia']
#print(df)   

# construct using a dict of Series objects
temps_mso_series = pd.Series(temps_missoula)
temps_phl_series = pd.Series(temps_philly)
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series})
#print(df)

# alignment occurs during creation
temps_nyc_series = pd.Series([85, 87], index=[1, 2])
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series,
                   'New York': temps_nyc_series})
#print(df)

# # Creating a DataFrame from a CSV file
# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])  #指定读入列
# peek at the first 5 rows of the data using .head()
print(sp500.head())

# how many rows of data?  Should be 500
#print(len(sp500))  #=500

# what is the shape?
#print(sp500.shape)    #=(500, 3)

# what is the size?
#The size of the data frame can be found using the .size property. This property returns the number of data
#values in the data frame. We would expect 500*3 = 1,500
#print(sp500.size)   #=1500

# examine the index
#print(sp500.index)

# get the columns
#print(sp500.columns)

# # Selecting columns of a DataFrame
# retrieve the Sector column
#print(sp500['Sector'].head())

#print(type(sp500['Sector']))

# retrieve the Price and Book Value columns
#print(sp500[['Price', 'Book Value']].head())

# show that this is a DataFrame
#print(type(sp500[['Price', 'Book Value']]))

# attribute access of column by name
#print(sp500.Price)

# # Selecting rows of a DataFrame

# get row with label MMM
# returned as a Series
#print(sp500.loc['MMM'])

# rows with label MMM and MSFT
# this is a DataFrame result
#print(sp500.loc[['MMM', 'MSFT']])

# get rows in location 0 and 2
#print(sp500.iloc[[0, 2]])

# get the location of MMM and A in the index
i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
#print((i1, i2))     #索引序列号

# and get the rows
#print(sp500.iloc[[i1, i2]])


# # Scalar lookup by label or location using .at[] and .iat[] 
# by label in both the index and column
#print(sp500.at['MMM', 'Price'])

# by location.  Row 0, column 1
#print(sp500.iat[0, 1])

# # Slicing using the [] operator
# first five rows
#print(sp500[:5])
# ABT through ACN labels
#print(sp500['ABT':'ACN'])

# # Selecting rows using Boolean selection
# what rows have a price < 100?
#print(sp500.Price < 100)

# now get the rows with Price < 100
#print(sp500[sp500.Price < 100])

# get only the Price where Price is < 10 and > 0
r = sp500[(sp500.Price < 10) & (sp500.Price > 6)] ['Price']
print(r)

# # Selecting across both rows and columns
# select the price and sector columns for ABT and ZTS
print(sp500.loc[['ABT', 'ZTS']][['Sector', 'Price']])






























