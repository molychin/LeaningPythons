# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:25:27 2019

@author: Administrator
"""


#Python for Data Analysis
#DATA WRANGLING WITH PANDAS,NUMPY, AND IPYTHON
#Wes McKinney
import numpy as np
import pandas as pd


#Data Cleaning and Preparation

#During the course of doing data analysis and modeling, a significant amount of time
#is spent on data preparation: loading, cleaning, transforming, and rearranging. Such
#tasks are often reported to take up 80% or more of an analyst’s time. Sometimes the
#way that data is stored in files or databases is not in the right format for a particular
#task. Many researchers choose to do ad hoc processing of data from one form to
#another using a general-purpose programming language, like Python, Perl, R, or Java,
#or Unix text-processing tools like sed or awk. Fortunately, pandas, along with the
#built-in Python language features, provides you with a high-level, flexible, and fast set
#of tools to enable you to manipulate data into the right form.
#在进行数据分析和建模的过程中，大量时间花在数据准备上：加载、清理、转换和重新排列。据报道，这类任务通常
#占用分析师80%或更多的时间。有时，数据存储在文件或数据库中的方式对于特定任务的格式不正确。许多研究人员
#选择使用一种通用编程语言（如Python、Perl、R或Java）或UNIX文本处理工具（如SED或AWK）从一种形式到
#另一种形式进行数据的特设处理。幸运的是，熊猫以及内置的Python语言特性为您提供了一个高级、灵活和快速的集合。
#使您能够将数据操作到正确的表单中的工具。

#Handling Missing Data
#Missing data occurs commonly in many data analysis applications. One of the goals
#of pandas is to make working with missing data as painless as possible. For example,
#all of the descriptive statistics on pandas objects exclude missing data by default.
#The way that missing data is represented in pandas objects is somewhat imperfect,
#but it is functional for a lot of users. For numeric data, pandas uses the floating-point
#value NaN (Not a Number) to represent missing data. We call this a sentinel value that
#can be easily detected:
#处理丢失的数据
#在许多数据分析应用程序中，丢失数据通常会出现。熊猫的目标之一是尽可能无痛地处理丢失的数据。例如，
#默认情况下，熊猫对象的所有描述性统计数据都排除丢失的数据。
#在熊猫对象中表示丢失数据的方法有些不完善，但对于许多用户来说，它是有用的。对于数字数据，pandas使用浮点值nan（不是数字）
#表示缺少的数据。我们称之为哨兵值，很容易检测到：

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
#print(string_data)
#print(string_data.isnull())

#In pandas, we’ve adopted a convention used in the R programming language by refer‐
#ring to missing data as NA, which stands for not available. In statistics applications,
#NA data may either be data that does not exist or that exists but was not observed
#(through problems with data collection, for example). When cleaning up data for
#analysis, it is often important to do analysis on the missing data itself to identify data
#collection problems or potential biases in the data caused by missing data.
#在pandas中，我们采用了r编程语言中使用的一种约定，将丢失的数据称为na，表示不可用。在统计应用程序中，
#NA数据可能是不存在或存在但未观察到的数据（例如，通过数据收集问题）。在清理数据进行分析时，通常重要
#的是对丢失的数据本身进行分析，以确定数据收集问题或丢失数据导致的数据潜在偏差。

string_data[0] = None
#print(string_data.isnull())

#Filtering Out Missing Data
#There are a few ways to filter out missing data. While you always have the option to
#do it by hand using pandas.isnull and boolean indexing, the dropna can be helpful.
#On a Series, it returns the Series with only the non-null data and index values:
#过滤掉丢失的数据
#有几种方法可以过滤掉丢失的数据。虽然您总是可以选择手动使用pandas.isNull和布尔索引，但dropna会
#很有帮助。对于一个系列，它只返回包含非空数据和索引值的系列：
data = pd.Series([1, np.nan, 3.5,np.nan, 7])
#print(data)
#print(data.dropna())   #删除nan项  =data[data.notnull()]

#With DataFrame objects, things are a bit more complex. You may want to drop rows
#or columns that are all NA or only those containing any NAs. dropna by default drops
#any row containing a missing value:
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan,np.nan],
    [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
#print(data)
cleaned = data.dropna()    #删除含有任一个nan的行
#print(cleaned)
#Passing how='all' will only drop rows that are all NA:
cleaned=data.dropna(how='all')    #每行所有值为nan，则删除
#print(cleaned)

#To drop columns in the same way, pass axis=1:
data[4] = np.nan
print(data)
cleaned=data.dropna(axis=1, how='all')
print(cleaned)































