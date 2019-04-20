
# coding: utf-8

# # Configuring pandas

# In[1]:


# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 60)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# # Working with missing data

# In[2]:


# create a DataFrame with 5 rows and 3 columns
df = pd.DataFrame(np.arange(0, 15).reshape(5, 3), 
               index=['a', 'b', 'c', 'd', 'e'], 
               columns=['c1', 'c2', 'c3'])
df


# In[3]:


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
df


# # Determining NaN values in Series and DataFrame objects

# In[4]:


# which items are NaN?
df.isnull()


# In[5]:


# count the number of NaN's in each column
df.isnull().sum()


# In[6]:


# total count of NaN values
df.isnull().sum().sum()


# In[7]:


# number of non-NaN values in each column
df.count()


# In[8]:


# and this counts the number of NaN's too
(len(df) - df.count()).sum()


# In[9]:


# which items are not null?
df.notnull()


# # Selecting out or dropping missing data

# In[10]:


# select the non-NaN items in column c4
df.c4[df.c4.notnull()]


# In[11]:


# .dropna will also return non NaN values
# this gets all non NaN items in column c4
df.c4.dropna()


# In[12]:


# dropna returns a copy with the values dropped
# the source DataFrame / column is not changed
df.c4


# In[13]:


# on a DataFrame this will drop entire rows
# where there is at least one NaN
# in this case, that is all rows
df.dropna()


# In[14]:


# using how='all', only rows that have all values
# as NaN will be dropped
df.dropna(how = 'all')


# In[15]:


# flip to drop columns instead of rows
df.dropna(how='all', axis=1) # say goodbye to c5


# In[16]:


# make a copy of df
df2 = df.copy()
# replace two NaN cells with values
df2.loc['g'].c1 = 0
df2.loc['g'].c3 = 0
df2


# In[17]:


# now drop columns with any NaN values
df2.dropna(how='any', axis=1) 


# In[18]:


# only drop columns with at least 5 NaN values
df.dropna(thresh=5, axis=1)


# # How pandas handles NaN’s in mathematical operations

# In[19]:


# create a NumPy array with one NaN value
a = np.array([1, 2, np.nan, 3])
# create a Series from the array
s = pd.Series(a)
# the mean of each is different
a.mean(), s.mean()


# In[20]:


# demonstrate sum, mean and cumsum handling of NaN
# get one column
s = df.c4
s.sum(), # NaN's treated as 0


# In[21]:


s.mean() # NaN also treated as 0


# In[22]:


# as 0 in the cumsum, but NaN's preserved in result Series
s.cumsum()


# In[23]:


# in arithmetic, a NaN value will result in NaN
df.c4 + 1


# # Filling in missing data

# In[24]:


# return a new DataFrame with NaN's filled with 0
filled = df.fillna(0)
filled


# In[25]:


# NaN's don't count as an item in calculating
# the means
df.mean()


# In[26]:


# having replaced NaN with 0 can make
# operations such as mean have different results
filled.mean()


# # Forward and backwards filling of missing values

# In[27]:


# extract the c4 column and fill NaNs forward
df.c4.fillna(method="ffill")


# In[28]:


# perform a backwards fill
df.c4.fillna(method="bfill")


# # Filling using index labels

# In[29]:


# create a new Series of values to be 
# used to fill NaN's where index label matches
fill_values = pd.Series([100, 101, 102], index=['a', 'e', 'g'])
fill_values


# In[30]:


# using c4, fill using fill_values
# a, e and g will be filled with matching values
df.c4.fillna(fill_values)


# In[31]:


# fill NaN values in each column with the 
# mean of the values in that column
df.fillna(df.mean())


# # Interpolation of missing values

# In[32]:


# linear interpolate the NaN values from 1 through 2
s = pd.Series([1, np.nan, np.nan, np.nan, 2])
s.interpolate()


# In[33]:


# create a time series, but missing one date in the Series
ts = pd.Series([1, np.nan, 2], 
            index=[datetime(2014, 1, 1), 
                   datetime(2014, 2, 1),                   
                   datetime(2014, 4, 1)])
ts


# In[34]:


# linear interpolate based on number of items in the Series
ts.interpolate()


# In[35]:


# this accounts for the fact that we don't have
# an entry for 2014-03-01
ts.interpolate(method="time")


# In[36]:


# a Series to demonstrate index label based interpolation
s = pd.Series([0, np.nan, 100], index=[0, 1, 10])
s


# In[37]:


# linear interpolate
s.interpolate()


# In[38]:


# interpolate based upon the values in the index
s.interpolate(method="values")


# # Handling Duplicate Data

# In[39]:


# a DataFrame with lots of duplicate data
data = pd.DataFrame({'a': ['x'] * 3 + ['y'] * 4, 
                     'b': [1, 1, 2, 3, 3, 4, 4]})
data


# In[40]:


# reports which rows are duplicates based upon
# if the data in all columns was seen before
data.duplicated()


# In[41]:


# drop duplicate rows retaining first row of the duplicates
data.drop_duplicates()


# In[42]:


# drop duplicate rows, only keeping the first 
# instance of any data
data.drop_duplicates(keep='last')


# In[43]:


# add a column c with values 0..6
# this makes .duplicated() report no duplicate rows
data['c'] = range(7)
data.duplicated()


# In[44]:


# but if we specify duplicates to be dropped only in columns a & b
# they will be dropped
data.drop_duplicates(['a', 'b'])


# # Mapping

# In[45]:


# create two Series objects to demonstrate mapping
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b", 3: "c"})
x


# In[46]:


y


# In[47]:


# map values in x to values in y 
x.map(y)


# In[48]:


# three in x will not align / map to a value in y
x = pd.Series({"one": 1, "two": 2, "three": 3})
y = pd.Series({1: "a", 2: "b"})
x.map(y)


# # Replacing values

# In[49]:


# create a Series to demonstrate replace
s = pd.Series([0., 1., 2., 3., 2., 4.])
s


# In[50]:


# replace all items with index label 2 with value 5
s.replace(2, 5)


# In[51]:


# replace all items with new values
s.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])


# In[52]:


# replace using entries in a dictionary
s.replace({0: 10, 1: 100})


# In[53]:


# DataFrame with two columns
df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})
df


# In[54]:


# specify different replacement values for each column
df.replace({'a': 1, 'b': 8}, 100)


# In[55]:


# demonstrate replacement with pad method
# set first item to 10, to have a distinct replacement value
s[0] = 10
s


# In[56]:


# replace items with index label 1, 2, 3, using fill from the
# most recent value prior to the specified labels (10)
s.replace([1, 2, 3], method='pad')


# # Applying functions to transform data

# In[57]:


# demonstrate applying a function to every item of a Series
s = pd.Series(np.arange(0, 5))
s.apply(lambda v: v * 2)


# In[58]:


# demonstrate applying a sum on each column
df = pd.DataFrame(np.arange(12).reshape(4, 3), 
                  columns=['a', 'b', 'c'])
df


# In[59]:


# calculate cumulative sum of items in each column
df.apply(lambda col: col.sum())


# In[60]:


# calculate sum of items in each row
df.apply(lambda row: row.sum(), axis=1)


# In[61]:


# create a new column 'interim' with a * b
df['interim'] = df.apply(lambda r: r.a * r.b, axis=1)
df


# In[62]:


# and now a 'result' column with 'interim' + 'c'
df['result'] = df.apply(lambda r: r.interim + r.c, axis=1)
df


# In[63]:


# replace column a with the sum of columns a, b and c
df.a = df.a + df.b + df.c
df


# In[64]:


# create a 3x5 DataFrame
# only second row has a NaN
df = pd.DataFrame(np.arange(0, 15).reshape(3,5))
df.loc[1, 2] = np.nan
df


# In[65]:


# demonstrate applying a function to only rows having
# a count of 0 NaN values
df.dropna().apply(lambda x: x.sum(), axis=1)


# In[66]:


# use applymap to format all items of the DataFrame
df.applymap(lambda x: '%.2f' % x)

