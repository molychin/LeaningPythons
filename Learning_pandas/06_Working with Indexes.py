
# coding: utf-8

# # Configuring panadas

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

# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])


# # The importance of indexes

# In[2]:


# create DataFame of random numbers and a key column
np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(10000), 'key':range(100, 10100)})
df[:5]


# In[3]:


# boolean select where key is 10099
df[df.key==10099]


# In[4]:


# time the select
get_ipython().magic('timeit df[df.key==10099]')


# In[5]:


# move key to the index
df_with_index = df.set_index(['key'])
df_with_index[:5]


# In[6]:


# now can lookup with the index
df_with_index.loc[10099]


# In[7]:


# and this is a lot faster
get_ipython().magic('timeit df_with_index.loc[10099]')


# # The fundamental index type: Index

# In[8]:


# show that the columns are actually an index
temps = pd.DataFrame({ "City": ["Missoula", "Philadelphia"],
                       "Temperature": [70, 80] })
temps


# In[9]:


# we can see columns is an index
temps.columns


# # Integer index labels using Int64Index and RangeIndex

# In[10]:


# explicitly create an Int64Index
df_i64 = pd.DataFrame(np.arange(10, 20), index=np.arange(0, 10))
df_i64[:5]


# In[11]:


# view the index
df_i64.index


# In[12]:


# by default we are given a RangeIndex
df_range = pd.DataFrame(np.arange(10, 15))
df_range[:5]


# In[13]:


df_range.index


# # Floating point labels using Float64Index

# In[14]:


# indexes using a Float64Index
df_f64 = pd.DataFrame(np.arange(0, 1000, 5), 
                      np.arange(0.0, 100.0, 0.5))
df_f64.iloc[:5] # need iloc to slice first five


# In[15]:


df_f64.index


# # Representing discrete intervals using IntervalIndex

# In[16]:


# a DataFrame with an IntervalIndex
df_interval = pd.DataFrame({ "A": [1, 2, 3, 4]},
                    index = pd.IntervalIndex.from_breaks(
                        [0, 0.5, 1.0, 1.5, 2.0]))
df_interval


# In[17]:


df_interval.index


# # Categorical values as an index: CategoricalIndex

# In[18]:


# create a DataFrame with a Categorical coulmn
df_categorical = pd.DataFrame({'A': np.arange(6),
                               'B': list('aabbca')})
df_categorical['B'] = df_categorical['B'].astype('category', 
                                          categories=list('cab'))
df_categorical


# In[19]:


# shift the categorical column to the index
df_categorical = df_categorical.set_index('B')
df_categorical.index


# In[20]:


# lookup values in category 'a'
df_categorical.loc['a']


# # Indexing by dates and times using DatetimeIndex

# In[21]:


# create a DatetimeIndex from a date range
rng = pd.date_range('5/1/2017', periods=5, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts


# In[22]:


ts.index


# # Indexing periods of time using PeriodIndex

# In[23]:


# explicily create a PeriodIndex
periods = pd.PeriodIndex(['2017-1', '2017-2', '2017-3'], freq='M')
periods


# In[24]:


# use the index in a Series
period_series = pd.Series(np.random.randn(len(periods)), 
                          index=periods)
period_series


# # Creating and using an index with a Series or DataFrame

# In[25]:


# create a DatetimeIndex
date_times = pd.DatetimeIndex(pd.date_range('5/1/2017', 
                                            periods=5, 
                                            freq='H'))
date_times


# In[26]:


# create a DataFrame using the index
df_date_times = pd.DataFrame(np.arange(0, len(date_times)), 
                             index=date_times)
df_date_times


# In[27]:


# set the index of a DataFrame
df_date_times.index = pd.DatetimeIndex(pd.date_range('6/1/2017', 
                                                     periods=5, 
                                                     freq='H'))
df_date_times


# # Selecting values using an index

# In[28]:


# create a series
s = pd.Series(np.arange(0, 5), index=list('abcde'))
s


# In[29]:


# lookup by index label
s['b']


# In[30]:


# explicit lookup by label
s.loc['b']


# In[31]:


# create a DataFrame with two columns
df = pd.DataFrame([ np.arange(10, 12), 
                    np.arange(12, 14)], 
                  columns=list('ab'), 
                  index=list('vw'))
df


# In[32]:


# this returns the column 'a'
df['a']


# In[33]:


# return the row 'w' by label
df.loc['w']


# In[34]:


# slices the Series from index label b to d
s['b':'d']


# In[35]:


# this explicitly slices from label b to d
s.loc['b':'d']


# In[36]:


# and this looks up rows by label
s.loc[['a', 'c', 'e']]


# # Moving data to and from the index 

# In[37]:


# examine asome of the sp500 data
sp500[:5]


# In[38]:


# reset the index which moves the values in the index to a column
index_moved_to_col = sp500.reset_index()
index_moved_to_col[:5]


# In[39]:


# and now set the Sector column to be the index
index_moved_to_col.set_index('Sector')[:5]


# In[40]:


# reindex to have MMM, ABBV, and FOO index labels
reindexed = sp500.reindex(index=['MMM', 'ABBV', 'FOO'])
# note that ABT and ACN are dropped and FOO has NaN values
reindexed


# In[41]:


# reindex columns
sp500.reindex(columns=['Price', 
                       'Book Value', 
                       'NewCol'])[:5]


# # Hierarchical indexing

# In[42]:


# first, push symbol into a column
reindexed = sp500.reset_index()
# and now index sp500 by sector and symbol
multi_fi = reindexed.set_index(['Sector', 'Symbol'])
multi_fi[:5]


# In[43]:


# the index is a MultiIndex
type(multi_fi.index)


# In[44]:


# this has two levels
len(multi_fi.index.levels)


# In[45]:


# each index level is an index
multi_fi.index.levels[0]


# In[46]:


# each index level is an index
multi_fi.index.levels[1]


# In[47]:


# values of index level 0
multi_fi.index.get_level_values(0)


# In[48]:


# get all stocks that are Industrials
# note the result drops level 0 of the index
multi_fi.xs('Industrials')[:5]


# In[49]:


# select rows where level 1 (Symbol) is ALLE
# note that the Sector level is dropped from the result
multi_fi.xs('ALLE', level=1)


# In[50]:


# Industrials, without dropping the level
multi_fi.xs('Industrials', drop_level=False)[:5]


# In[51]:


# drill through the levels
multi_fi.xs('Industrials').xs('UPS')


# In[52]:


# drill through using tuples
multi_fi.xs(('Industrials', 'UPS'))

