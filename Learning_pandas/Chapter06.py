# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:50:08 2019

@author: Administrator
"""

# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

#Indexing Data
#An index is a tool for optimized look up of values from a series or DataFrame. They are a lot like a key in
#a relational database, but more powerful. They provide the means of alignment for multiple sets of data
#and also carry semantics for how to handle various tasks with data such as resampling to different
#frequencies.
#Much of the modeling that you will perform with pandas depends critically on how you set up your
#indexes. A properly implemented index will optimize performance and be an invaluable tool in driving
#your analysis.
#索引是一种工具，用于优化从序列或数据帧中查找值。它们很像关系数据库中的键，但功能更强大。它们为多组数据提供
#了对齐的方法，还提供了如何使用数据处理各种任务的语义，例如重新采样到不同的频率。
#您将对熊猫执行的建模很大程度上取决于您如何设置索引。一个正确实现的索引将优化性能，并且是驱动分析的宝贵工具。
#We have previously used indexes briefly, and in this chapter, we will dive quite a bit deeper. During this
#deep dive, we will learn more about:
#The importance of indexes
#The types of pandas indexes, including RangeIndex, Int64Index, CategoricalIndex, Float64Index, Datetimeindex,
#and PeriodIndex
#Setting and resetting an index
#Creating hierarchical indexes
#Selection of data using hierarchical indexes


# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])
print(sp500.head())
# # The importance of indexes
# create DataFame of random numbers and a key column
np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(10000), 'key':range(100, 10100)})
#print(df[:5])

# boolean select where key is 10099
#print(df[df.key==10099])



#Conceptually, this is simple. But what if we want to do this repeatedly? This can be simulated in Python
#using the %timeit statement. The following code performs the lookup repeatedly and reports on the
#performance.
#从概念上讲，这很简单。但是如果我们想反复这样做呢？这可以在python中使用%timeit语句进行模拟。以下代码重复执行查找并报告性能。
# time the select
get_ipython().magic('timeit df[df.key==10099]')  #552us

#%timeit df[df.key==10099]     #error

# move key to the index
df_with_index = df.set_index(['key'])
#print(df_with_index[:5])

# now can lookup with the index
df_with_index.loc[10099]
# and this is a lot faster
get_ipython().magic('timeit df_with_index.loc[10099]')  #101us

# # The fundamental index type: Index

#The downside of using an index is that it can take time to construct and also consumes more memory.
#使用索引的缺点是它可能需要一些时间来构造，并且会消耗更多的内存。

#Many times, you will inherently know what your indexes should be and you can just create them upfront
#and get going with exploration. Other times, it will take some exploration first to determine the best index.
#And often it is possible that you do not have enough data or the proper fields to create a proper index. In
#these cases, you may need to use a partial index that returns multiple semi-ambiguous results and still
#perform Boolean selection on that set to get to the desired result.
#很多时候，你会从本质上知道你的索引应该是什么，你可以直接创建它们，然后继续探索。有时，需要先进行一些探索才能确定最佳指标。
#通常情况下，您可能没有足够的数据或适当的字段来创建适当的索引。在这些情况下，可能需要使用返回多个半模糊结果的部分索引，
#并对该集合执行布尔选择以获得所需的结果。

#The fundamental type - Index
#This type of index is the most generic and represents an ordered and sliceable set of values. The values
#that it contains must be hashable Python objects. This is because the index will use this hash to form an
#efficient lookup of values associated with the value of that object. While hash lookup is preferred over
#linear lookup, there are other types of indexes that can be further optimized.
#基本类型索引
#这种类型的索引是最通用的，表示一组有序且可切片的值。它包含的值必须是可哈希的python对象。这是因为索引
#将使用此哈希来高效查找与该对象的值关联的值。虽然哈希查找优于线性查找，但还有其他类型的索引可以进一步优化。



























