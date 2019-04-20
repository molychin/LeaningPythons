
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
pd.set_option('display.width', 80)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# # Creating a Series using Python lists and dictionaries

# In[2]:


# create a series of multiple values from a list
s = pd.Series([10, 11, 12, 13, 14])
s


# In[3]:


# value stored at index label 3
s[3]


# In[4]:


# create a Series of alphas
pd.Series(['Mike', 'Marcia', 'Mikael', 'Bleu'])


# In[5]:


# a sequence of 5 values, all 2
pd.Series([2]*5)


# In[6]:


# use each character as a value
pd.Series(list('abcde'))


# In[7]:


# create Series from dict
pd.Series({'Mike': 'Dad', 
           'Marcia': 'Mom', 
           'Mikael': 'Son', 
           'Bleu': 'Best doggie ever' })


# # Creation using NumPy functions

# In[8]:


# 4 through 8
pd.Series(np.arange(4, 9))


# In[9]:


# 0 through 9
pd.Series(np.linspace(0, 9, 5))


# In[10]:


# random numbers
np.random.seed(12345) # always generate the same values
# 5 normally random numbers
pd.Series(np.random.normal(size=5))


# # Creation using a scalar value

# In[11]:


# create a one item Series
s = pd.Series(2)
s


# In[12]:


# create the Series
s = pd.Series(np.arange(0, 5))
# multiple all values by 2
s * 2


# # The .index and .values properties

# In[13]:


# get the values in the Series
s = pd.Series([1, 2, 3])
s.values


# In[14]:


# show that this is a numpy array
type(s.values)


# In[15]:


# get the index of the Series
s.index


# # The size and shape of a Series

# In[16]:


# example series
s = pd.Series([0, 1, 2, 3])
len(s)


# In[17]:


# .size is also the # of items in the Series
s.size


# In[18]:


# .shape is a tuple with one value
s.shape


# # Specifying an index at creation

# In[19]:


# explicitly create an index
labels = ['Mike', 'Marcia', 'Mikael', 'Bleu']
role = ['Dad', 'Mom', 'Son', 'Dog']
s = pd.Series(labels, index=role)
s


# In[20]:


# examine the index
s.index


# In[21]:


# who is the Dad?
s['Dad']


# # Heads, tails and takes

# In[22]:


# a ten item Series
s = pd.Series(np.arange(1, 10), 
              index=list('abcdefghi'))


# In[23]:


# show the first five
s.head()


# In[24]:


# the first three
s.head(n = 3) # s.head(3) is equivalent


# In[25]:


# the last five
s.tail()


# In[26]:


# the last 3
s.tail(n = 3) # equivalent to s.tail(3)


# In[27]:


# only take specific items by position
s.take([1, 5, 8])


# # Lookup by label using the [] and .ix[] operators

# In[28]:


# we will use this series to examine lookups
s1 = pd.Series(np.arange(10, 15), index=list('abcde'))
s1


# In[29]:


# get the value with label 'a'
s1['a']


# In[30]:


# get multiple items
s1[['d', 'b']]


# In[31]:


# gets values based upon position
s1[[3, 1]]


# In[32]:


# to demo lookup by matching labels as integer values
s2 = pd.Series([1, 2, 3, 4], index=[10, 11, 12, 13])
s2


# In[33]:


# this is by label not position
s2[[13, 10]]


# # Explicit position lookup with .iloc[]

# In[34]:


# explicitly  by position
s1.iloc[[0, 2]]


# In[35]:


# explicitly  by position
s2.iloc[[3, 2]]


# # Explicit label lookup with .loc[]

# In[36]:


# explicit via labels
s1.loc[['a', 'd']]


# In[37]:


# get items at position 11 an d12
s2.loc[[11, 12]]


# In[38]:


# -1 and 15 will be NaN
s1.loc[['a', 'f']]


# # Slicing a Series into subsets

# In[39]:


# a Series to use for slicing
# using index labels not starting at 0 to demonstrate 
# position based slicing
s = pd.Series(np.arange(100, 110), index=np.arange(10, 20))
s


# In[40]:


# slice showing items at position 1 thorugh 5
s[1:6]


# In[41]:


# lookup via list of positions
s.iloc[[1, 2, 3, 4, 5]]


# In[42]:


# items at position 1, 3, 5
s[1:6:2]


# In[43]:


# first five by slicing, same as .head(5)
s[:5]


# In[44]:


# fourth position to the end
s[4:]


# In[45]:


# every other item in the first five positions
s[:5:2]


# In[46]:


# every other item starting at the fourth position
s[4::2]


# In[47]:


# reverse the Series
s[::-1]


# In[48]:


# every other starting at position 4, in reverse
s[4::-2]


# In[49]:


# -4:, which means the last 4 rows
s[-4:]


# In[50]:


# :-4, all but the last 4
s[:-4]


# In[51]:


# equivalent to s.tail(4).head(3)
s[-4:-1]


# In[52]:


# used to demonstrate the next two slices
s = pd.Series(np.arange(0, 5), 
              index=['a', 'b', 'c', 'd', 'e'])
s


# In[53]:


# slices by position as the index is characters
s[1:3]


# In[54]:


# this slices by the strings in the index
s['b':'d']


# # Alignment via index labels

# In[55]:


# First series for alignment
s1 = pd.Series([1, 2], index=['a', 'b'])
s1


# In[56]:


# Second series for alignment
s2 = pd.Series([4, 3], index=['b', 'a'])
s2


# In[57]:


# add them
s1 + s2


# In[58]:


# multiply all values in s3 by 2
s1 * 2


# In[59]:


# scalar series using s3's index
t = pd.Series(2, s1.index)
t


# In[60]:


# multiply s1 by t
s1 * t


# In[61]:


# we will add this to s1
s3 = pd.Series([5, 6], index=['b', 'c'])
s3


# In[62]:


# s1 and s3 have different sets of index labels
# NaN will result for a and c
s1 + s3


# In[63]:


# 2 'a' labels
s1 = pd.Series([1.0, 2.0, 3.0], index=['a', 'a', 'b'])
s1


# In[64]:


# 3 a labels
s2 = pd.Series([4.0, 5.0, 6.0, 7.0], index=['a', 'a', 'c', 'a'])
s2


# In[65]:


# will result in 6 'a' index labels, and NaN for b and c
s1 + s2


# # Boolean selection

# In[66]:


# which rows have values that are > 5?
s = pd.Series(np.arange(0, 5), index=list('abcde'))
logical_results = s >= 3
logical_results


# In[67]:


# select where True
s[logical_results]


# In[68]:


# a little shorter version
s[s > 5]


# In[69]:


# commented as it throws an exception
# s[s >= 2 and s < 5]


# In[70]:


# correct syntax
s[(s >=2) & (s < 5)]


# In[71]:


# are all items >= 0?
(s >= 0).all()


# In[72]:


# any items < 2?
s[s < 2].any()


# In[73]:


# how many values < 2?
(s < 2).sum()


# # Reindexing a Series

# In[74]:


# sample series of five items
np.random.seed(123456)
s = pd.Series(np.random.randn(5))
s


# In[75]:


# change the index
s.index = ['a', 'b', 'c', 'd', 'e']
s


# In[76]:


# a series that we will reindex
np.random.seed(123456)
s1 = pd.Series(np.random.randn(4), ['a', 'b', 'c', 'd'])
s1


# In[77]:


# reindex with different number of labels
# results in dropped rows and/or NaN's
s2 = s1.reindex(['a', 'c', 'g'])
s2


# In[78]:


# different types for the same values of labels
# causes big trouble
s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([3, 4, 5], index=['0', '1', '2'])
s1 + s2


# In[79]:


# reindex by casting the label types
# and we will get the desired result
s2.index = s2.index.values.astype(int)
s1 + s2


# In[80]:


# fill with 0 instead of NaN
s2 = s.copy()
s2.reindex(['a', 'f'], fill_value=0)


# In[81]:


# create example to demonstrate fills
s3 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
s3


# In[82]:


# forward fill example
s3.reindex(np.arange(0,7), method='ffill')


# In[83]:


# backwards fill example
s3.reindex(np.arange(0,7), method='bfill')


# # Modifying a Series in-place

# In[84]:


# generate a Series to play with
np.random.seed(123456)
s = pd.Series(np.random.randn(3), index=['a', 'b', 'c'])
s


# In[85]:


# change a value in the Series
# this is done in-place
# a new Series is not returned that has a modified value
s['d'] = 100
s


# In[86]:


# modify the value at 'd' in-place
s['d'] = -100
s


# In[87]:


# remove a row / item
del(s['a'])
s


# In[88]:


copy = s.copy() # preserve s
slice = copy[:2] # slice with first two rows
slice


# In[89]:


# change item with label 10 to 1000
slice['b'] = 0
# and see it in the source
copy

