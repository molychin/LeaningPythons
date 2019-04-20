
# coding: utf-8

# ## Combining and  Reshaping Data

# In[ ]:


This chapter has two general categories of topics: combination and reshaping
of data. The frst two sections will cover the capabilities provided by pandas to
combine the data from multiple pandas objects together. Combination of data in
pandas is performed by concatenating two sets of data, where data is combined
simply along either axes but without regard to relationships in the data. Or data can
be combined using relationships in the data by using a pandas capability referred
to as merging, which provides join operations that are similar to those in many
relational databases.
本章有两类主题：数据的组合和重塑。前两部分将介绍熊猫提供的将多个熊猫对象的数据组合在一起的功能。
数据组合输入PANDA是通过连接两组数据来执行的，其中的数据只是沿着任意一个轴组合，而不考虑数据中的关系。
或者，可以使用数据中的关系，通过使用所引用的熊猫功能来组合数据。
作为合并，它提供了类似于许多关系数据库中的连接操作。

The remaining sections will examine the three primary means reshaping data in
pandas. These will examine the processes of pivoting, stacking and unstacking,
and melting of data. Pivoting allows us to restructure pandas data similarly to
how spreadsheets pivot data by creating new index levels and moving data into
columns based upon values (or vice-versa). Stacking and unstacking are similar to
pivoting, but allow us to pivot data organized with multiple levels of indexes. And
fnally, melting allows us to restructure data into unique ID-variable-measurement
combinations that are or required for many statistical analyses.
其余部分将研究大熊猫的三种主要方法：重塑数据。这些将检查数据的旋转、堆叠和解压以及熔化过程。
Pivoting允许我们重新构造熊猫数据，类似于电子表格如何通过创建新的索引级别和根据值将数据移动到
列中（反之亦然）来透视数据。堆叠和拆垛与透视类似，但允许我们透视使用多个索引级别组织的数据。
最后，融合允许我们将数据重组为独特的ID变量测量组合，这是许多统计分析所需要的。


# In[ ]:


Specifcally, in this chapter we will examine the following concepts of combining and
reshaping pandas data:
• Concatenation
• Merging and joining
• Pivots
• Stacking/unstacking
• Melting
• The potential performance benefits of stacked data


# #### Concatenating data

# In[3]:


import numpy as np
import pandas as pd

# two Series objects to concatenate
s1 = pd.Series(np.arange(0, 3))
s2 = pd.Series(np.arange(5, 8))
s1
# concatenate them
pd.concat([s1, s2])   #原有索引保持不变



# In[5]:


# create two DataFrame objects to concatenate
# using the same index labels and column names,
# but different values
df1 = pd.DataFrame(np.arange(9).reshape(3, 3),columns=['a', 'b', 'c'])
#df2 has 9 .. 18
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3),columns=['a', 'b', 'c'])
df1
df2


# In[6]:


# do the concat
pd.concat([df1, df2])


# In[9]:


# demonstrate concatenating two DataFrame objects with
# different columns
df1 = pd.DataFrame(np.arange(9).reshape(3, 3),columns=['a', 'b', 'c'])
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3),columns=['a', 'c', 'd'])
df1


# In[10]:


# do the concat, NaN values will be filled in for
# the d column for df1 and b column for df2
pd.concat([df1, df2])


# In[12]:


# concat the two objects, but create an index using the
# given keys
c = pd.concat([df1, df2], keys=['df1', 'df2'])
# note the labeling of the rows in the output
c


# In[14]:


# we can extract the data originating from
# the first or second source DataFrame
c.loc['df2']


# In[15]:


# concat df1 and df2 along columns
# aligns on row labels, has duplicate columns
pd.concat([df1, df2], axis=1)


# In[16]:


# a new DataFrame to merge with df1
# this has two common row labels (2, 3)
# common columns (a) and one disjoint column
# in each (b in df1 and d in df2)
df3 = pd.DataFrame(np.arange(20, 26).reshape(3, 2),columns=['a', 'd'],index=[2, 3, 4])
df3


# In[17]:


# concat them. Alignment is along row labels
# columns first from df1 and then df3, with duplicates.
# NaN filled in where those columns do not exist in the source
pd.concat([df1, df3], axis=1)


# In[ ]:


The type of join can be changed to an inner join and can be performed by specifying
join='inner' as the parameter. The inner join then logically performs an intersection
instead of a union. The following demonstrates this and results in a single row because
2 is the only row index label in common:


# In[18]:


# do an inner join instead of outer
# results in one row
pd.concat([df1, df3], axis=1, join='inner')


# In[19]:


# add keys to the columns
df = pd.concat([df1, df2],axis=1,keys=['df1', 'df2'])
df


# In[23]:


# retrieve the data that originated from the
# DataFrame with key 'df2'
df.loc[:, 'df2']


# In[24]:


# append does a concatenate along axis=0
# duplicate row index labels can result
df1.append(df2)


# In[25]:


# remove duplicates in the result index by ignoring the
# index labels in the source DataFrame objects
df1.append(df2, ignore_index=True)


# ## Merging and joining data
# pandas allows the merging of pandas objects with database-like join operations
# using the pd.merge() function and the .merge() method of a DataFrame object.
# These joins are high performance and are performed in memory. A merge combines
# the data of two pandas objects by fnding matching values in one or more columns
# or row indexes. It then returns a new object that represents a combination of the data
# from both based on relational-database-like join semantics applied to those values.
# pandas允许使用pd.merge（）函数和数据帧对象的.merge（）方法将pandas对象与类似数据库的联接操作合并。
# 这些连接是高性能的，在内存中执行。合并通过在一个或多个列或行索引中查找匹配值来组合两个熊猫对象的
# 数据。然后，它返回一个新对象，该对象表示来自这两个对象的数据组合，这些数据组合基于关系数据库，
# 类似于应用于这些值的连接语义。
# 

# In[27]:


# these are our customers
customers = {'CustomerID': [10, 11],
    'Name': ['Mike', 'Marcia'],
    'Address': ['Address for Mike','Address for Marcia']}
customers = pd.DataFrame(customers)
customers



# In[29]:


import datetime

# and these are the orders made by our customers
# they are related to customers by CustomerID
orders = {'CustomerID': [10, 11, 10],
          'OrderDate': [datetime.date(2014, 12, 1),
                        datetime.date(2014, 12, 1),
                        datetime.date(2014, 12, 1)]}
orders = pd.DataFrame(orders)
orders


# In[30]:


# merge customers and orders so we can ship the items
customers.merge(orders)


# In[ ]:


To be even more detailed, what pandas has specifcally done is the following:
1. Determines the columns in both customers and orders with common labels.
These columns are treated as the keys to perform the join.
2. It creates a new DataFrame whose columns are the labels from the keys
identifed in step 1, followed by all of the non-key labels from both objects.
3. It matches values in the key columns of both DataFrame objects.
4. It then creates a row in the result for each set of matching labels.
5. It then copies the data from those matching rows from each source object into
that respective row and columns of the result.
6. It assigns a new Int64Index to the result.


# In[2]:


import numpy as np
import pandas as pd

# data to be used in the remainder of this section's examples
left_data = {'key1': ['a', 'b', 'c'],'key2': ['x', 'y', 'z'],'lval1': [ 0, 1, 2]}
right_data = {'key1': ['a', 'b', 'c'],'key2': ['x', 'a', 'z'],'rval1': [ 6, 7, 8 ]}
left = pd.DataFrame(left_data, index=[0, 1, 2])
right = pd.DataFrame(right_data, index=[1, 2, 3])
left


# In[3]:


right


# In[35]:


# demonstrate merge without specifying columns to merge
# this will implicitly merge on all common columns
left.merge(right)


# In[36]:


# demonstrate merge using an explicit column
# on needs the value to be in both DataFrame objects
left.merge(right, on='key1')


# In[37]:


# merge explicitly using two columns
left.merge(right, on=['key1', 'key2'])


# In[38]:


# join on the row indices of both matrices
pd.merge(left, right, left_index=True, right_index=True)


# In[4]:


# join on the row indices of both matrices
pd.merge(left, right, left_index=True, right_index=True)


# In[5]:


# outer join, merges all matched data,
# and fills unmatched items with NaN
left.merge(right, how='outer')


# In[6]:


# left join, merges all matched data, and only fills unmatched
# items from the left dataframe with NaN filled for the
# unmatched items in the result
# rows with labels 0 and 2
# match on key1 and key2 the row with label 1 is from left
left.merge(right, how='left')


# In[7]:


# right join, merges all matched data, and only fills unmatched
# item from the right with NaN filled for the unmatched items
# in the result
# rows with labels 0 and 1 match on key1 and key2
# the row with label 2 is from right
left.merge(right, how='right')


# In[8]:


# join left with right (default method is outer)
# and since these DataFrame objects have duplicate column names
# we just specify lsuffix and rsuffix
left.join(right, lsuffix='_left', rsuffix='_right')


# In[9]:


# join left with right with an inner join
left.join(right, lsuffix='_left', rsuffix='_right', how='inner')


# #### Pivoting
# Data is often stored in a stacked format, which is also referred to as record format;
# this is common in databases, .csv fles, and Excel spreadsheets. In a stacked format,
# the data is often not normalized and has repeated values in many columns, or values
# that should logically exists in other tables (violating another concept of tidy data).
# 数据通常以堆叠格式存储，也称为记录格式；这在数据库、csv fles和Excel电子表格中很常见。
# 在堆栈格式中，数据通常不规范化，在许多列中有重复的值，或者在其他表中逻辑上存在的值（违反了整洁数据的另一个概念）。

# In[10]:


# read in accellerometer data
sensor_readings = pd.read_csv("data/accel.csv")
sensor_readings


# In[11]:


# extract X-axis readings
sensor_readings[sensor_readings['axis'] == 'X']


# In[12]:


# pivot the data. Interval becomes the index, the columns are
# the current axes values, and use the readings as values
sensor_readings.pivot(index='interval',columns='axis',values='reading')





# #### Stacking and unstacking
# Similar to the pivot function are the .stack() and .unstack() methods that are
# part of both Series and DataFrame objects. The process of stacking pivots a level of
# column labels to the row index. Unstacking performs the opposite, pivoting a level of
# the row index into the column index.

# In[3]:


#Stacking using nonhierarchical indexes
# simple DataFrame with one column
df = pd.DataFrame({'a': [1, 2]}, index={'one', 'two'})
df




# In[4]:


# push the column to another level of the index
# the result is a Series where values are looked up through
# a multi-index
stacked1 = df.stack()

stacked1.index
stacked1


# In[5]:


# lookup one / a using just the index via a tuple
stacked1[('one', 'a')]


# In[19]:


# DataFrame with two columns
df = pd.DataFrame({'a': [1, 2],'b': [3, 4]},index={'one', 'two'})
df


# In[20]:


# push the two columns into a single level of the index
stacked2 = df.stack()
stacked2


# In[21]:


# lookup value with index of one / b
stacked2[('one', 'b')]


# #### Unstacking using hierarchical indexes
# To demonstrate unstacking with hierarchical indexes we will revisit the sensor data
# we saw earlier in the chapter. However, we will add in an additional column to the
# measurement data that represents readings for multiple users and copy data for two
# users. The following sets up this data

# In[26]:


# make two copies of the sensor data, one for each user
user1 = sensor_readings.copy()
user2 = sensor_readings.copy()
print(user1)
# add names to the two copies
user1['who'] = 'Mike'
user2['who'] = 'Mikael'
# for demonstration, let's scale user2's readings
user2['reading'] *= 100
# and reorganize this to have a hierarchical row index
multi_user_sensor_data = pd.concat([user1, user2]) .set_index(['who', 'interval', 'axis'])
multi_user_sensor_data



# In[24]:


# look up user data for Mike using just the index
multi_user_sensor_data.loc['Mike']


# In[27]:


# readings for all users and axes at interval 1
multi_user_sensor_data.xs(1, level='interval')


# In[28]:


'''
Unstacking will move the last level of the row index into a new level of the columns
index resulting in columns having MultiIndex. The following demonstrates the last
level of this unstacking (the axis level of the index):
'''
# unstack axis
multi_user_sensor_data.unstack()


# In[29]:


# unstack at level=0
multi_user_sensor_data.unstack(level=0)


# In[30]:


'''
Multiple levels can be unstacked simultaneously by passing a list of the levels to
.unstack(). Additionally, if the levels are named, they can be specifed by name
instead of location. The following unstacks the who and axis levels by name:
'''
# unstack who and axis levels
unstacked = multi_user_sensor_data.unstack(['who', 'axis'])
unstacked


# In[31]:


# and we can of course stack what we have unstacked
# this re-stacks who
unstacked.stack(level='who')


# In[ ]:


There are a couple of things worth pointing out about this result. First, stacking
and unstacking always move the levels into the last levels of the other index.
Notice that the who level is now the last level of the row index, but started out earlier
as the frst level. This would have ramifcations on the code to access elements via
that index as it has changed to another level. If you want to put a level back into
another position you will need to reorganize the indexes with other means than
stacking and unstacking.
关于这个结果，有几点值得指出。第一，堆叠拆垛总是将级别移动到另一个索引的最后一个级别。
请注意，who级别现在是行索引的最后一个级别，但开始于前面作为第一层。这将对代码产生影响，以便通过
该索引已更改为另一个级别。如果你想把水平仪放回另一个位置需要用其他方法重新组织索引，而不是堆垛和拆垛。
Second, with all this moving around of data, stacking and unstacking (as well as
pivoting) do not lose any information. They simply change the means by which
it is organized and accessed.
第二，在所有这些数据移动的情况下，堆叠和卸载（以及旋转）不会丢失任何信息。它们只是改变组织和访问它的方式。

Melting
Melting is a type of unpivoting, and is often referred to as changing a DataFrame
object from wide format to long format. This format is common in various statistical
analyses, and data you read may be provided already in a melted form, or you may
need to pass data in this format to other code that expects this organization.
Technically, melting is the process of reshaping a DataFrame into a format
where two or more columns, referred to as variable and value, are created by
unpivoting column labels in the variable column, and then moving the data from
these columns into the appropriate location in the value column. All other columns
are then made into identifer columns that assist in describing the data.
融合是一种非透视类型，通常被称为将数据帧对象从宽格式更改为长格式。这种格式在各种统计分析中都很常见，
您读取的数据可能已经以融合的形式提供，或者您可能需要将这种格式的数据传递给其他期望此组织的代码。
从技术上讲，融合是将一个数据帧整形为一种格式的过程，其中两个或多个列（称为变量和值）是通过在变量
列中取消透视列标签创建的，然后将这些列中的数据移动到值列中的适当位置。然后，所有其他列都被制成有助
于描述数据的标识符列。


# In[32]:


# we will demonstrate melting with this DataFrame
data = pd.DataFrame({'Name' : ['Mike', 'Mikael'],'Height' : [6.1, 6.0],'Weight' : [220, 185]})
data


# In[1]:


# melt it, use Name as the id,
# Height and Weight columns as the variables
pd.melt(data,id_vars=['Name'],value_vars=['Height', 'Weight'])


# In[6]:


#Performance benefts of stacked data
# stacked scalar access can be a lot faster than column access
# time the different methods
#测试代码执行的效率（时间）

import timeit
import numpy as np
import pandas as pd

t = timeit.Timer("stacked1[('one', 'a')]","from __main__ import stacked1, df")
r1 = timeit.timeit(lambda: stacked1.loc[('one', 'a')],number=10000)
r2 = timeit.timeit(lambda: df.loc['one']['a'],number=10000)
r3 = timeit.timeit(lambda: df.iloc[1, 0],number=10000)
# and the results are... Yes, it's the fastest of the three
r1, r2, r3


# In[ ]:


第二版P84.   2015第一版 P286

