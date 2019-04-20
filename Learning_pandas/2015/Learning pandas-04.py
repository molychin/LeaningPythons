
# coding: utf-8

# ## The pandas Series Object

# In[ ]:


pandas is a high-performance library that provides a comprehensive set of data
structures for manipulating tabular data, providing high-performance indexing,
automatic alignment, reshaping, grouping, joining, and statistical analyses capabilities.
PANDAS是一个高性能的库，它为处理表格数据、提供高性能索引、自动对齐、重塑、分组、连接和统计分析功能提供了一套全面的数据结构。

The two primary data structures in pandas are the Series and the DataFrame
objects. In this chapter, we will examine the Series object and how it builds on the
features of a NumPy ndarray to provide operations such as indexing, axis labeling,
alignment, handling of missing data, and merging across multiple series of data.
pandas的两个主要数据结构是Series和DataFrame。在本章中，我们将研究series对象以及它如何
基于numpy ndarray的特性来提供诸如索引、轴标记、对齐、处理丢失数据以及跨多个数据系列合并等操作。


# In[ ]:


In this chapter, we will cover the following topics:
• Creating and initializing a Series and its index
• Determining the shape of a Series object
• Heads, tails, uniqueness, and counts of values
• Looking up values in a Series object
• Boolean selection
• Alignment via index labels
• Arithmetic operations on a Series object
• Reindexing a Series object
• Applying arithmetic operations on Series objects
• The special case of Not-A-Number (NaN)
• Slicing Series objects


# In[ ]:


The Series is the primary building block of pandas. A Series represents a
one-dimensional labeled indexed array based on the NumPy ndarray. Like
an array, a Series can hold zero or more values of any single data type.

A pandas Series deviates from NumPy arrays by adding an associated set of labels
that are used to index and efficiently access the elements of the array by the label
values instead of just by the integer position. This labeled index is a key feature of
pandas Series (and, as we will see, also a DataFrame) and adds significant power
for accessing the elements of the Series over a NumPy array.


# In[ ]:


A pandas index is a first-class component of pandas. pandas provides various
specializations of indexes for different data types with each being highly optimized
for that specific type of data, be it integers, floats, strings, datetime objects, or any
type of hashable pandas object. Additionally, a Series can be reindexed into other
types of indexes, effectively providing different views into the Series object using
different indexes.

pandas提供各种各样的针对不同数据类型的索引专门化，每种索引都针对特定类型的数据
（无论是整数、浮点、字符串、日期时间对象还是任何类型的可哈希熊猫对象）进行了高度优化。
此外，可以将序列重新索引到其他类型的索引中，从而有效地使用不同的索引为序列对象提供不同的视图。


# In[14]:


import numpy as np
import pandas as pd

#Creating Series
#A Series can be created and initialized by passing either a scalar value,
#a NumPy ndarray, a Python list, or a Python Dict as the data parameter of
#the Series constructor. This is the default parameter and does not need to
#be specified if it is the first item.

# create one item Series
s1 = pd.Series(12)
s1
s1[0]
# create a series of multiple items from a list
s2 = pd.Series([1, 2, 3, 4, 5])
s2
# get the index of the Series
s2.index

# explicitly create an index
# index is alpha, not integer
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s3
s3.index
# lookup by label value, not integer position
s3['c']
# create Series from an existing index
# scalar value with be copied at each index label
s4 = pd.Series(2, index=s2.index)
s4
# generate a Series from 5 normal random numbers
np.random.seed(123456)
pd.Series(np.random.randn(5))

# 0 through 9
pd.Series(np.linspace(0, 9, 10))

# 0 through 8
pd.Series(np.arange(0, 9))

# create Series from dict
s6 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
s6


# #### Size, shape, uniqueness, and counts of values

# In[22]:


# example series, which also contains a NaN
s = pd.Series([0, 1, 1, 2, 1, 5, 5, 6, 7, np.nan])
print(s)
# length of the Series
len(s)
# .size is also the # of items in the Series
s.size
# .shape is a tuple with one value
s.shape
# count() returns the number of non-NaN values
s.count()   #去除Nan的计数
# all unique values
s.unique()   #返回不重复的值
# count of non-NaN values, returned max to min order
s.value_counts()    #不重复的值并计数


# In[ ]:


Peeking at data with heads, tails, and take
pandas provides the .head() and .tail() methods to examine just the first few,
or last, records in a Series. By default, these return the first or last five rows,
respectively, but you can use the n parameter or just pass an integer to specify
the number of rows:


# In[38]:


s = pd.Series([0, 1, 1, 2, 1, 5, 5, 6, 7, np.nan])
print(s)
# first five
s.head()
s.head(3)
# last five
s.tail()
#The .take() method will return the rows in a series that correspond to the
#zero-based positions specified in a list:
s.take([0, 3, 9])    #=s[[0,3,9]]

#Looking up values in Series
#Values in a Series object can be retrieved using the [] operator and passing either
#a single index label or a list of index labels. The following code retrieves the value
#associated with the index label 'a' of the s3 series defined earlier
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s3['b']
# lookup by position since the index is not an integer
s3[1]
# multiple items
s3[['a', 'c']]
s[[0,3,9]]
# series with an integer index, but not starting with 0
s5 = pd.Series([1, 2, 3], index=[10, 11, 12])
print(s5)
# force lookup by index label
s5.loc[12]   #按index定位
# forced lookup by location / position
s5.iloc[1]   #按位置定位
# multiple items by label (loc)
s5.loc[[12, 10]]
# multiple items by location / position (iloc)
s5.iloc[[0, 2]]




# In[ ]:


Alignment via index labels
A fundamental difference between a NumPy ndarray and a pandas Series is the
ability of a Series to automatically align data from another Series based on label
values before performing an operation.

numpy ndarray和pandas系列之间的一个基本区别是，在执行操作之前，Series能够根据标签值自动对齐另一个系列的数据。


# In[5]:


import numpy as np
import pandas as pd

s6 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s6
s7 = pd.Series([44, 33, 22,11], index=['d', 'c', 'b', 'a'])
s7
# add them
s6 + s7


# #### Arithmetic operations

# In[13]:


# multiply all values in s3 by 2
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s3 * 2
# scalar series using s3's index
t = pd.Series(2, s3.index)
s3 * t
# we will add this to s9
s8 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 5})
s8
# going to add this to s8
s9 = pd.Series({'b': 6, 'c': 7, 'd': 9, 'e': 10})
s9
# NaN's result for a and e
# demonstrates alignment
s8 + s9
#The NaN value is, by default the
#result of any pandas arithmetic operation where an index label does not align
#with the other Series.

# going to add this to s11
s10 = pd.Series([1.0, 2.0, 3.0], index=['a', 'a', 'b'])
s10
# going to add this to s10
s11 = pd.Series([4.0, 5.0, 6.0], index=['a', 'a', 'c'])
s11
# will result in four 'a' index labels
s10 + s11


# #### The special case of Not-A-Number (NaN)

# In[17]:


nda = np.array([1, 2, 3, 4, 5])
nda.mean()
# mean of numpy array values with a NaN
nda = np.array([1, 2, 3, 4, np.NaN])
nda.mean()   #数组运算，计算式中含有Nan，则返回Nan
# ignores NaN values
s = pd.Series(nda)
s.mean()      #Series运算，会忽略Nan，计算其他值
# handle NaN values like NumPy
s.mean(skipna=False)



# In[ ]:


Boolean selection
Items in a Series can be selected, based on the value instead of index labels, via the
utilization of a Boolean selection. A Boolean selection applies a logical expression to
the values of the Series and returns a new Series of Boolean values representing the
result for each value. The following code demonstrates identifying items in a Series
where the values are greater than 5


# In[21]:


# which rows have values that are > 5?
s = pd.Series(np.arange(0, 10))
s > 5
# select rows where values are > 5
logicalResults = s > 5
s[logicalResults]
# a little shorter version
s[s > 5]

# correct syntax
s[(s > 5) & (s < 8)]

# are all items >= 0?
(s >= 0).all()   #所有条件满足，返回True

# any items < 2?
s[s < 2].any()   #只要有一个条件满足，返回True


# In[ ]:


Reindexing a Series
Reindexing in pandas is a process that makes the data in a Series or DataFrame
match a given set of labels. This is core to the functionality of pandas as it enables
label alignment across multiple objects, which may originally have different
indexing schemes.
在pandas中重新索引是一个使序列或数据帧中的数据与给定标签集匹配的过程。这是pandas功能的核心，
因为它可以跨多个对象对齐标签，这些对象最初可能有不同的索引方案。

This process of performing a reindex includes the following steps:
1. Reordering existing data to match a set of labels.
2. Inserting NaN markers where no data exists for a label.
3. Possibly, filling missing data for a label using some type of logic (defaulting
to adding NaN values).


# In[25]:


# sample series of five items
s = pd.Series(np.random.randn(5))
s
s.index = ['a', 'b', 'c', 'd', 'e']
s
# concat copies index values verbatim,
# potentially making duplicates
np.random.seed(123456)
s1 = pd.Series(np.random.randn(3))
s2 = pd.Series(np.random.randn(3))
combined = pd.concat([s1, s2])
combined
# reset the index
combined.index = np.arange(0, len(combined))
combined


# In[28]:


np.random.seed(123456)
s1 = pd.Series(np.random.randn(4), ['a', 'b', 'c', 'd'])
# reindex with different number of labels
# results in dropped rows and/or NaN's
s2 = s1.reindex(['a', 'c', 'g'])
s2
# s2 is a different Series than s1
s2['a'] = 0
s2
# this did not modify s1
s1


# In[34]:


# different types for the same values of labels
# causes big trouble
s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([3, 4, 5], index=['0', '1', '2'])
s1 + s2
# reindex by casting the label types
# and we will get the desired result
s2.index = s2.index.values.astype(int)
s1 + s2
# fill with 0 instead of NaN
s2 = s.copy()
s2.reindex(['a', 'f'], fill_value=0)
# create example to demonstrate fills
s3 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
s3
# forward fill example
#The following example demonstrates forward filling, often referred to as "last known
#value." The Series is reindexed to create a contiguous integer index, and using the
#method='ffill' parameter, any new index labels are assigned the previously
#known values that are not part of NaN value from earlier in the Series object
s3.reindex(np.arange(0,7), method='ffill')
# backwards fill example
s3.reindex(np.arange(0,7), method='bfill')


# #### Modifying a Series in-place

# In[37]:


# generate a Series to play with
np.random.seed(123456)
s = pd.Series(np.random.randn(3), index=['a', 'b', 'c'])
s
# change a value in the Series
# this is done in-place
# a new Series is not returned that has a modified value
s['d'] = 100
s
# remove a row / item
del(s['a'])
s


# ### Slicing a Series

# In[3]:


import numpy as np
import pandas as pd

# a Series to use for slicing
# using index labels not starting at 0 to demonstrate
# position based slicing
s = pd.Series(np.arange(100, 110), index=np.arange(10, 20))
s
# items at position 0, 2, 4
s[0:6:2]
# first five by slicing, same as .head(5)
s[:5]
# fourth position to the end
s[4:]
# every other item in the first five positions
s[:5:2]
# every other item starting at the fourth position
s[4::2]
# reverse the Series
s[::-1]
# every other starting at position 4, in reverse
s[4::-2]
# :-2, which means positions 0 through (10-2) [8]
s[:-2]
# last three items of the series
s[-3:]
# equivalent to s.tail(4).head(3)
s[-4:-1]
copy = s.copy() # preserve s
slice = copy[:2] # slice with first two rows
slice
# change item with label 10 to 1000
slice[11] = 1000
# and see it in the source
copy






# In[6]:


# used to demonstrate the next two slices
s = pd.Series(np.arange(0, 5),
index=['a', 'b', 'c', 'd', 'e'])
s
# slices by position as the index is characters
s[1:3]
# this slices by the strings in the index
s['b':'d']


# In[ ]:


总结

在本章中，您学习了pandas系列对象以及它如何提供numpy数组之外的功能。我们研究了如何创建和初始化序列及其相关索引。然后，我们使用一个系列来研究如何在一个或多个系列对象中操作数据，包括标签对齐、各种重新排列和更改数据的方法以及应用算术运算。我们结束了对如何重新索引和执行切片的研究。

在下一章中，您将了解如何使用数据帧来表示自动与数据帧级索引对齐的多系列数据，从而为每个索引标签提供统一和自动的表示多个值的能力。


# In[ ]:


第二版P84.   2015第一版 P126

