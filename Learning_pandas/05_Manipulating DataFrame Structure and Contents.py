
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
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 60)

# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])


# # Renaming columns

# In[2]:


# rename the Book Value column to not have a space
# this returns a copy with the column renamed
newSP500 = sp500.rename(columns=
                        {'Book Value': 'BookValue'})
# print first 2 rows
newSP500[:2]


# In[3]:


# verify the columns in the original did not change
sp500.columns


# In[4]:


# this changes the column in-place
sp500.rename(columns=                  
             {'Book Value': 'BookValue'},                   
             inplace=True)
# we can see the column is changed
sp500.columns


# In[5]:


# and now we can use .BookValue
sp500.BookValue[:5]


# # Adding new columns with [] and .insert()

# In[6]:


# make a copy so that we keep the original data unchanged
sp500_copy = sp500.copy()
# add the new column
sp500_copy['RoundedPrice'] = sp500.Price.round()
sp500_copy[:2]


# In[7]:


# make a copy so that we keep the original data unchanged
copy = sp500.copy()
# insert sp500.Price * 2 as the 
# second column in the DataFrame
copy.insert(1, 'RoundedPrice', sp500.Price.round())
copy[:2]


# # Adding columns through enlargement

# In[8]:


# copy of subset / slice
ss = sp500[:3].copy()
# add the new column initialized to 0
ss.loc[:,'PER'] = 0
# take a look at the results
ss


# In[9]:


# copy of subset / slice
ss = sp500[:3].copy()
# add the new column initialized with random numbers
np.random.seed(123456)
ss.loc[:,'PER'] = pd.Series(np.random.normal(size=3), index=ss.index)
# take a look at the results
ss


# # Adding columns using concatenation

# In[10]:


# create a DataFrame with only the RoundedPrice column
rounded_price = pd.DataFrame({'RoundedPrice':    
                              sp500.Price.round()})
# concatenate along the columns axis
concatenated = pd.concat([sp500, rounded_price], axis=1)
concatenated[:5]


# In[11]:


# create a DataFrame with only the RoundedPrice column
rounded_price = pd.DataFrame({'Price': sp500.Price.round()})
rounded_price[:5]


# In[12]:


# this will result in duplicate Price columm
dups = pd.concat([sp500, rounded_price], axis=1)
dups[:5]


# In[13]:


# retrieves both Price columns
dups.Price[:5]


# # Reordering columns

# In[14]:


# return a new DataFrame with the columns reversed
reversed_column_names = sp500.columns[::-1]
sp500[reversed_column_names][:5]


# # Replacing the contents of a column

# In[15]:


# this occurs in-place so let's use a copy
copy = sp500.copy()
# replace the Price column data with the new values
# instead of adding a new column
copy.Price = rounded_price.Price
copy[:5]


# In[16]:


# this occurs in-place so let's use a copy
copy = sp500.copy()
# replace the Price column data wwith rounded values
copy.loc[:,'Price'] = rounded_price.Price
copy[:5]


# # Deleting columns

# In[17]:


# Example of using del to delete a column
# make a copy as this is done in-place
copy = sp500.copy()
del copy['BookValue']
copy[:2]


# In[18]:


# Example of using pop to remove a column from a DataFrame
# first make a copy of a subset of the data frame as
# pop works in place
copy = sp500.copy()
# this will remove Sector and return it as a series
popped = copy.pop('Sector')
# Sector column removed in-place
copy[:2]


# In[19]:


# and we have the Sector column as the result of the pop
popped[:5]


# In[20]:


# Example of using drop to remove a column 
# make a copy of a subset of the data frame
copy = sp500.copy()
# this will return a new DataFrame with 'Sector’ removed
# the copy DataFrame is not modified
afterdrop = copy.drop(['Sector'], axis = 1)
afterdrop[:5]


# # Appending rows from other DataFrame objects with .append()

# In[21]:


# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# append df1 and df2
appended = df1.append(df2)
# the result is the rows of the first followed by 
# those of the second
appended


# In[22]:


# data frame using df1.index and just a PER column
# also a good example of using a scalar value
# to initialize multiple rows
df3 = pd.DataFrame(0.0, 
                   index=df1.index,
                   columns=['PER'])
df3


# In[23]:


# append df1 and df3
# each has three rows, so 6 rows is the result
# df1 had no PER column, so NaN from for those rows
# df3 had no BookValue, Price or Sector, so NaN's
df1.append(df3)


# In[24]:


# ignore index labels, create default index
df1.append(df3, ignore_index=True)


# # Concatenating rows

# In[25]:


# copy the first three rows of sp500
df1 = sp500.iloc[0:3].copy()
# copy 10th and 11th rows
df2 = sp500.iloc[[10, 11, 2]]
# pass them as a list
pd.concat([df1, df2])


# In[26]:


# copy df2
df2_2 = df2.copy()
# add a column to df2_2 that is not in df1
df2_2.insert(3, 'Foo', pd.Series(0, index=df2.index))
# see what it looks like
df2_2


# In[27]:


# now concatenate
pd.concat([df1, df2_2])


# In[28]:


# specify keys
r = pd.concat([df1, df2_2], keys=['df1', 'df2'])
r


# # Adding and replacing rows via setting with enlargement

# In[29]:


# get a small subset of the sp500 
# make sure to copy the slice to make a copy
ss = sp500[:3].copy()
# create a new row with index label FOO
# and assign some values to the columns via a list
ss.loc['FOO'] = ['the sector', 100, 110]
ss


# # Removing rows using .drop()

# In[30]:


# get a copy of the first 5 rows of sp500
ss = sp500[:5]
ss


# In[31]:


# drop rows with labels ABT and ACN
afterdrop = ss.drop(['ABT', 'ACN'])
afterdrop[:5]


# # Removing rows using Boolean selection

# In[32]:


# determine the rows where Price > 300
selection = sp500.Price > 300
# report number of rows and number that will be dropped
(len(selection), selection.sum())


# In[33]:


# select the complement of the expression
# note the use of the complement of the selection
price_less_than_300 = sp500[~selection]
price_less_than_300


# # Removing rows using a slice

# In[34]:


# get only the first three rows
only_first_three = sp500[:3]
only_first_three


# In[35]:


# first three, but a copy of them
only_first_three = sp500[:3].copy()
only_first_three

