
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


# # Creating a DataFrame using NumPy function results

# In[2]:


# From a 1-d array
pd.DataFrame(np.arange(1, 6))


# In[3]:


# create a DataFrame from a 2-d ndarray
df = pd.DataFrame(np.array([[10, 11], [20, 21]]))
df


# In[4]:


# retrieve the columns index
df.columns


# In[5]:


# specify column names
df = pd.DataFrame(np.array([[70, 71], [90, 91]]),
                  columns=['Missoula', 'Philadelphia'])
df


# In[6]:


# how many rows?
len(df)


# In[7]:


# what is the dimensionality
df.shape


# # Creating a DataFrame using a Python dictionary and pandas Series objects

# In[8]:


# initialization using a python dictionary
temps_missoula = [70, 71]
temps_philly = [90, 91]
temperatures = {'Missoula': temps_missoula,
                'Philadelphia': temps_philly}
pd.DataFrame(temperatures)


# In[9]:


# create a DataFrame for a list of Series objects
temps_at_time0 = pd.Series([70, 90])
temps_at_time1 = pd.Series([71, 91])
df = pd.DataFrame([temps_at_time0, temps_at_time1])
df


# In[10]:


# try to specify column names
df = pd.DataFrame([temps_at_time0, temps_at_time1],
                  columns=['Missoula', 'Philadelphia'])
df


# In[11]:


# specify names of columns after creation
df = pd.DataFrame([temps_at_time0, temps_at_time1])
df.columns = ['Missoula', 'Philadelphia']
df


# In[12]:


# construct using a dict of Series objects
temps_mso_series = pd.Series(temps_missoula)
temps_phl_series = pd.Series(temps_philly)
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series})
df


# In[13]:


# alignment occurs during creation
temps_nyc_series = pd.Series([85, 87], index=[1, 2])
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series,
                   'New York': temps_nyc_series})
df


# # Creating a DataFrame from a CSV file

# In[14]:


# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])


# In[15]:


# peek at the first 5 rows of the data using .head()
sp500.head()


# In[16]:


# how many rows of data?  Should be 500
len(sp500)


# In[17]:


# what is the shape?
sp500.shape


# In[18]:


# what is the size?
sp500.size


# In[19]:


# examine the index
sp500.index


# In[20]:


# get the columns
sp500.columns


# # Selecting columns of a DataFrame

# In[21]:


# retrieve the Sector column
sp500['Sector'].head()


# In[22]:


type(sp500['Sector'])


# In[23]:


# retrieve the Price and Book Value columns
sp500[['Price', 'Book Value']].head()


# In[24]:


# show that this is a DataFrame
type(sp500[['Price', 'Book Value']])


# In[25]:


# attribute access of column by name
sp500.Price


# # Selecting rows of a DataFrame

# In[26]:


# get row with label MMM
# returned as a Series
sp500.loc['MMM']


# In[27]:


# rows with label MMM and MSFT
# this is a DataFrame result
sp500.loc[['MMM', 'MSFT']]


# In[28]:


# get rows in location 0 and 2
sp500.iloc[[0, 2]]


# In[29]:


# get the location of MMM and A in the index
i1 = sp500.index.get_loc('MMM')
i2 = sp500.index.get_loc('A')
(i1, i2)


# In[30]:


# and get the rows
sp500.iloc[[i1, i2]]


# # Scalar lookup by label or location using .at[] and .iat[] 

# In[31]:


# by label in both the index and column
sp500.at['MMM', 'Price']


# In[32]:


# by location.  Row 0, column 1
sp500.iat[0, 1]


# # Slicing using the [] operator

# In[33]:


# first five rows
sp500[:5]


# In[34]:


# ABT through ACN labels
sp500['ABT':'ACN']


# # Selecting rows using Boolean selection

# In[35]:


# what rows have a price < 100?
sp500.Price < 100


# In[36]:


# now get the rows with Price < 100
sp500[sp500.Price < 100]


# In[37]:


# get only the Price where Price is < 10 and > 0
r = sp500[(sp500.Price < 10) & 
          (sp500.Price > 6)] ['Price']
r


# In[38]:


# price > 100 and in the Health Care Sector
r = sp500[(sp500.Sector == 'Health Care') & 
          (sp500.Price > 100.00)] [['Price', 'Sector']]
r


# # Selecting across both rows and columns

# In[39]:


# select the price and sector columns for ABT and ZTS
sp500.loc[['ABT', 'ZTS']][['Sector', 'Price']]

