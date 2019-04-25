
# coding: utf-8

# ## Tidying Up Your Data  整理数据

# In[7]:


Data analysis typically ﬂows in a processing pipeline that starts with retrieving data
from one or more sources. Upon receipt of this data, it is often the case that it can be
in a raw form and can be diffcult to use for data analysis. This can be for a multitude
of reasons such as data is not recorded, it is lost, or it is just in a different format than
what you require.
数据分析通常位于处理管道中，从一个或多个源检索数据开始。一旦收到这些数据，通常情况下，
它可以是原始形式的，很难用于数据分析。这可能是由于多种原因造成的，例如数据未被记录、
丢失或格式与您要求的格式不同。
Therefore, one of the most common things you will do with pandas involves tidying
your data, which is the process of preparing raw data for analysis. Showing you
how to use various features of pandas to get raw data into a tidy form is the focus
of this chapter.


# In[ ]:


In this chapter, you will learn:
• The concept of tidy data
• How pandas represents unknown values
• How to find NaN values in data
• How to filter (drop) data
• What pandas does with unknown values in calculations
• How to find, filter and fix unknown values
• How to identify and remove duplicate data
• How to transform values using replace, map, and apply


# In[ ]:


Tidying of data is required for many reasons including these:
• The names of the variables are different from what you require
• There is missing data
• Values are not in the units that you require
• The period of sampling of records is not what you need
• Variables are categorical and you need quantitative values
• There is noise in the data,
• Information is of an incorrect type
• Data is organized around incorrect axes
• Data is at the wrong level of normalization
• Data is duplicated


# In[ ]:


there are several characteristics of data that can be considered good, tidy, and ready for
analysis, which are as follows:
• Each variable is in one column
• Each observation of the variable is in a different row
• There should be one table for each kind of variable
•If multiple tables, they should be relatable
• Qualitative and categorical variables have mappings to values useful for analysis



# ### Working with missing data

# In[ ]:


处理NaN值
In pandas, there are a number of reasons why a value can be NaN:
• A join of two sets of data does not have matched values
• Data that you retrieved from an external source is incomplete
• The NaN value is not known at a given point in time and will be filled in later
• There is a data collection error retrieving a value, but the event must still be
recorded in the index
Reindexing of data has resulted in an index that does not have a value
• The shape of data has changed and there are now additional rows or
columns, which at the time of reshaping could not be determined


# In[8]:


import numpy as np
import pandas as pd

# create a DataFrame with 5 rows and 3 columns
df = pd.DataFrame(np.arange(0, 15).reshape(5, 3),index=['a', 'b', 'c', 'd', 'e'],columns=['c1', 'c2', 'c3'])
df
#生成一些NaN值
# add some columns and rows to the DataFrame
# column c4 with NaN values
df['c4'] = np.nan
# row 'f' with 15 through 18
df.loc['f'] = np.arange(15, 19)
# row 'g' will all NaN
df.loc['g'] = np.nan
# column 'C5' with NaN's
df['c5'] = np.nan
# change value in col 'c4' row 'a'
df['c4']['a'] = 20
print(df)
#Determining NaN values in Series and DataFrame objects
# which items are NaN?
df.isnull()
# count the number of NaN values in each column
df.isnull().sum()
# total count of NaN values
df.isnull().sum().sum()
# number of non-NaN values in each column
df.count()   #计算非NaN值的数量
# and this counts the number of NaN values too
(len(df) - df.count()).sum()
# which items are not null?
df.notnull()


# #### Selecting out or dropping missing data

# In[9]:


# select the non-NaN items in column c4
df.c4[df.c4.notnull()]
# .dropna will also return non NaN values
# this gets all non NaN items in column c4
df.c4.dropna()
#Note that .dropna() has actually returned a copy of DataFrame without the rows.
#The original DataFrame is not changed
# dropna returns a copy with the values dropped
# the source DataFrame / column is not changed
df.c4
#When applied to a DataFrame object, .dropna() will drop all rows from a DataFrame
#object that have at least one NaN value. The following code demonstrates this in action,
#and since each row has at least one NaN value, there are no rows in the result:
# on a DataFrame this will drop entire rows
# where there is at least one NaN
# in this case, that is all rows
df.dropna()  #行含有一个NaN，就删除该行
# using how='all', only rows that have all values
# as NaN will be dropped
df.dropna(how = 'all') #删除所有元素都为NaN的行
# flip to drop columns instead of rows
df.dropna(how='all', axis=1) # say goodbye to c5
# make a copy of df
df2 = df.copy()
# replace two NaN cells with values
df2.loc['g'].c1 = 0
df2.loc['g'].c3 = 0
df2
# now drop columns with any NaN values
df2.dropna(axis=1)
#df2.dropna(how='any', axis=1)
#The .dropna() methods also has a parameter, thresh, which when given an integer
#value specifes the minimum number of NaN values that must exist before the drop is
#performed. The following code drops all columns with at least fve NaN values; these
#are the c4 and c5 columns
# only drop columns with at least 5 NaN values
df2.dropna(thresh=5, axis=1)
#If you want to drop the data in the actual DataFrame, use the inplace=True parameter.
df2.dropna(thresh=5, axis=1,inplace=True)
df2
df



# #### How pandas handles NaN values in mathematical operations

# In[10]:


#The NaN values are handled differently in pandas than in NumPy. This is
#demonstrated using the following example
# create a NumPy array with one NaN value
a = np.array([1, 2, np.nan, 3])
# create a Series from the array
s = pd.Series(a)
# the mean of each is different
a.mean(), s.mean()   #Series忽略NaN
#Note that the mean of the preceding series was calculated as
#(1+2+3)/3 = 2, not (1+2+3)/4, or (1+2+0+4)/4. This verifes that NaN
#is totally ignored and not even counted as an item in the Series.
'''
More specifcally, the way that pandas handles NaN values is as follows:
• Summing of data treats NaN as 0
• If all values are NaN, the result is NaN
• Methods like .cumsum() and .cumprod() ignore NaN values, but preserve
them in the resulting arrays
'''
# demonstrate sum, mean and cumsum handling of NaN
# get one column
s = df.c4
s.sum() # NaN values treated as 0
s.mean() # NaN also treated as 0
# as 0 in the cumsum, but NaN values preserved in result Series
s.cumsum()
# in arithmetic, a NaN value will result in NaN
df.c4 + 1


# #### Filling in missing data

# In[ ]:


If you prefer to replace the NaN values with a specifc value, instead of having them
propagated or ﬂat out ignored, you can use the .fillna() method. The following
code flls the NaN values with 0:


# In[11]:


# return a new DataFrame with NaN values filled with 0
filled = df.fillna(0)   #以0填充所有NaN
filled
'''
Be aware that this causes differences in the resulting values. As an example, the
following code shows the result of applying the .mean() method to the DataFrame
object with the NaN values, as compared to the DataFrame that has its NaN values
flled with 0
'''
# NaNs don't count as an item in calculating
# the means
df.mean()
#print(df.mean())
# having replaced NaN with 0 can make
# operations such as mean have different results
filled.mean()
# only fills the first two NaN values in each row with 0
df.fillna(0, limit=2)


# #### Forward and backward flling of missing values

# In[12]:


'''
Gaps in data can be flled by propagating non-NaN values forward or backward
along a Series. To demonstrate this, the following example will "fll forward"
the c4 column of DataFrame
'''
# extract the c4 column and fill NaNs forward
df.c4.fillna(method="ffill")   #以前面的值填充NaN
# perform a backwards fill
df.c4.fillna(method="bfill")


# #### Filling using index labels
# Data can be flled using the labels of a Series or keys of a Python dictionary. This
# allows you to specify different fll values for different elements based upon the value
# of the index label:

# In[13]:


import numpy as np
import pandas as pd

# create a new Series of values to be
# used to fill NaN values where the index label matches
fill_values = pd.Series([100, 101, 102], index=['a', 'e', 'g'])
fill_values


# In[16]:


print(df.c4)
# using c4, fill using fill_values
# a, e and g will be filled with matching values
df.c4.fillna(fill_values)
df


# In[17]:


# fill NaN values in each column with the
# mean of the values in that column
df.fillna(df.mean())


# #### Interpolation of missing values
# Both DataFrame and Series have an .interpolate() method that will, by default,
# perform a linear interpolation of missing values:

# In[24]:


import datetime
# linear interpolate the NaN values from 1 through 2
s = pd.Series([1, np.nan, np.nan, np.nan, 2])
s.interpolate()  #线性插值

# create a time series, but missing one date in the Series
ts = pd.Series([1, np.nan, 2],
index=[datetime.datetime(2014, 1, 1),datetime.datetime(2014, 2, 1),datetime.datetime(2014, 4, 1)])
ts
# linear interpolate based on the number of items in the Series
ts.interpolate()
# this accounts for the fact that we don't have
# an entry for 2014-03-01
ts.interpolate(method="time")



# In[27]:


# a Series to demonstrate index label based interpolation
s = pd.Series([0, np.nan, 100], index=[0, 1, 10])
s
# linear interpolate
s.interpolate()
# interpolate based upon the values in the index
s.interpolate(method="values")


# ### Handling duplicate data
# The data in your sample can often contain duplicate rows. This is just a reality of
# dealing with data collected automatically, or even a situation created in manually
# collecting data. Often, it is considered best to err on the side of having duplicates
# instead of missing data, especially if the data can be considered to be idempotent.
# However, duplicate data can increase the size of the dataset, and if it is not
# idempotent, then it would not be appropriate to process the duplicates.

# In[28]:


# a DataFrame with lots of duplicate data
data = pd.DataFrame({'a': ['x'] * 3 + ['y'] * 4,'b': [1, 1, 2, 3, 3, 4, 4]})
data


# In[35]:


# reports which rows are duplicates based upon
# if the data in all columns was seen before
data.duplicated()    #第2个开始重复的元素，标记为True，The default operation is to keep the frst row of the duplicates. 
# drop duplicate rows retaining first row of the duplicates
data.drop_duplicates()
#It is also possible to use the inplace=True parameter to remove the rows without making a copy
# drop duplicate rows, only keeping the first

#If you want to check for duplicates based on a smaller set of columns, you can
#specify a list of columns names:
# add a column c with values 0..6
# this makes .duplicated() report no duplicate rows
data['c'] = range(7)
data.duplicated()
# but if we specify duplicates to be dropped only in columns a & b
# they will be dropped
data
data.drop_duplicates(['a', 'b'])



# In[31]:


data


# ### Transforming Data
# Another part of tidying data involves transforming existing data into another
# presentation. This may be needed for the following reasons:
# • Values are not in the correct units
# • Values are qualitative and need to be converted to appropriate numeric values
# • There is extraneous data that either wastes memory and processing time, or
# can affect results simply by being included
# To address these situations, we can take one or more of the following actions:
# • Map values to other values using a table lookup process
# • Explicitly replace certain values with other values (or even another type
# of data)
# • Apply methods to transform the values based on an algorithm
# • Simply remove extraneous columns and rows

# #### Mapping
# One of the basic tasks in data transformations is mapping of a set of values to
# another set. pandas provides a generic ability to map values using a lookup table
# (via a Python dictionary or a pandas Series) using the .map() method. This method
# performs the mapping by matching the values of the outer Series with the index
# labels of the inner Series, and returning a new Series with the index labels of the
# outer Series but the values from the inner Series:

# In[38]:


# create two Series objects to demonstrate mapping
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b", 3: "c"})
x,y
# map values in x to values in y
x.map(y)


# In[40]:


# three in x will not align / map to a value in y
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b"})
x.map(y)


# ### Replacing values

# In[44]:


# create a Series to demonstrate replace
s = pd.Series([0., 1., 2., 3., 2., 4.])
s
# replace all items with index label 2 with value 5
s.replace(2, 5)
# replace all items with new values
s.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
# replace using entries in a dictionary
s.replace({0: 10, 1: 100})


# In[ ]:


If using .replace() on a DataFrame, it is possible to specify different replacement
values for each column. This is performed by passing a Python dictionary to the
.replace() method, where the keys of the dictionary represent the names of the
columns where replacement is to occur and the values of the dictionary are values
that you want to replace. The second parameter to the method is the value that will
be replaced where any matches are found.


# In[45]:


# DataFrame with two columns
df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})
df


# In[46]:


# specify different replacement values for each column
df.replace({'a': 1, 'b': 8}, 100)


# In[48]:


# demonstrate replacement with pad method
# set first item to 10, to have a distinct replacement value
s[0] = 10
s
# replace items with index label 1, 2, 3, using fill from the
# most recent value prior to the specified labels (10)
s.replace([1, 2, 3], method='pad')


# ### Applying functions to transform data
# In situations where a direct mapping or substitution will not suffce, it is possible to
# apply a function to the data to perform an algorithm on the data. pandas provides
# the ability to apply functions to individual items, entire columns, or entire rows,
# providing incredible ﬂexibility in transformation.
# Functions can be applied using the conveniently named .apply() method, which
# given a Python function, will iteratively call the function passing in each value
# from a Series, or each Series representing a DataFrame column, or a list of values
# representing each row in a DataFrame. The choice of technique to be used depends
# on whether the object is a Series or a DataFrame object, and when a DataFrame
# object, depending upon which axis is specifed.

# In[49]:


# demonstrate applying a function to every item of a Series
s = pd.Series(np.arange(0, 5))
s.apply(lambda v: v * 2)


# In[52]:


# demonstrate applying a sum on each column
df = pd.DataFrame(np.arange(12).reshape(4, 3),columns=['a', 'b', 'c'])
df


# In[54]:


# calculate cumulative sum of items in each column
df.apply(lambda col1: col1.sum())


# In[55]:


# calculate the sum of items in each row
df.apply(lambda row: row.sum(), axis=1)


# In[56]:


# create a new column 'interim' with a * b
df['interim'] = df.apply(lambda r: r.a * r.b, axis=1)
df


# In[58]:


# and now a 'result' column with 'interim' + 'c'
df['result'] = df.apply(lambda r: r.interim + r.c, axis=1)
df


# In[59]:


# replace column a with the sum of columns a, b and c
df.a = df.a + df.b + df.c
df


# In[ ]:


As a matter of practice, replacing a column with completely new values is not the
best way to do things and often leads to situations of temporary insanity trying to
debug problems caused by data that is lost. In pandas, it is a common practice to just
add new rows or columns (or totally new objects), and if memory or performance
becomes a problem later on, do the optimizations as required.
实际上，用完全新的值替换列并不是最好的方法，而且通常会导致暂时的精神错乱，试图调试丢失数据导致的问题。
在pandas中，只添加新行或列（或完全是新对象）是一种常见的做法，如果以后内存或性能出现问题，请根据需要进行优化。

Another point to note, is that a pandas DataFrame is not a spreadsheet where cells
are assigned formulas and can be recalculated when cells that are referenced by the
formula change. If you desire this to happen, you will need to execute the formulas
whenever the dependent data changes. On the ﬂip side, this is more effcient than with
spreadsheets as every little change does not cause a cascade of operations to occur.
另一点需要注意的是，熊猫数据帧不是一个电子表格，在该表格中，单元格被指定为公式，并且当公式引用的
单元格发生更改时，可以重新计算。如果您希望发生这种情况，则需要在依赖数据更改时执行公式。
在flyip方面，这比使用电子表格更有效，因为每一个微小的变化都不会导致一系列操作的发生。


# In[60]:


# create a 3x5 DataFrame
# only second row has a NaN
df = pd.DataFrame(np.arange(0, 15).reshape(3,5))
df.loc[1, 2] = np.nan
df


# In[61]:


# demonstrate applying a function to only rows having
# a count of 0 NaN values
df.dropna().apply(lambda x: x.sum(), axis=1)


# In[ ]:


The .apply() method was
always passed an entire row or column. If you desire to apply a function to every
individual item in the DataFrame one by one, then .applymap() is the method to use.


# In[62]:


# use applymap to format all items of the DataFrame
df.applymap(lambda x: '%.2f' % x)


# In[ ]:


第二版P84.   2015第一版 P268

