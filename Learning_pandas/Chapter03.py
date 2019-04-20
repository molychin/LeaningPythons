# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:40:41 2019

@author: Administrator
Learning pandas-Michael Heydt BIRMINGHAM-2017版
"""

#Representing Univariate Data with the Series
#用序列表示单变量数据

#The Series is the primary building block of pandas. It represents a one-dimensional array-like set of values
#of a single data type. It is often used to model zero or more measurements of a single variable. While it
#can appear like an array, a Series has an associated index that can be used to perform very efficient
#retrievals of values based upon labels.
#该系列是大熊猫的主要组成部分。它表示一个一维数组，类似于单个数据类型的一组值。它通常用于对单个变量的零个或多个测量值建模。
#虽然它看起来像一个数组，但是一个系列有一个关联的索引，可以用来根据标签执行非常有效的值检索。
#
#A Series also performs automatic alignment of data between itself and other pandas objects. Alignment is a
#core feature of pandas where data is multiple pandas objects that are matched by label value before any
#operation is performed. This allows the simple application of operations without needing to explicitly
#code joins.
#一个系列还执行自身和其他熊猫对象之间的数据自动对齐。对齐是熊猫的一个核心特性，其中数据是多个熊猫对象，在执行任何操作之前，
#这些对象与标签值匹配。这使得操作的简单应用无需显式编码联接。
#
#In this chapter, we will examine how to model measurements of a variable using a Series, including using
#an index to retrieve samples. This examination will include overviews of several patterns involved in
#index labeling, slicing and querying data, alignment, and re-indexing data.
#在本章中，我们将研究如何使用一个系列来建模变量的度量，包括使用索引来检索样本。这个检查将包括索引标记、切片和查询数据、
#对齐和重新索引数据中涉及的几个模式的概述。
#
#Specifically, in this chapter we will cover the following topics:
#●Creating a series using Python lists, dictionaries, NumPy functions, and scalar values
#●Accessing the index and values properties of the Series
#●Determining the size and shape of a Series object
#●Specifying an index at the time of Series creation
#●Using heads, tails, and takes to access values
#●Value lookup by index label and position
#●Slicing and common slicing patterns
#●Alignment via index labels
#●Performing Boolean selection
#●Re-indexing a Series
#●In-place modification of values
#
#具体来说，在本章中，我们将讨论以下主题：
#●使用python列表、字典、numpy函数和标量值创建一个系列
#●访问序列的索引和值属性
#●确定一系列物体的大小和形状
#●在创建序列时指定索引
#●使用头部、尾部和Take访问值
#●按索引标签和位置查找值
#●切片和常见切片模式
#●通过索引标签对齐
#●执行布尔选择
#●重新编制系列索引
#●就地修改值
#-------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
#屏蔽来自未来变化的函数禁用警告信息
warnings.simplefilter(action='ignore', category=FutureWarning)


#Creating a Series
#A Series can be created using several techniques. We will examine the following three:
#Using a Python list or dictionary
#From NumPy arrays
#Using a scalar value

# create a series of multiple values from a list
s = pd.Series([10, 11, 12, 13, 14])
#print(s)
# value stored at index label 3
#print(s[3])
# create a Series of alphas
temp_ser1=pd.Series(['Mike', 'Marcia', 'Mikael', 'Bleu'])
#print (temp_ser1)

# a sequence of 5 values, all 2
temp_ser2=pd.Series([2]*5)
#print(temp_ser2)

# use each character as a value
temp_ser3=pd.Series(list('abcde'))
#print(temp_ser3)

# create Series from dict
temp_ser4=pd.Series({'Mike': 'Dad', 
           'Marcia': 'Mom', 
           'Mikael': 'Son', 
           'Bleu': 'Best doggie ever' })
#print(temp_ser4)

# # Creation using NumPy functions
# 4 through 8
temp_ser5=pd.Series(np.arange(4, 9))   #生成[4,8]之间的值
#print(temp_ser5)

# 0 through 9
temp_ser6=pd.Series(np.linspace(0, 9, 5))  #将[0,9]之间的值5等分
#print(temp_ser6)

# random numbers
np.random.seed(12345) # always generate the same values
# 5 normally random numbers
temp_ser7=pd.Series(np.random.normal(size=5))
#print(temp_ser7)

# # Creation using a scalar value
# create a one item Series
s = pd.Series(2)
#print(s)

# create the Series
s = pd.Series(np.arange(0, 5))
# multiple all values by 2
#print(s * 2)

# # The .index and .values properties
# get the values in the Series
s = pd.Series([1, 2, 3])
#print(s.values)    
# show that this is a numpy array
#print(type(s.values))  #返回<class 'numpy.ndarray'>

# get the index of the Series
#print(s.index)

# # The size and shape of a Series
# example series
s = pd.Series([0, 1, 2, 3])
#print(len(s))
# .size is also the # of items in the Series
#print(s.size)
# .shape is a tuple with one value
#print(s.shape)    #(4,)

# # Specifying an index at creation
# explicitly create an index
labels = ['Mike', 'Marcia', 'Mikael', 'Bleu']
role = ['Dad', 'Mom', 'Son', 'Dog']
s = pd.Series(labels, index=role)
#print(s)
# examine the index
#print(s.index)
# who is the Dad?
#print(s['Dad'])

# # Heads, tails and takes
# a ten item Series
s = pd.Series(np.arange(1, 10),index=list('abcdefghi'))
#print(s)
# show the first five
#print(s.head())
# the first three
#print(s.head(n = 3)) # s.head(3) is equivalent
# the last five
#print(s.tail())


#Retrieving values in a Series by label or position
#Values in a Series can be retrieved in two general ways: by index label or by 0-based position. Pandas
#provides you with a number of ways to perform either of these lookups. Let's examine a few of the
#common techniques.

# only take specific items by position
#print(s.take([1, 5, 8]))   #=print(s[[1,5,8]])

# # Lookup by label using the [] and .ix[] operators
# we will use this series to examine lookups
s1 = pd.Series(np.arange(10, 15), index=list('abcde'))
#print(s1) 
# get the value with label 'a'
#print(s1['a'])
## get multiple items
#print(s1[['d', 'b']])
## gets values based upon position
#print(s1[[3, 1]])

# to demo lookup by matching labels as integer values
s2 = pd.Series([1, 2, 3, 4], index=[10, 11, 12, 13])
#print(s2)
## explicitly  by position
#print(s1.iloc[[0, 2]])

# a Series to use for slicing
# using index labels not starting at 0 to demonstrate 
# ★★★★position based slicing
s = pd.Series(np.arange(100, 110), index=np.arange(10, 20))
#print(s)    
## items at position 1, 3, 5
#print(s[1:6:2])
## first five by slicing, same as .head(5)
#print(s[:5])
## fourth position to the end
#print(s[4:])
## every other item in the first five positions
#print(s[:5:2])
## every other item starting at the fourth position
#print(s[4::2])
## reverse the Series
#print(s[::-1])
## every other starting at position 4, in reverse
#print(s[4::-2])
## -4:, which means the last 4 rows
#print(s[-4:])
## :-4, all but the last 4
#print(s[:-4])
## equivalent to s.tail(4).head(3)
#print(s[-4:-1])

#Alignment via index labels  通过索引标签对齐
#Alignment of Series data by index labels is a fundamental concept in pandas, as well as being one of its
#most powerful concepts. Alignment provides automatic correlation of related values in multiple Series
#objects based upon index labels. This saves a lot of error-prone effort matching data in multiple sets using
#standard procedural techniques.
#通过索引标签对齐系列数据是熊猫的一个基本概念，也是熊猫最强大的概念之一。对齐提供了基于索引标签的
#多个序列对象中相关值的自动关联。这就节省了大量使用标准过程技术在多个集合中匹配数据时容易出错的工作。
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([4, 3], index=['b', 'a'])
# add them
#print(s1 + s2)
## multiply all values in s3 by 2
#print(s1 * 2)

# scalar series using s3's index
t = pd.Series(2, s1.index)
#print(t)
## multiply s1 by t
#print(s1 * t)

#p228
# we will add this to s1
s3 = pd.Series([5, 6], index=['b', 'c'])
# s1 and s3 have different sets of index labels
# NaN will result for a and c
#print(s1 + s3)

#Labels in a pandas index do not need to be unique. The alignment operation actually forms a Cartesian
#product of the labels in the two Series. If there are n 'a' labels in series 1, and m labels in series 2, then the
#result will have n*m total rows in the result.
#熊猫索引中的标签不需要是唯一的。对齐操作实际上形成了两个系列中标签的笛卡尔积。如果序列1中有n个“a”标签，
#序列2中有m个标签，则结果中的总行数将为n*m。
# 2 'a' labels
s1 = pd.Series([1.0, 2.0, 3.0], index=['a', 'a', 'b'])
# 3 a labels
s2 = pd.Series([4.0, 5.0, 6.0, 7.0], index=['a', 'a', 'c', 'a'])
# will result in 6 'a' index labels, and NaN for b and c
#print(s1 + s2)


#Performing Boolean selection  执行布尔选择
#Indexes give us a very powerful and efficient means of looking up values in a Series based upon their
#labels. But what if you want to look up entries in a Series based upon the values?
#To handle this scenario pandas provides us with Boolean selection. A Boolean selection applies a logical
#expression to the values of the Series and returns a new series of Boolean values representing the result of
#that expression upon each value. This result can then be used to extract only values where True was a
#result.
#索引为我们提供了一种非常强大和有效的方法，可以根据标签在一个系列中查找值。但是，如果您希望根据值
#查找序列中的条目，该怎么办？
#为了处理这个场景，熊猫为我们提供了布尔选择。布尔选择将逻辑表达式应用于序列的值，并返回一系列新的
#布尔值，这些值表示该表达式对每个值的结果。然后，该结果只能用于提取结果为true的值。
















