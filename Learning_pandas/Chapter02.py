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

import warnings
#屏蔽来自未来变化的函数禁用警告信息
warnings.simplefilter(action='ignore', category=FutureWarning)

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
#print(s2[['a','伤害']])
#The s.index property allows direct access to the index of the Series object.
#print(s2.index)

# create a Series who's index is a series of dates
# between the two specified dates (inclusive)
#A common usage of a Series in pandas is to represent a time series that associates
#date/time index labels with a value. A date range can be created using the pandas
#method pd.date_range().
dates = pd.date_range('2016-04-01', '2016-04-06')
#print(dates)

temps1=pd.Series([50,34,445,667,7,34],index=dates)   #使用日期作为索引（标签）
#print(temps1)
#print(temps1['2016-04-02'])

temps2 = pd.Series([70, 75, 69, 83, 79, 77],index = dates)
temp_diffs=temps1-temps2
#print(temp_diffs)

#Statistical methods provided by NumPy can be applied to a pandas Series.
#The following returns the mean of the values in the Series.
#print(temps1.mean())  #求算术平均值
#print(temp_diffs.mean())

#temps_df.columns  #获取列名称
#--------------------------------------------
#A pandas Series can only have a single value associated with each index label. To have multiple values
#per index label we can use a data frame. A data frame represents one or more Series objects aligned by
#index label. Each series will be a column in the data frame, and each column can have an associated
#name.
#熊猫系列只能有一个与每个索引标签关联的值。为了每个索引标签有多个值，我们可以使用一个数据帧。数据帧表示一个或
#多个按索引标签对齐的序列对象。每个序列都将是数据帧中的一列，并且每个列都可以有一个关联的名称。

temps_df = pd.DataFrame({'Missoula': temps1,'Philadelphia': temps2})
#print(temps_df['Missoula'])   #=temps_df.Missoula
#print(temps_df[['Philadelphia', 'Missoula']])   #使用list参数
temps_df['Difference'] = temp_diffs
#print(temps_df)
#print(temps_df.Difference[1:4])


#Entire rows from a DataFrame can be retrieved using its .loc and .iloc properties.
#The following code returns a Series object representing the second row of temps_df
#of the DataFrame object by zero-based position of the row using the .iloc property:
#.loc for label based indexing or .iloc for positional indexing
#可以使用它的.loc和.iloc属性来检索数据帧中的整行。
#以下代码返回表示第二行temps_df的series对象
#通过使用.iloc属性的行的基于零的位置来显示数据帧对象：
#.loc用于基于标签的索引，或.iloc用于位置索引

#print(temps_df.iloc[1])  #获取指定(索引)行的数据，返回Series
#print(temps_df.loc['2016-04-03'])  #获取指定（标签）行的数据
##temps_df.ix[1].index   #DeprecationWarning
#print(temps_df.iloc[[1, 3, 5]].Difference)

#Rows of a DataFrame can be selected based upon a logical expression applied to
#the data in each row. The following code returns the evaluation of the value in the
#Missoula temperature column being greater than 82 degrees:
#可以根据应用于每行数据的逻辑表达式选择数据帧的行。
#print(temps_df.Missoula > 82)
#print(temps_df[temps_df.Missoula > 82])   #获取符合条件的数据行

#This technique is referred to as Boolean Selection in pandas terminology and will form the basis of
#selecting rows based upon values in specific columns (like a query in SQLusing a WHERE clause - but as we
#will see it is much more powerful).


#----------------------------------------------
# ## Loading data from files and the Web
#The data used in analyses is typically provided from other systems via files that are
#created and updated at various intervals, dynamically via access over the Web, or
#from various types of databases. The pandas library provides powerful facilities for
#easy retrieval of data from a variety of data sources and converting it into pandas
#objects. Here, we will briefly demonstrate this ease of use by loading data from files
#and from financial web services.
#分析中使用的数据通常通过不同时间间隔创建和更新的文件从其他系统提供，动态地通过Web访问或从各种类型的数据库访问。
#熊猫图书馆提供了强大的设施，可以方便地从各种数据源中检索数据，并将其转换为熊猫对象。在这里，我们将通过从文件和
#金融Web服务加载数据来简要演示这种易用性。

# #### Loading CSV data from files   从外部文件读取数据
#test1_df = pd.read_csv('data/test1.csv')
test1_df = pd.read_csv('data/goog.csv')
#print(test1_df)
#print(test1_df.head())
#print(test1_df.Date)
#print(test1_df.Date[1])
#print(type(test1_df.Date))
print(type(test1_df.Date[1]))    #此处默认是str

#To guide pandas on how to convert data directly into a Python/pandas date
#object, we can use the parse_dates parameter of the pd.read_csv() function.
#The following code informs pandas to convert the content of the 'date' column
#into actual TimeStamp objects.
test2_df = pd.read_csv('data/goog.csv',parse_dates=['Date'])
#test2_df
print(type(test2_df.Date[1]))
#test2_df.index




































