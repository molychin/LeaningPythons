
# coding: utf-8

# ## The pandas DataFrame Object

# In[ ]:


The pandas DataFrame object extends the capabilities of the Series object into
two-dimensions. A Series object adds an index to a NumPy array but can only
associate a single data item per index label, a DataFrame integrates multiple Series
objects by aligning them along common index labels. This automatic alignment by
index label provides a seamless view across all the Series at each index label that
has the appearance of a row in a table.
pandas数据帧对象将序列对象的功能扩展到二维。序列对象将索引添加到numpy数组，但每个索引标签
只能关联一个数据项，数据帧通过将多个序列对象与常用索引标签对齐来集成它们。通过索引标签自动
对齐，可以在每个索引标签处的所有系列中提供无缝视图，这些索引标签的外观与表中的行类似。

A DataFrame object can be thought of as a dictionary-like container of one or more
Series objects, or as a spreadsheet, probably the best description for those new to
pandas is to compare a DataFrame object to a relational database table. However,
even that comparison is limited, as a DataFrame object has very distinct qualities
(such as automatic data alignment of series) that make it much more capable for
exploratory data analysis than either a spreadsheet or relational database table.
一个数据帧对象可以被认为是一个或多个系列对象的字典式容器，或者是一个电子表格，对于熊猫新
手来说，最好的描述可能是将一个数据帧对象与一个关系数据库表进行比较。然而，即使这种比较也是
有限的，因为数据帧对象具有非常明显的特性（例如，序列的自动数据对齐），使其比电子表格或关系
数据库表更能进行探索性数据分析。

A DataFrame also introduces the concept of multiple axes, specifically the horizontal
and vertical axis. Functions from pandas can then be applied to either axis, in essence
stating that the operation be applied horizontally to all the values in the rows, or up
and down each column.
数据框架还引入了多轴的概念，特别是水平轴和垂直轴。然后可以将pandas的函数应用于任意一个轴，
本质上说，该操作将水平应用于行中的所有值，或者向上和向下应用于每一列。


# In[ ]:


Specifically, in this chapter we will cover:
• Creating a DataFrame from scratch
• Loading sample data to demonstrate the capabilities of a DataFrame object
• Selecting columns of a DataFrame object
• Selecting rows and values of a DataFrame using the index
• Selecting rows of a DataFrame using Boolean selection
• Adding, replacing, and deleting columns from a DataFrame
• Adding, replacing, and deleting rows from a DataFrame
• Modifying scalar values in a DataFrame
• Arithmetic operations on the DataFrame objects
• Resetting and reindexing a DataFrame
• Hierarchically indexing a DataFrame
• Statistical methods of a DataFrame
• Summarized data and statistical methods of a DataFrame


# In[11]:


import numpy as np
import pandas as pd

# create a DataFrame from a 2-d ndarray
pd.DataFrame(np.array([[10, 11], [20, 21]]))
#Each row of the array forms a row in the DataFrame object. Since we did not specify
#an index, pandas creates a default int64 index in the same manner as a Series
#object. Since we did not specify column names, pandas also assigns the names for
#each column with a zero-based integer series.

# create a DataFrame for a list of Series objects
df1 = pd.DataFrame([pd.Series(np.arange(10, 15)),
    pd.Series(np.arange(15, 20))])
df1
# what's the shape of this DataFrame
df1.shape # it is two rows by 5 columns
# specify column names
df = pd.DataFrame(np.array([[10, 11], [20, 21]]),
    columns=['a', 'b'])
df                  
# what are the names of the columns?
df.columns
# rename the columns
df.columns = ['c1', 'c2']
df
# create a DataFrame with named columns and rows
df = pd.DataFrame(np.array([[0, 1], [2, 3]]),
    columns=['c1', 'c2'],index=['r1', 'r2'])
df
# retrieve the index of the DataFrame
df.index
# create a DataFrame with two Series objects
# and a dictionary
s1 = pd.Series(np.arange(1, 6, 1))
s2 = pd.Series(np.arange(6, 11, 1))
pd.DataFrame({'c1': s1, 'c2': s2})
#A DataFrame also performs automatic alignment of the data for each Series passed in
#by a dictionary. For example, the following code adds a third column in the DataFrame
#initialization. This third Series contains two values and will specify its index. When
#the DataFrame is created, each series in the dictionary is aligned with each other by the
#index label, as it is added to the DataFrame object. 
# demonstrate alignment during creation
s3 = pd.Series(np.arange(12, 14), index=[1, 2])
df = pd.DataFrame({'c1': s1, 'c2': s2, 'c3': s3})
df


# In[27]:


# read in the data and print the first five rows
# use the Symbol column as the index, and
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol',usecols=[0, 2, 3, 7])   #读取指定列

# peek at the first 5 rows of the data using .head()
sp500.tail()
# how many rows of data?
len(sp500)
# examine the index
sp500.index
# get the columns
sp500.columns
# peek at the first 5 rows of the data using .head()
sp500.head()


# In[19]:


# read in the data
one_mon_hist = pd.read_csv("data/omh.csv")
# examine the first three rows
one_mon_hist[:3]


# In[46]:


#Selecting columns of a DataFrame
# get first and second columns (1 and 2) by location
sp500 = pd.read_csv("data/sp500.csv")
sp500.head()
sp500[['Sector','Price']]
#sp500[[0,3]]   #抛出错误
# create a new DataFrame with integers as the column names
# make sure to use .copy() or change will be in-place
df = sp500.copy()
#df.columns=[0]  #抛出错误
#df.columns=[ 'Name']
df.head()
df.columns
df['Sector']
# attribute access of the column by name
sp500.Price


# #### Selecting rows and values of a DataFrame using the index
# • Slicing using the [] operator
# • Label or location based lookup using .loc, .iloc, and .ix
# • Scalar lookup by label or location using .at and .iat

# In[60]:


sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol')   #读取指定列
# first five rows
sp500[:5]
# ABT through ACN labels
sp500['ABT':'ACN']   #抛出异常
# get row with label MMM
# returned as a Series
sp500.loc['MMM']
# rows with label MMM and MSFT
# this is a DataFrame result
sp500.loc[['MMM', 'MSFT']]
# get rows in locations 0 and 2
sp500.iloc[[0, 2]]
# by label in both the index and column
sp500.at['MMM', 'Price']   #定位到元素
# by location. Row 0, column 1
sp500.iat[0, 1]


# In[63]:


#Selecting rows of a DataFrame by Boolean selection
# what rows have a price < 100?
sp500.Price < 100
# now get the rows with Price < 100
sp500[sp500.Price < 100]
# get only the Price where Price is < 10 and > 0
r = sp500[(sp500.Price < 10) & (sp500.Price > 0)] [['Price']]
r


# In[ ]:


Modifying the structure and content of DataFrame
The structure and content of a DataFrame can be mutated in several ways. Rows and
columns can be added and removed, and data within either can be modified to take
on new values. Additionally, columns, as well as index labels, can also be renamed.
Each of these will be described in the following sections.


# In[67]:


#Renaming columns
# rename the Book Value column to not have a space
# this returns a copy with the column renamed
df = sp500.rename(columns={'Book Value': 'BookValue'})   #修改列名
# print first 2 rows
df[:2]
# verify the columns in the original did not change
sp500.columns
# this changes the column in-place
sp500.rename(columns={'Book Value': 'BookValue'},inplace=True)
# we can see the column is changed
sp500.columns
# and now we can use .BookValue
sp500.BookValue[:5]



# In[ ]:


Adding and inserting columns
Alignment of data is important to understanding this process, as pandas does not
simply concatenate the Series to the DataFrame. pandas will first align the data in
the DataFrame with the Series using the index from both objects, and fill in the data
from the Series into the new DataFrame at the appropriate index labels.


# In[69]:


# make a copy
copy = sp500.copy()
# add a new column to the copy
copy['TwicePrice'] = sp500.Price * 2    #将新列插入到列的末尾
copy[:2]

copy = sp500.copy()
# insert sp500.Price * 2 as the
# second column in the DataFrame
copy.insert(1, 'TwicePrice', sp500.Price * 2)   #将新列插入到指定位置
copy[:2]


# In[ ]:


It is important to remember that this is not simply inserting a column into the
DataFrame. The alignment process used here is performing a left join of the DataFrame
and the Series by their index labels, and then creating the column and populating the
data in the appropriate cells in the DataFrame from matching entries in the Series. If
an index label in the DataFrame is not matched in the Series, the value used will be
NaN. Items in the Series that do not have a matching label will be ignored.


# In[71]:


# extract the first four rows and just the Price column
rcopy = sp500[0:3][['Price']].copy()
rcopy
# create a new Series to merge as a column
# one label exists in rcopy (MSFT), and MMM does not
s = pd.Series({'MMM': 'Is in the DataFrame','MSFT': 'Not in the DataFrame'} )
s
# add rcopy into a column named 'Comment'
rcopy['Comment'] = s    #新列插入时，如匹配不到index，则改值不插入
rcopy


# In[ ]:


Replacing the contents of a column
In general, assignment of a Series to a column using the [] operator will either
create a new column if the column does not already exist, or replace the contents
of a column if it already exists. To demonstrate replacement, the following code
replaces the Price column with the result of the multiplication, instead of creating
a new column


# In[72]:


copy = sp500.copy()
# replace the Price column data with the new values
# instead of adding a new column
copy.Price = sp500.Price * 2   #替代
copy[:5]


# In[74]:


# copy all 500 rows
copy = sp500.copy()
# this just copies the first 2 rows of prices
prices = sp500.iloc[[3, 1, 0]].Price.copy()
# examine the extracted prices
prices
# now replace the Prices column with prices
copy.Price = prices
# it's not really simple insertion, it is alignment
# values are put in the correct place according to labels
copy


# In[ ]:


Deleting columns in a DataFrame
Columns can be deleted from a DataFrame by using the del keyword, the pop(column)
method of the DataFrame, or by calling the drop() method of the DataFrame.

The behavior of each of these differs slightly:
• del will simply delete the Series from the DataFrame (in-place)
• pop() will both delete the Series and return the Series as a result (also in-place)
• drop(labels, axis=1) will return a new DataFrame with the column(s)
removed (the original DataFrame object is not modified)


# In[1]:


import numpy as np
import pandas as pd

sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol')   #读取指定列
# Example of using del to delete a column
# make a copy of a subset of the data frame
copy = sp500[:5].copy()
copy
# delete the BookValue column
# deletion is in-place
del copy['Book Value']  #删除某列
copy
# Example of using pop to remove a column from a DataFrame
# first make a copy of a subset of the data frame
# pop works in-place
copy = sp500[:2].copy()
# this will remove Sector and return it as a series
popped = copy.pop('Sector')
# Sector column removed in-place
copy
popped


# In[2]:


#The .drop() method can be used to remove both rows and columns. To use it to
#remove a column, specify axis=1:
# Example of using drop to remove a column
# make a copy of a subset of the DataFrame
copy = sp500[:2].copy()
print(copy)
# this will return a new DataFrame with 'Sector' removed
# the copy DataFrame is not modified
afterdrop = copy.drop(['Sector'], axis = 1)
afterdrop


# In[3]:


Adding rows to a DataFrame
Rows can be added to a DataFrame object via several different operations:
• Appending a DataFrame to another   #允许重行
• Concatenation of two DataFrame objects
• Setting with enlargement


# In[4]:


# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# append df1 and df2
appended = df1.append(df2)
# the result is the rows of the first followed by
# those of the second
appended
# DataFrame using df1.index and just a PER column
# also a good example of using a scalar value
# to initialize multiple rows
df3 = pd.DataFrame(0.0,index=df1.index,columns=['PER'])
df3
# append df1 and df3
# each has three rows, so 6 rows is the result
# df1 had no PER column, so NaN for those rows
# df3 had no BookValue, Price or Sector, so NaN values
#df1.append(df3)
df1.append(df3,sort=True)


# In[5]:


#Concatenating DataFrame objects with pd.concat()
# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# pass them as a list
pd.concat([df1, df2])



# In[8]:


# copy df2
df2_2 = df2.copy()
# add a column to df2_2 that is not in df1
df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
# see what it looks like
df2_2
# now concatenate
pd.concat([df1, df2_2])
# specify keys
r = pd.concat([df1, df2_2], keys=['df1', 'df2'])
r


# In[18]:


# first three rows, columns 0 and 1
#print(sp500.head())
#df3 = sp500[:3][[0, 1]]    #error
df3=sp500[:3][['Name','Sector']]
df3
# first three rows, column 2
df4 = sp500[:3][['Price']]
df4
pd.concat([df3, df4], axis=1)     #按列进行合并
# make a copy of df4
df4_2 = df4.copy()
# add a column to df4_2, that is also in df3
df4_2.insert(1, 'Sector', pd.Series(1, index=df4_2.index))
df4_2
# demonstrate duplicate columns
pd.concat([df3, df4_2], axis=1)    #合并时，允许同名列




# In[ ]:


To be very specific, pandas is performing an outer join along the labels of the specified
axis. An inner join can be specified using the join='inner' parameter, which
changes the operation from being a sorted union of distinct labels to the distinct
values of the intersection of the labels. To demonstrate, the following selects two
subsets of the financial data with one row in common and performs an inner join:


# In[22]:


# first three rows and first two columns
df5 =sp500[:3][['Name','Sector']]
print(df5)
# row 2 through 4 and first two columns
df6 = sp500[2:5][['Name','Sector']]
print(df6)
# inner join on index labels will return in only one row
pd.concat([df5, df6], join='inner', axis=1)


# In[26]:


#Adding rows (and columns) via setting with enlargement
# get a small subset of the sp500
# make sure to copy the slice to make a copy
ss = sp500[:3][['Name','Price','Market Cap']].copy()
print(ss.head())
# create a new row with index label FOO
# and assign some values to the columns via a list
ss.loc['FOO'] = ['the sector', 100, 110]
ss
#Note that the change is made in place. If FOO already exists as an index label, then
#the column data would be replaced. This is one of the means of updating data in a
#DataFrame in-place, as .loc not only retrieves row(s), but also lets you modify the
#results that are returned.

# add the new column initialized to 0
ss.loc[:,'PER'] = 0
# take a look at the results
ss


# In[ ]:


Removing rows from a DataFrame
Removing rows from a DataFrame object is normally performed using one of
three techniques:
• Using the .drop() method
• Boolean selection
• Selection using a slice

Technically, only the .drop() method removes rows in-place on the source object.
The other techniques either create a copy without specific rows, or a view into the
rows that are not to be dropped. Details of each are given in the following sections.


# In[29]:


# get a copy of the first 5 rows of sp500
ss = sp500[:5].copy()
ss
# drop rows with labels ABT and ACN
afterdrop = ss.drop(['ABT', 'ACN'])   #通过标签名删除
afterdrop
# note that ss is not modified
ss


# In[3]:


#Removing rows using Boolean selection
import numpy as np
import pandas as pd

sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol')   #读取指定列
# determine the rows where Price > 300
selection = sp500.Price > 300
# select the complement
withPriceLessThan300 = sp500[~selection]
withPriceLessThan300
#Removing rows using a slice
# get only the first three rows
onlyFirstThree = sp500[:3]
onlyFirstThree
#Remember, that this result is a slice. Therefore, it is a view into the DataFrame.
#Data has not been removed from the sp500 object. Changes to these three rows
#will change the data in sp500. To prevent this from occurring, the proper action
#is to make a copy of the slice, as follows:
# first three, but a copy of them
onlyFirstThree = sp500[:3].copy()
onlyFirstThree


# In[6]:


#Changing scalar values in a DataFrame
# get a subset / copy of the data
subset = sp500[:3].copy()
subset
subset.loc['MMM', 'Price'] = 10
subset.loc['ABBV', 'Price'] = 20
subset


# In[ ]:


.loc may suffer from lower performance, as compared to .iloc, due to the possibility
of needing to map the label values into locations. The following example gets the
location of the specific row and column that is desired to be changed and then uses
.iloc to execute the change (the examples only change one price for brevity)


# In[8]:


# subset of the first three rows
subset = sp500[:3].copy()
# get the location of the Price column
price_loc = sp500.columns.get_loc('Price')
# get the location of the MMM row
abt_row_loc = sp500.index.get_loc('ABT')
# change the price
subset.iloc[abt_row_loc, price_loc] = 1000
subset


# In[ ]:


This may be look like overkill for this small example. But if this is where code is
being executed frequently, such as in a loop or in response to market changes,
looking up the locations once and always using .loc with those values, will
give significant performance gains over the other options.


# In[4]:


#Arithmetic on a DataFrame
import numpy as np
import pandas as pd

# set the seed to allow replicatable results
np.random.seed(123456)
# create the DataFrame
df = pd.DataFrame(np.random.randn(5, 4),columns=['A', 'B', 'C', 'D'])
df
# multiply everything by 2
df * 2

# get first row
s = df.iloc[0]
# subtract first row from every row of the DataFrame
diff = df - s
diff
# subtract DataFrame from Series
diff2 = s - df
diff2
# B, C
s2 = s[1:3]
# add E
s2['E'] = 0
# see how alignment is applied in math
df + s2
# get rows 1 through three, and only B, C columns
subframe = df[1:4][['B', 'C']]
# we have extracted a little square in the middle of the df
subframe
# demonstrate the alignment of the subtraction
df - subframe

# get the A column
a_col = df['A']
df.sub(a_col, axis=0)


# In[11]:


#Resetting and reindexing
sp500 = pd.read_csv("data/sp500.csv",index_col='Symbol')   #读取指定列
sp500
# reset the index, moving it into a column
reset_sp500 = sp500.reset_index()
reset_sp500
# move the Symbol column into the index
reset_sp500.set_index('Symbol')

# get first four rows
subset = sp500[:4].copy()
subset
# reindex to have MMM, ABBV, and FOO index labels
reindexed = subset.reindex(index=['MMM', 'ABBV', 'FOO'])
# note that ABT and ACN are dropped and FOO has NaN values
reindexed

# reindex columns
subset.reindex(columns=['Price','Book Value','NewCol'])  #修改列索引



# In[19]:


# first, push symbol into a column
reindexed = sp500.reset_index()
# and now index sp500 by sector and symbol
multi_fi = reindexed.set_index(['Sector', 'Symbol'])
multi_fi
# the index is a MultiIndex
type(multi_fi.index)
# examine the index
#print (multi_fi.index)
# this has two levels
len(multi_fi.index.levels)
# each index level is an index
multi_fi.index.levels[0]
# each index level is an index
multi_fi.index.levels[1]
# values of the index level 0
multi_fi.index.get_level_values(0)


# In[34]:


#Summarized data and descriptive statistics  统计函数
# read in the data
one_mon_hist = pd.read_csv("data/omh.csv")
# examine the first three rows
print(one_mon_hist[:3])
# calc the mean of the values in each column
one_mon_hist.mean()
# calc the mean of the values in each row
one_mon_hist.mean(axis=1)  #按行统计
# calc the variance of the values in each column
one_mon_hist.var()      #方差
# calc the median of the values in each column
one_mon_hist.median()   #中位数
# location of min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].min()   #最小值
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].max()   #最大值
# location of the min price for both stocks
one_mon_hist[['MSFT', 'AAPL']].idxmin()  #最小值的索引值
# and location of the max
one_mon_hist[['MSFT', 'AAPL']].idxmax()
# find the mode of this Series
s = pd.Series([1, 2, 3, 3, 5])
s.mode()
# there can be more than one mode
s = pd.Series([1, 2, 3, 3, 5, 1])
s.mode()

# calculate a cumulative product
pd.Series([1, 2, 3, 4]).cumprod()   #累积，累乘
# calculate a cumulative sum
pd.Series([1, 2, 3, 4]).cumsum()   #累加
# summary statistics
one_mon_hist.describe()  #显示常用的统计结果
# get summary stats on non-numeric data
#This has given us the count variable of items that are not part of NaN, the number of
#unique items that are not part of NaN, the most common item (top), and the number
#of times the most frequent item occurred (freq).
s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
s.describe()
# get summary stats on non-numeric data
s.count()


# In[36]:


#A list of unique items can be obtained using the .unique() method:
# return a list of unique items
s.unique()
#The number of occurrences of each unique (value that is not part of NaN) value can be
#determined with the .value_counts() method:
# number of occurrences of each unique value
s.value_counts()



# In[ ]:


第二版P84.   2015第一版 P185

