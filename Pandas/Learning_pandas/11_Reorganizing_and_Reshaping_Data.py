
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


# # Concatenating data

# In[2]:


# two Series objects to concatenate
s1 = pd.Series(np.arange(0, 3))
s2 = pd.Series(np.arange(5, 8))
s1


# In[3]:


s2


# In[4]:


# concatenate them
pd.concat([s1, s2])


# In[5]:


# create two DataFrame objects to concatenate
# using the same index labels and column names, 
# but different values
df1 = pd.DataFrame(np.arange(9).reshape(3, 3), 
                   columns=['a', 'b', 'c'])
#df2 has 9 .. 18
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3), 
                   columns=['a', 'b', 'c'])
df1


# In[6]:


df2


# In[7]:


# do the concat
pd.concat([df1, df2])


# In[8]:


# demonstrate concatenating two DataFrame objects with
# different columns
df1 = pd.DataFrame(np.arange(9).reshape(3, 3), 
                   columns=['a', 'b', 'c'])
df2 = pd.DataFrame(np.arange(9, 18).reshape(3, 3), 
                   columns=['a', 'c', 'd'])
df1


# In[9]:


df2


# In[10]:


# do the concat, NaN's will be filled in for
# the d column for df1 and b column for df2
pd.concat([df1, df2])


# In[11]:


# concat the two objects, but create an index using the
# given keys 
c = pd.concat([df1, df2], keys=['df1', 'df2'])
# note in the labeling of the rows in the output
c


# In[12]:


# we can extract the data originating from
# the first or second source DataFrame
c.loc['df2']


# In[13]:


# concat df1 and df2 along columns
# aligns on row labels, has duplicate columns
pd.concat([df1, df2], axis=1)


# In[14]:


# a new DataFrame to merge with df1
# this has two common row labels (2, 3) 
# common columns (a) and one disjoint column
# in each (b in df1 and d in df2)
df3 = pd.DataFrame(np.arange(20, 26).reshape(3, 2), 
                   columns=['a', 'd'], 
                   index=[2, 3, 4])
df3


# In[15]:


# concat them. Alignment is along row labels
# columns first from df1 and then df3, with duplicates.
# NaN filled in where those columns do not exist in the source
pd.concat([df1, df3], axis=1)


# In[16]:


# do an inner join instead of outer
# results in one row
pd.concat([df1, df3], axis=1, join='inner')


# In[17]:


# add keys to the columns
df = pd.concat([df1, df2], 
               axis=1,
               keys=['df1', 'df2'])
df


# In[18]:


# retrieve the data that originated from the 
# DataFrame with key 'df2'
df.loc[:, 'df2']


# In[19]:


# append does a concatenate along axis=0 
# duplicate row index labels can result
df1.append(df2)


# In[20]:


# remove duplicates in the result index by ignoring the 
# index labels in the source DataFrame objects
df1.append(df2, ignore_index=True)


# # An overview of merges

# In[21]:


# these are our customers
customers = {'CustomerID': [10, 11],
             'Name': ['Mike', 'Marcia'],
             'Address': ['Address for Mike',
                         'Address for Marcia']}
customers = pd.DataFrame(customers)
customers


# In[22]:


# and these are the orders made by our customers
# they are related to customers by CustomerID
orders = {'CustomerID': [10, 11, 10],
          'OrderDate': [date(2014, 12, 1),
                        date(2014, 12, 1),
                        date(2014, 12, 1)]}
orders = pd.DataFrame(orders)
orders


# In[23]:


# merge customers and orders so we can ship the items
customers.merge(orders)


# In[24]:


# data to be used in the remainder of this section's examples
left_data = {'key1': ['a', 'b', 'c'], 
            'key2': ['x', 'y', 'z'],
            'lval1': [ 0, 1, 2]}
right_data = {'key1': ['a', 'b', 'c'],
              'key2': ['x', 'a', 'z'], 
              'rval1': [ 6, 7, 8 ]}
left = pd.DataFrame(left_data, index=[0, 1, 2])
right = pd.DataFrame(right_data, index=[1, 2, 3])
left


# In[25]:


right


# In[26]:


# demonstrate merge without specifying columns to merge
# this will implicitly merge on all common columns
left.merge(right)


# In[27]:


# demonstrate merge using an explicit column
# on needs the value to be in both DataFrame objects
left.merge(right, on='key1')


# In[28]:


# merge explicitly using two columns
left.merge(right, on=['key1', 'key2'])


# In[29]:


# join on the row indices of both matrices
pd.merge(left, right, left_index=True, right_index=True)


# # Specifying the join semantics of a merge operation

# In[30]:


# outer join, merges all matched data, 
# and fills unmatched items with NaN
left.merge(right, how='outer')


# In[31]:


# left join, merges all matched data, and only fills unmatched 
# items from the left dataframe with NaN filled for the 
# unmatched items in the result 
# rows with labels 0 and 2 
# match on key1 and key2 the row with label 1 is from left

left.merge(right, how='left')


# In[32]:


# right join, merges all matched data, and only fills unmatched
# item from the right with NaN filled for the unmatched items
# in the result 
# rows with labels 0 and 2 match on key1 and key2
# the row with label 1 is from right
left.merge(right, how='right')


# In[33]:


# join left with right (default method is outer)
# and since these DataFrame objects have duplicate column names
# we just specify lsuffix and rsuffix
left.join(right, lsuffix='_left', rsuffix='_right')


# In[34]:


# join left with right with an inner join
left.join(right, lsuffix='_left', rsuffix='_right', how='inner')


# # Pivoting

# In[35]:


# read in accelerometer data
sensor_readings = pd.read_csv("data/accel.csv")
sensor_readings


# In[36]:


# extract X-axis readings
sensor_readings[sensor_readings['axis'] == 'X']


# In[37]:


# pivot the data.  Interval becomes the index, the columns are
# the current axes values, and use the readings as values
sensor_readings.pivot(index='interval', 
                     columns='axis', 
                     values='reading')


# # Stacking using non-hierarchical indexes

# In[38]:


# simple DataFrame with one column
df = pd.DataFrame({'a': [1, 2]}, index={'one', 'two'})
df


# In[39]:


# push the column to another level of the index
# the result is a Series where values are looked up through
# a multi-index
stacked1 = df.stack()
stacked1


# In[40]:


# lookup one / a using just the index via a tuple
stacked1[('one', 'a')]


# In[41]:


# DataFrame with two columns
df = pd.DataFrame({'a': [1, 2],
                   'b': [3, 4]}, 
                  index={'one', 'two'})
df


# In[42]:


# push the two columns into a single level of the index
stacked2 = df.stack()
stacked2


# In[43]:


# lookup value with index of one / b
stacked2[('one', 'b')]


# # Unstacking using hierarchical indexes

# In[44]:


# make two copies of the sensor data, one for each user
user1 = sensor_readings.copy()
user2 = sensor_readings.copy()
# add names to the two copies
user1['who'] = 'Mike'
user2['who'] = 'Mikael'
# for demonstration, lets scale user2's readings
user2['reading'] *= 100
# and reorganize this to have a hierarchical row index
multi_user_sensor_data = pd.concat([user1, user2])             .set_index(['who', 'interval', 'axis'])
multi_user_sensor_data


# In[45]:


# lookup user data for Mike using just the index
multi_user_sensor_data.loc['Mike']


# In[46]:


# readings for all users and axes at interval 1
multi_user_sensor_data.xs(1, level='interval')


# In[47]:


# unstack the who level
multi_user_sensor_data.unstack()


# In[48]:


# unstack at level=0
multi_user_sensor_data.unstack(level=0)


# In[49]:


# unstack who and axis levels
unstacked = multi_user_sensor_data.unstack(['who', 'axis'])
unstacked


# In[50]:


# and we can of course stack what we have unstacked
# this re-stacks who
unstacked.stack(level='who')


# # Melting

# In[51]:


# we will demonstrate melting with this DataFrame
data = pd.DataFrame({'Name' : ['Mike', 'Mikael'],
                     'Height' : [6.1, 6.0],
                     'Weight' : [220, 185]})
data


# In[52]:


# melt it, use Name as the id's, 
# Height and Weight columns as the variables
pd.melt(data, 
        id_vars=['Name'],
        value_vars=['Height', 'Weight'])


# # Performance benefits of stacked data

# In[53]:


# stacked scalar access can be a lot faster than
# column access

# time the different methods
import timeit
t = timeit.Timer("stacked1[('one', 'a')]", 
                 "from __main__ import stacked1, df")
r1 = timeit.timeit(lambda: stacked1.loc[('one', 'a')], 
                   number=10000)
r2 = timeit.timeit(lambda: df.loc['one']['a'], 
                   number=10000)
r3 = timeit.timeit(lambda: df.iloc[1, 0], 
                   number=10000)

# and the results are...  Yes, it's the fastest of the three
r1, r2, r3

